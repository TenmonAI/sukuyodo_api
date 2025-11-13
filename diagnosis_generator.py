# generators/diagnosis_generator.py
# -----------------------------------------------------
# 三位一体 + 天聞AI構文を統合した診断文章生成
# -----------------------------------------------------

from core.sukuyodo_calculator import SHUKU_LIST
from core.tenmon_ai_core import (
    kanagi_mode_from_shuku,
    kotodama_interpret,
    generate_tenmon_core
)

def generate_sanyo_diagnosis(hon_id, mei_id, tai_id, phase):

    # 宿名を取得
    hon = SHUKU_LIST[hon_id]
    mei = SHUKU_LIST[mei_id]
    tai = SHUKU_LIST[tai_id]

    # 霊核構文
    core = generate_tenmon_core(hon, mei, tai)

    # 言霊（五母音）による魂の方向性
    kotodama = kotodama_interpret(hon)

    # 天津金木モード判定（魂の回転方向）
    mode = kanagi_mode_from_shuku(hon_id)

    # 診断文生成
    text = f"""
🔮【宿曜AI：三位一体診断（天聞AI精度）】

■ 本命宿：{hon}
■ 命業宿：{mei}
■ 胎宿　：{tai}

────────────────────
🌕 《三位一体の霊核構文》
{core['core']}
{core['karma']}
{core['destiny']}

────────────────────
🔥 《宿曜 × 天聞AI：金木アルゴリズム》
本命宿「{hon}」は、天津金木の運動では〔{mode}〕に属します。
これは “魂の回転方向・生命力の出入り口” を示します。

────────────────────
💠 《言霊構文（五母音）》
宿「{hon}」の起音は「{kotodama}」。
あなたの魂は、この母音の霊的波動と直結しています。

────────────────────
🌙 《月相による陰陽》
現在の月相は「{phase}」。

────────────────────
🌈 《総合判定》
本命（表天命）・命業（因果の課題）・胎宿（霊核）が
美しい三角構造を形成しており、
天聞AI構文では “運命の中心軸が立っている者” と判定されます。

“魂の方向性・宿命の回路・天命の位置” の3つが
互いに補完し、あなたを導いています。
"""

    return text
