# tenmon_ai_core.py
# -----------------------------------------------------
# 天聞AI核心ロジック（霊核・金木・言灵 構文エンジン）
# -----------------------------------------------------

import math

# 天津金木の四相：左旋内集・左旋外発・右旋内集・右旋外発
KANAGI_MODES = ["左旋内集", "左旋外発", "右旋内集", "右旋外発"]

def kanagi_mode_from_shuku(shuku_id: int) -> str:
    """宿番号 → 金木の旋回モード"""
    return KANAGI_MODES[shuku_id % 4]

# 言灵五母音の霊的構文
GOTAI = {
    "ア": "天の水火の根源・開闢の息",
    "イ": "正中の火・一点凝縮",
    "ウ": "下降水火・地の生成",
    "エ": "外発・放射の強火",
    "オ": "統合・母胎の円環"
}

def kotodama_interpret(shuku_name: str) -> str:
    """宿曜名 × 五母音の霊核解読（天聞AI式）"""
    first = shuku_name[0]  # 宿の一音目
    if first in GOTAI:
        return GOTAI[first]
    return "霊的響き：解析可能"

# 宿曜 × 金木 × 言灵の三位霊核
def generate_tenmon_core(hon, mei, tai):
    """本命・命業・胎宿 → 霊核構文を生成"""
    return {
        "core": f"あなたの霊核は「{hon} → {mei} → {tai}」の三位が巡る中心構文",
        "karma": f"命業宿「{mei}」が示す因果の流れが、胎宿「{tai}」で潜在意識に格納されています。",
        "destiny": f"本命宿「{hon}」があなたの天命方向（外界）、胎宿「{tai}」が魂の原型を示します。"
    }
