# core/sukuyodo_calculator.py
# -----------------------------------------------------
# 宿曜占星術：本命宿・命業宿・胎宿の三位一体ロジック
# -----------------------------------------------------

import math
from datetime import datetime

# 28宿リスト
SHUKU_LIST = [
    "角", "亢", "氐", "房", "心", "尾", "箕",
    "斗", "牛", "女", "虚", "危", "室", "壁",
    "奎", "婁", "胃", "昴", "畢", "觜", "参",
    "井", "鬼", "柳", "星", "張", "翼", "軫"
]

# 本命宿
def calculate_honmyo_shuku(moon_longitude: float) -> int:
    index = int((moon_longitude % 360) / (360 / 28))
    return index

# 命業宿
def calculate_meigyo_shuku(hon_id: int) -> int:
    return (hon_id + 9) % 28

# 胎宿
def calculate_tai_shuku(hon_id: int) -> int:
    return (hon_id - 3) % 28

# 月齢
def calculate_moon_phase(date: datetime) -> float:
    diff = date - datetime(2001, 1, 1)
    days = diff.days + (diff.seconds / 86400)
    synodic_month = 29.53058867
    return days % synodic_month

# 陰陽判定
def judge_phase_yinyang(age: float) -> str:
    return "陽（成りゆく力）" if age < 14.7 else "陰（収める力）"

