document.getElementById("send-btn").onclick = async () => {
    const input = document.getElementById("user-input");
    const query = input.value.trim();
    if (!query) return;

    addMessage("You", query);

    const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await res.json();

    addMessage("Bot", data.answer || "Server Error");
    input.value = "";
};

function addMessage(sender, text) {
    const chat = document.getElementById("chat-container");
    const div = document.createElement("div");
    div.className = sender === "You" ? "user-msg" : "bot-msg";
    div.textContent = `${sender}: ${text}`;
    chat.appendChild(div);
}
