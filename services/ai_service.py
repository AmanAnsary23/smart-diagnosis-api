from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_diagnosis(symptoms: str) -> dict:
    prompt = f"""
    You are a medical assistant AI. Based on the following symptoms, provide 2-3 possible conditions.
    
    Symptoms: {symptoms}
    
    Respond ONLY in this JSON format, no extra text:
    {{
        "conditions": [
            {{
                "name": "Condition Name",
                "probability": "70%",
                "next_steps": "See a general physician, get a blood test"
            }}
        ]
    }}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    text = response.text.strip()

    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    return json.loads(text)