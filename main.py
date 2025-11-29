from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import mysql.connector
from config import DB_CONFIG

# -------------------------
# DB CONNECTION
# -------------------------
db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

# -------------------------
# MODEL (Hugging Face)
# -------------------------
MODEL_NAME = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto"
)

chat = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,
    temperature=0.4,
    top_p=0.92,
    repetition_penalty=1.2
)

# -------------------------
# FASTAPI APP
# -------------------------
app = FastAPI(title="HuggingFace Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/chat")
def chat_api(request: ChatRequest):
    user_message = request.message.strip()

    # PROMPT TEMPLATE
    prompt = f"""
You are a friendly and intelligent assistant. 
Answer the question clearly and professionally.
Avoid repeating sentences. Keep it helpful.

User: {user_message}
Assistant:
"""

    response = chat(prompt)[0]["generated_text"]

    # Clean model output
    response = response.split("Assistant:")[-1].strip()

    # Save to DB
    cursor.execute(
        "INSERT INTO history (user_message, bot_reply) VALUES (%s, %s)",
        (user_message, response)
    )
    db.commit()

    return {"reply": response}


@app.get("/history")
def get_history():
    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    rows = cursor.fetchall()

    return [
        {"id": r[0], "user": r[1], "bot": r[2], "timestamp": str(r[3])}
        for r in rows
    ]
