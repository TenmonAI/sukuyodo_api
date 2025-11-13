# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

# ▼ 正しい import（フォルダ構成に対応）
from core.sukuyodo_calculator import (
    calculate_honmyo_shuku,      # ← spelling 正しい
    calculate_meigyo_shuku,
    calculate_tai_shuku,
    calculate_moon_phase,
    judge_phase_yinyang
)

from generators.diagnosis_generator import generate_sanyo_diagnosis

# -----------------------------------------------------
# FastAPI アプリ本体
# -----------------------------------------------------
app = FastAPI(
    title="宿曜AI 三位一体 診断API",
    description="天聞AIエンジンによる宿曜三位一体診断API",
    version="2.0.0"
)

# -----------------------------------------------------
# リクエストモデル
# -----------------------------------------------------
class RequestData(BaseModel):
    name: str
    birthdate: str  # "YYYY-MM-DD"


# -----------------------------------------------------
# 宿曜AI：三位一体診断API 本体
# -----------------------------------------------------
@app.post("/api/diagnose")
def diagnose(req: RequestData):

    # 生年月日パース
    date = datetime.strptime(req.birthdate, "%Y-%m-%d")

    # 月相から陰陽を求める
    age = calculate_moon_phase(date)
    phase = judge_phase_yinyang(age)

    # 本命宿 ID（0〜27）
    hon_id = calculate_honmyo_shuku((date.timetuple().tm_yday * 12.85) % 360)

    # 命業宿 ID（0〜27）
    mei_id = calculate_meigyo_shuku(hon_id)

    # 胎宿 ID（0〜27）
    tai_id = calculate_tai_shuku(hon_id)

    # 診断文章（天聞AI構文）
    result = generate_sanyo_diagnosis(
        hon_id,
        mei_id,
        tai_id,
        phase
    )

    # 返却（旧API形式 全部削除 → result のみ）
    return {
        "success": True,
        "name": req.name,
        "birthdate": req.birthdate,
        "result": result
    }


# -----------------------------------------------------
# 動作確認用
# -----------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "宿曜AI 三位一体 診断API（天聞AIエンジン）",
        "docs": "/docs",
        "diagnose": "/api/diagnose"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}

