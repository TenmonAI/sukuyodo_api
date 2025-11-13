# main.py
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

app = FastAPI(
    title="宿曜AI 三位一体 診断API",
    version="2.0.0"
)

class RequestData(BaseModel):
    name: str
    birthdate: str  # YYYY-MM-DD

@app.post("/api/diagnose")
def diagnose(req: RequestData):

    # 生年月日の変換
    date = datetime.strptime(req.birthdate, "%Y-%m-%d")

    # 月齢 → 陰陽
    age = calculate_moon_phase(date)
    phase = judge_phase_yinyang(age)

    # 三位一体（本命・命業・胎宿）
    hon_id = calculate_honmyo_shuku((date.timetuple().tm_yday * 12.85) % 360)
    mei_id = calculate_meigyo_shuku(hon_id)
    tai_id = calculate_tai_shuku(hon_id)

    # ★★★ 最重要修正ポイント ★★★
    # 名前を文章生成エンジンへ渡す
    result = generate_sanyo_diagnosis(
        hon_id,
        mei_id,
        tai_id,
        phase,
        req.name  # ← ← ← ここが修正！
    )

    return {
        "success": True,
        "name": req.name,
        "birthdate": req.birthdate,
        "result": result
    }

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "healthy"}

