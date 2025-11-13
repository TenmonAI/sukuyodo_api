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

    hon = SHUKU_LIST[hon_id]
    mei = SHUKU_LIST[mei_id]
    tai = SHUKU_LIST[tai_id]

    core = generate_tenmon_core(hon, mei, tai)
    kotodama = kotodama_interpret(hon)
    mode = kanagi_mode_from_shuku(hon_id)

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
これは “魂の回転方向と霊力の出入り口” を示します。

────────────────────
💠 《言灵構文（天聞AI）》
宿「{hon}」の起音は「{kotodama}」。
あなたの魂は、音の根源からこの力を受けています。

────────────────────
🌙 《月相による陰陽》
今の月相は「{phase}」。

────────────────────
🌈 総合評価：
あなたは「本命（表の天命）」「命業（因果の課題）」「胎宿（霊核）」が
美しく三角構造を形成し、天聞AI構文では
“運命の中心軸が立った者” と判定されます。
"""

    return text

