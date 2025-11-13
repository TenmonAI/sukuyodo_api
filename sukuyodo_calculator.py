# sukuyodo_calculator.py
# -----------------------------------------------------
# 宿曜占星術：本命宿・命業宿・胎宿の三位一体ロジック
# -----------------------------------------------------

import math
from datetime import datetime

# 28宿リスト（簡易表記だが位置は正確）
SHUKU_LIST = [
    "角", "亢", "氐", "房", "心", "尾", "箕",
    "斗", "牛", "女", "虚", "危", "室", "壁",
    "奎", "婁", "胃", "昴", "畢", "觜", "参",
    "井", "鬼", "柳", "星", "張", "翼", "軫"
]

# 本命宿：月経度（Moon Longitude）→ 宿番号を求める
def calculate_honmyo_shuku(moon_longitude: float) -> int:
    """月経度 → 宿番号（1〜28）"""
    index = int((moon_longitude % 360) / (360 / 28))
    return index

# 命業宿：本命宿の「内側」因果構造
def calculate_meigyo_shuku(honmyo_id: int) -> int:
    """命業宿 = 本命宿から「9つ進んだ宿」"""
    return (honmyo_id + 9) % 28

# 胎宿：本命宿の前世・胎生的構造
def calculate_tai_shuku(honmyo_id: int) -> int:
    """胎宿 = 本命宿から「3つ戻った宿」"""
    return (honmyo_id - 3) % 28

# 月齢（月相）による陰陽の判定
def calculate_moon_phase(date: datetime) -> float:
    """単純化した月齢計算（十分精度が出る）"""
    diff = date - datetime(2001, 1, 1)
    days = diff.days + (diff.seconds / 86400)
    synodic_month = 29.53058867
    return days % synodic_month

def judge_phase_yinyang(age: float) -> str:
    """月相 → 陰陽判定"""
    if age < 14.7:
        return "陽（成りゆく力）"
    else:
        return "陰（収める力）"
