from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from chatbot import ask_rowan_bot
import traceback

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/ask")
async def ask_bot(request: Request):
    data = await request.json()
    query = data.get("query", "")

    if not query:
        return JSONResponse({"error": "Query is empty"}, status_code=400)

    print("\n=== Incoming Query ===")
    print(query)

    try:
        answer = ask_rowan_bot(query)
        return {"answer": answer}

    except Exception as e:
        print("ERROR:", e)
        traceback.print_exc()
        return JSONResponse({"error": "Server error", "details": str(e)}, status_code=500)

# ⬇️ Only needed if running via `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)




