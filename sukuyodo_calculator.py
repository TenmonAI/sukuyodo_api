"""
宿曜占星術 27宿計算モジュール
生年月日から本命宿を計算する
"""

import ephem
from datetime import datetime
from typing import Tuple


class SukuyodoCalculator:
    """宿曜道27宿計算クラス"""
    
    # 27宿の定義（黄経0度から順番）
    SHUKU_LIST = [
        {"id": 1, "name": "婁宿", "reading": "ろうしゅく", "range": (0.0, 13.33)},
        {"id": 2, "name": "胃宿", "reading": "いしゅく", "range": (13.33, 26.67)},
        {"id": 3, "name": "昴宿", "reading": "ぼうしゅく", "range": (26.67, 40.0)},
        {"id": 4, "name": "畢宿", "reading": "ひっしゅく", "range": (40.0, 53.33)},
        {"id": 5, "name": "觜宿", "reading": "ししゅく", "range": (53.33, 66.67)},
        {"id": 6, "name": "参宿", "reading": "しんしゅく", "range": (66.67, 80.0)},
        {"id": 7, "name": "井宿", "reading": "せいしゅく", "range": (80.0, 93.33)},
        {"id": 8, "name": "鬼宿", "reading": "きしゅく", "range": (93.33, 106.67)},
        {"id": 9, "name": "柳宿", "reading": "りゅうしゅく", "range": (106.67, 120.0)},
        {"id": 10, "name": "星宿", "reading": "せいしゅく", "range": (120.0, 133.33)},
        {"id": 11, "name": "張宿", "reading": "ちょうしゅく", "range": (133.33, 146.67)},
        {"id": 12, "name": "翼宿", "reading": "よくしゅく", "range": (146.67, 160.0)},
        {"id": 13, "name": "軫宿", "reading": "しんしゅく", "range": (160.0, 173.33)},
        {"id": 14, "name": "角宿", "reading": "かくしゅく", "range": (173.33, 186.67)},
        {"id": 15, "name": "亢宿", "reading": "こうしゅく", "range": (186.67, 200.0)},
        {"id": 16, "name": "氐宿", "reading": "ていしゅく", "range": (200.0, 213.33)},
        {"id": 17, "name": "房宿", "reading": "ぼうしゅく", "range": (213.33, 226.67)},
        {"id": 18, "name": "心宿", "reading": "しんしゅく", "range": (226.67, 240.0)},
        {"id": 19, "name": "尾宿", "reading": "びしゅく", "range": (240.0, 253.33)},
        {"id": 20, "name": "箕宿", "reading": "きしゅく", "range": (253.33, 266.67)},
        {"id": 21, "name": "斗宿", "reading": "としゅく", "range": (266.67, 280.0)},
        {"id": 22, "name": "女宿", "reading": "じょしゅく", "range": (280.0, 293.33)},
        {"id": 23, "name": "虚宿", "reading": "きょしゅく", "range": (293.33, 306.67)},
        {"id": 24, "name": "危宿", "reading": "きしゅく", "range": (306.67, 320.0)},
        {"id": 25, "name": "室宿", "reading": "しつしゅく", "range": (320.0, 333.33)},
        {"id": 26, "name": "壁宿", "reading": "へきしゅく", "range": (333.33, 346.67)},
        {"id": 27, "name": "奎宿", "reading": "けいしゅく", "range": (346.67, 360.0)},
    ]
    
    def __init__(self):
        """初期化"""
        pass
    
    def calculate_moon_longitude(self, birthdate: datetime) -> float:
        """
        指定された日時の月の黄経を計算
        
        Args:
            birthdate: 生年月日（datetime）
            
        Returns:
            月の黄経（度）0-360
        """
        # PyEphemで月の位置を計算
        moon = ephem.Moon()
        moon.compute(birthdate)
        
        # 月の黄経（ラジアンから度に変換）
        moon_longitude = float(moon.hlon) * 180.0 / ephem.pi
        
        # 0-360の範囲に正規化
        moon_longitude = moon_longitude % 360.0
        
        return moon_longitude
    
    def get_shuku_from_longitude(self, longitude: float) -> dict:
        """
        月の黄経から27宿を判定
        
        Args:
            longitude: 月の黄経（度）
            
        Returns:
            宿の情報（辞書）
        """
        for shuku in self.SHUKU_LIST:
            min_lon, max_lon = shuku["range"]
            if min_lon <= longitude < max_lon:
                return shuku
        
        # 360度の場合は奎宿（最後の宿）
        return self.SHUKU_LIST[-1]
    
    def calculate_shuku(self, year: int, month: int, day: int) -> Tuple[dict, float]:
        """
        生年月日から本命宿を計算
        
        Args:
            year: 年
            month: 月
            day: 日
            
        Returns:
            (宿の情報, 月の黄経)のタプル
        """
        # 生年月日をdatetimeに変換（正午を基準）
        birthdate = datetime(year, month, day, 12, 0, 0)
        
        # 月の黄経を計算
        moon_longitude = self.calculate_moon_longitude(birthdate)
        
        # 27宿を判定
        shuku = self.get_shuku_from_longitude(moon_longitude)
        
        return shuku, moon_longitude
    
    def calculate_from_string(self, date_string: str) -> Tuple[dict, float]:
        """
        文字列形式の生年月日から本命宿を計算
        
        Args:
            date_string: 生年月日（例: "1990-01-01", "1990/01/01"）
            
        Returns:
            (宿の情報, 月の黄経)のタプル
        """
        # 区切り文字を統一
        date_string = date_string.replace("/", "-").replace("年", "-").replace("月", "-").replace("日", "")
        
        # パース
        try:
            date_parts = date_string.split("-")
            year = int(date_parts[0])
            month = int(date_parts[1])
            day = int(date_parts[2])
        except (ValueError, IndexError):
            raise ValueError(f"日付の形式が正しくありません: {date_string}")
        
        return self.calculate_shuku(year, month, day)


# テスト用
if __name__ == "__main__":
    calculator = SukuyodoCalculator()
    
    # テストケース
    test_dates = [
        "1990-01-01",
        "1985-05-15",
        "2000-12-25",
        "1995/07/20",
    ]
    
    print("=" * 60)
    print("宿曜占星術 27宿計算テスト")
    print("=" * 60)
    
    for date_str in test_dates:
        shuku, longitude = calculator.calculate_from_string(date_str)
        print(f"\n生年月日: {date_str}")
        print(f"月の黄経: {longitude:.2f}度")
        print(f"本命宿: {shuku['name']}（{shuku['reading']}）")
        print(f"宿番号: {shuku['id']}")

