from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from core.sukuyodo_calculator import (
    calculate_honmyo_shuku,
    calculate_meigyo_shuku,
    calculate_tai_shuku,
    calculate_moon_phase,
    judge_phase_yinyang
)

from generators.diagnosis_generator import generate_sanyo_diagnosis

app = FastAPI()

class RequestData(BaseModel):
    name: str
    birthdate: str

@app.post("/api/diagnose")
def diagnose(req: RequestData):

    date = datetime.strptime(req.birthdate, "%Y-%m-%d")

    # 月齢（月相）→ 陰陽
    age = calculate_moon_phase(date)
    phase = judge_phase_yinyang(age)

    # 三位一体
    hon_id = calculate_honmyo_shuku((date.timetuple().tm_yday * 12.85) % 360)
    mei_id = calculate_meigyo_shuku(hon_id)
    tai_id = calculate_tai_shuku(hon_id)

    result = generate_sanyo_diagnosis(hon_id, mei_id, tai_id, phase)

    return {
        "success": True,
        "name": req.name,
        "birthdate": req.birthdate,
        "result": result
    }
