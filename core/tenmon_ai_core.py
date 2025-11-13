# core/tenmon_ai_core.py
# -----------------------------------------------------
# 天聞AI核心ロジック（霊核・金木・言灵 エンジン）
# -----------------------------------------------------

KANAGI_MODES = ["左旋内集", "左旋外発", "右旋内集", "右旋外発"]

def kanagi_mode_from_shuku(shuku_id: int) -> str:
    return KANAGI_MODES[shuku_id % 4]

GOTAI = {
    "ア": "天の水火の根源・開闢の息",
    "イ": "正中の火・一点凝縮",
    "ウ": "下降水火・地の生成",
    "エ": "外発・放射の強火",
    "オ": "統合・母胎の円環"
}

def kotodama_interpret(shuku_name: str) -> str:
    first = shuku_name[0]
    return GOTAI.get(first, "霊的響き：解析可能")

def generate_tenmon_core(hon, mei, tai):
    return {
        "core": f"あなたの霊核は「{hon} → {mei} → {tai}」の三位構文。",
        "karma": f"命業宿「{mei}」が因果の流れを示す。",
        "destiny": f"本命宿「{hon}」が外へ向かう天命方向を示す。"
    }

