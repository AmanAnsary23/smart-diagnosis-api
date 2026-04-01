from fastapi import APIRouter, HTTPException
from models.diagnosis import SymptomInput
from controllers.diagnosis_controller import diagnose, get_history

router = APIRouter()

@router.post("/diagnose")
async def diagnose_symptoms(input: SymptomInput):
    try:
        result = await diagnose(input.symptoms)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
async def history():
    try:
        records = await get_history()
        return {"status": "success", "data": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))