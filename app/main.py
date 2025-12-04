from fastapi import FastAPI, Request # type: ignore
from fastapi.responses import HTMLResponse, JSONResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from chatbot import ask_rowan_bot # type: ignore

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")  # 


# Serve UI
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# POST endpoint for chatbot
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
        return JSONResponse({"error": "Server error", "details": str(e)}, status_code=500)


