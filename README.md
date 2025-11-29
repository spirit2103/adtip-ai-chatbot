# 🤖 AI Chatbot using FastAPI + Hugging Face + Microsoft Phi-2

This project is a lightweight yet powerful **AI chatbot API** built using:

- **FastAPI**
- **Microsoft Phi-2 (LLM)**
- **Hugging Face Transformers**
- **MySQL Database**

The chatbot can generate intelligent responses and store chat history.

---

## 📂 Project Features

- 🧠 Uses **Microsoft Phi-2** model (< 1.5GB quantized)
- 🚀 High-performance API using **FastAPI**
- 💾 Stores conversation history in MySQL
- 🧪 Fully testable via `Postman` or `/docs` Swagger
- 🎭 Generates sentiment-based reply when needed

---

## 📦 Requirements

- Python **3.10+**
- MySQL Installed
- Internet access (First-time model download only)

---

## 🔧 Installation Guide
```sh
### 1️⃣ Clone Repository
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
```
#### windows
```sh
venv\Scripts\activate
```

#### Linux/mac
```sh
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Setup MySQL Database
```sh
>Run the following command in MySQL:
CREATE DATABASE chatbot_db;
> Create table
CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT,
    bot_reply TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5️⃣ Configure Database Credentials
```sh
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "chatbot_db"
}
```

## 🤖 Model Used: Microsoft Phi-2

| Property   | Value                   |
| ---------- | ----------------------- |
| Model Name | microsoft/phi-2         |
| Parameters | 2.7B                    |
| Size       | ~1.5 GB (quantized)     |
| Best Use   | Chatbots, Reasoning, QA |


## ▶️ Run the Application
### to run backend
```sh
uvicorn main:app --reload --port 6500
```

Once Running, Open:
http://127.0.0.1:6500

## 🧪 API Usage
### Swaggers UI
```sh
>Visit:
http://127.0.0.1:6500/docs
```

## 🔹 Using Postman
### Send a POST request to:
http://127.0.0.1:6500/chat

### In Body -> raw
```sh
{
  "message": "Hello"
}
```

## 📜 API Endpoints
| Method | Endpoint   | Description            |
| ------ | ---------- | ---------------------- |
| GET    | `/`        | Server status          |
| POST   | `/chat`    | Ask chatbot a question |
| GET    | `/history` | View saved messages    |


##🗂 Project Structure
```sh
📦 ai-chatbot
 ┣ 📄 main.py
 ┣ 📄 config.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ┗ 📁 venv
```

## ❤️ Credits
Microsoft Research – Phi-2 Model
Hugging Face Transformers
FastAPI Framework
