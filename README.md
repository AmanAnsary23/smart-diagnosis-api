# 🩺 Smart Diagnosis API

An AI-powered medical diagnosis backend built with **FastAPI**, **Google Gemini API**, and **MongoDB**. Given a set of symptoms, it returns possible conditions with probability percentages and suggested next steps — and stores every request in a history log.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend Framework | FastAPI (Python) |
| AI Integration | Google Gemini API (`gemini-3-flash-preview`) |
| Database | MongoDB Atlas |
| Server | Uvicorn |
| Environment | python-dotenv |

---

## 📁 Project Structure

```
smart-diagnosis-api/
├── main.py                        # App entry point
├── routes/
│   └── diagnosis.py               # API route definitions
├── controllers/
│   └── diagnosis_controller.py    # Business logic
├── models/
│   └── diagnosis.py               # Pydantic request/response models
├── services/
│   └── ai_service.py              # Gemini AI integration
├── .env                           # Environment variables (not committed)
├── requirements.txt               # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/AmanAnsary23/smart-diagnosis-api.git
cd smart-diagnosis-api
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MONGODB_URL=your_mongodb_connection_string_here
```

- Get your **Gemini API Key** from [Google AI Studio](https://aistudio.google.com)
- Get your **MongoDB URL** from [MongoDB Atlas](https://mongodb.com/cloud/atlas)

### 5. Run the server

```bash
uvicorn main:app --reload
```

Server runs at: `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### `POST /diagnose`

Analyzes symptoms and returns possible medical conditions using Gemini AI.

**Request Body:**
```json
{
  "symptoms": "fever, cough, chest pain"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "conditions": [
      {
        "name": "Pneumonia",
        "probability": "60%",
        "next_steps": "Consult a doctor immediately for a physical exam and chest X-ray."
      },
      {
        "name": "Acute Bronchitis",
        "probability": "30%",
        "next_steps": "Monitor symptoms, stay hydrated, consult a physician if breathing worsens."
      },
      {
        "name": "Pleurisy",
        "probability": "10%",
        "next_steps": "Seek medical evaluation to check for inflammation of the lung lining."
      }
    ]
  }
}
```

---

### `GET /history`

Fetches all past diagnosis requests stored in MongoDB.

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "symptoms": "fever, cough, chest pain",
      "result": { ... },
      "timestamp": "2026-04-01T01:40:54.938294"
    }
  ]
}
```

---

## 🤖 How AI Integration Works

1. User sends symptoms via `POST /diagnose`
2. The `ai_service.py` constructs a structured prompt and sends it to **Google Gemini API**
3. Gemini returns 2-3 possible conditions in strict JSON format
4. The response is parsed, stored in **MongoDB**, and returned to the user

The prompt is engineered to always return consistent, structured JSON — making it reliable for production use.

---

## 🌐 Interactive API Docs

FastAPI provides auto-generated Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Requirements

```
fastapi
uvicorn
pymongo
motor
google-genai
python-dotenv
pydantic
```

Generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## ⚠️ Disclaimer

This API is built for demonstration purposes only. It is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for medical decisions.

---

## 👨‍💻 Author

**Aman Ansary**  
[GitHub](https://github.com/AmanAnsary23) • [LinkedIn](https://linkedin.com/in/aman-ansary)