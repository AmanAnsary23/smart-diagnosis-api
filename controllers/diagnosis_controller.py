from services.ai_service import get_diagnosis
from datetime import datetime
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"))
db = client["smart_diagnosis"]
collection = db["diagnoses"]

async def diagnose(symptoms: str) -> dict:
    try:
        result = get_diagnosis(symptoms)
        
        record = {
            "symptoms": symptoms,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
        collection.insert_one(record)
        
        return result
    
    except Exception as e:
        raise Exception(f"Diagnosis failed: {str(e)}")


async def get_history() -> list:
    try:
        records = list(collection.find({}, {"_id": 0}))
        return records
    
    except Exception as e:
        raise Exception(f"History fetch failed: {str(e)}")