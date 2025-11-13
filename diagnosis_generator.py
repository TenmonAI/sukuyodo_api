"""
宿曜占星術 診断テキスト生成モジュール
27宿の情報から診断テキストを生成する
"""

import json
from pathlib import Path
from typing import Dict


class DiagnosisGenerator:
    """診断テキスト生成クラス"""
    
    def __init__(self, data_file: str = "shuku_data.json"):
        """
        初期化
        
        Args:
            data_file: 27宿データのJSONファイルパス
        """
        # データファイルを読み込む
        data_path = Path(__file__).parent / data_file
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.shuku_data = data["27宿詳細データ"]
    
    def get_shuku_detail(self, shuku_id: int) -> Dict:
        """
        宿IDから詳細データを取得
        
        Args:
            shuku_id: 宿ID (1-27)
            
        Returns:
            宿の詳細データ
        """
        # 宿IDは1-27だが、データは1-29まである（一部重複）
        # 正しい27宿に対応させる
        shuku_id_map = {
            1: 27,  # 婁宿
            2: 28,  # 胃宿
            3: 1,   # 昴宿
            4: 2,   # 畢宿
            5: 3,   # 觜宿
            6: 4,   # 参宿
            7: 5,   # 井宿
            8: 6,   # 鬼宿
            9: 7,   # 柳宿
            10: 8,  # 星宿
            11: 9,  # 張宿
            12: 10, # 翼宿
            13: 11, # 軫宿
            14: 12, # 角宿
            15: 13, # 亢宿
            16: 14, # 氐宿
            17: 15, # 房宿
            18: 16, # 心宿
            19: 17, # 尾宿
            20: 18, # 箕宿
            21: 19, # 斗宿
            22: 20, # 牛宿
            23: 21, # 女宿
            24: 22, # 虚宿
            25: 23, # 危宿
            26: 24, # 室宿
            27: 25, # 壁宿
        }
        
        # 注: 奎宿(26)と珍宿(29)は特殊なのでマッピングから除外
        if shuku_id in shuku_id_map:
            data_id = str(shuku_id_map[shuku_id])
        else:
            data_id = str(shuku_id)
        
        return self.shuku_data.get(data_id, {})
    
    def generate_free_diagnosis(self, shuku_info: Dict, birthdate: str) -> str:
        """
        無料診断テキストを生成
        
        Args:
            shuku_info: 宿の基本情報（計算結果）
            birthdate: 生年月日
            
        Returns:
            診断テキスト
        """
        shuku_id = shuku_info["id"]
        shuku_name = shuku_info["name"]
        shuku_reading = shuku_info["reading"]
        
        # 詳細データを取得
        detail = self.get_shuku_detail(shuku_id)
        
        # 診断テキストを生成
        diagnosis = f"""━━━━━━━━━━━━━━━━
🌟 宿曜占星術 無料診断結果
━━━━━━━━━━━━━━━━

【生年月日】{birthdate}

【あなたの本命宿】
{shuku_name}（{shuku_reading}）

━━━━━━━━━━━━━━━━
✨ 基本性格
━━━━━━━━━━━━━━━━

{detail.get('性格', '情報なし')}

━━━━━━━━━━━━━━━━
🎯 運勢の傾向
━━━━━━━━━━━━━━━━

{detail.get('運勢', '情報なし')}

━━━━━━━━━━━━━━━━
💼 適職・才能
━━━━━━━━━━━━━━━━

{detail.get('適職', detail.get('特徴', '多方面で活躍できる才能があります'))}

━━━━━━━━━━━━━━━━
🌠 宿の特徴
━━━━━━━━━━━━━━━━

分類: {detail.get('分類', '一般')}
星形: {detail.get('星形', '情報なし')}

━━━━━━━━━━━━━━━━

✨ もっと詳しく知りたい方へ ✨

【有料診断メニュー】

🔮 詳細診断（5,000円）
・今年の運勢
・月別の吉凶
・恋愛運・仕事運・金運
・開運アドバイス

💕 相性診断（3,000円）
・気になる相手との相性
・12宮の関係性
・相性改善アドバイス

🌟 総合鑑定（10,000円）
・詳細診断 + 相性診断
・個別メッセージ付き
・今後1年間の運勢カレンダー

━━━━━━━━━━━━━━━━

👇 ご予約はこちらから
"""
        
        return diagnosis
    
    def generate_premium_diagnosis_preview(self, shuku_info: Dict) -> str:
        """
        有料診断のプレビューテキストを生成
        
        Args:
            shuku_info: 宿の基本情報
            
        Returns:
            プレビューテキスト
        """
        shuku_name = shuku_info["name"]
        
        preview = f"""━━━━━━━━━━━━━━━━
🌟 {shuku_name}の方へ
有料診断でわかること
━━━━━━━━━━━━━━━━

【詳細診断】5,000円

✅ 今年の総合運勢
✅ 月別の吉凶カレンダー
✅ 恋愛運・結婚運
✅ 仕事運・金運
✅ 健康運・人間関係運
✅ 開運アクション
✅ ラッキーカラー・方位

【相性診断】3,000円

✅ 気になる相手との相性度
✅ 12宮の関係性
✅ 相性の良い点・注意点
✅ 関係を深めるアドバイス
✅ 最適なアプローチ方法

【総合鑑定】10,000円

✅ 上記すべて
✅ 個別メッセージ
✅ 1年間の運勢カレンダー
✅ 質問1つ無料回答

━━━━━━━━━━━━━━━━

💰 お支払い方法
クレジットカード（Stripe決済）

📅 鑑定結果のお届け
ご入金確認後、3営業日以内にLINEでお届けします

━━━━━━━━━━━━━━━━
"""
        
        return preview


# テスト用
if __name__ == "__main__":
    generator = DiagnosisGenerator()
    
    # テスト
    test_shuku = {
        "id": 3,
        "name": "昴宿",
        "reading": "ぼうしゅく"
    }
    
    diagnosis = generator.generate_free_diagnosis(test_shuku, "1995-07-20")
    print(diagnosis)
    
    print("\n" + "="*60 + "\n")
    
    preview = generator.generate_premium_diagnosis_preview(test_shuku)
    print(preview)

