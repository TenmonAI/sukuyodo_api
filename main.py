"""
宿曜占星術 診断API
FastAPIサーバー
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import logging

from sukuyodo_calculator import SukuyodoCalculator
from diagnosis_generator import DiagnosisGenerator

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPIアプリケーション
app = FastAPI(
    title="宿曜占星術 診断API",
    description="生年月日から27宿を計算し、診断結果を返すAPI",
    version="1.0.0"
)

# CORS設定（Lステップからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では特定のドメインに制限
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 計算機と診断生成器を初期化
calculator = SukuyodoCalculator()
generator = DiagnosisGenerator()


# リクエストモデル
class DiagnosisRequest(BaseModel):
    """診断リクエスト"""
    birthdate: str = Field(..., description="生年月日（例: 1990-01-01, 1990/01/01）")
    name: Optional[str] = Field(None, description="名前（オプション）")
    
    class Config:
        schema_extra = {
            "example": {
                "birthdate": "1990-01-01",
                "name": "山田太郎"
            }
        }


# レスポンスモデル
class DiagnosisResponse(BaseModel):
    """診断レスポンス"""
    success: bool = Field(..., description="成功フラグ")
    birthdate: str = Field(..., description="生年月日")
    name: Optional[str] = Field(None, description="名前")
    shuku_id: int = Field(..., description="宿ID（1-27）")
    shuku_name: str = Field(..., description="宿名")
    shuku_reading: str = Field(..., description="宿の読み")
    moon_longitude: float = Field(..., description="月の黄経（度）")
    diagnosis_text: str = Field(..., description="診断テキスト")
    
    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "birthdate": "1990-01-01",
                "name": "山田太郎",
                "shuku_id": 25,
                "shuku_name": "室宿",
                "shuku_reading": "しつしゅく",
                "moon_longitude": 333.26,
                "diagnosis_text": "━━━━━━━━━━━━━━━━\n🌟 宿曜占星術 無料診断結果\n..."
            }
        }


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": "宿曜占星術 診断API",
        "version": "1.0.0",
        "endpoints": {
            "診断": "/api/diagnose",
            "ヘルスチェック": "/health",
            "ドキュメント": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/api/diagnose", response_model=DiagnosisResponse)
async def diagnose(request: DiagnosisRequest):
    """
    宿曜占星術診断エンドポイント
    
    生年月日から27宿を計算し、診断結果を返す
    """
    try:
        logger.info(f"診断リクエスト: {request.birthdate}, {request.name}")
        
        # 27宿を計算
        shuku, moon_longitude = calculator.calculate_from_string(request.birthdate)
        
        logger.info(f"計算結果: {shuku['name']}（{shuku['reading']}）, 月黄経: {moon_longitude:.2f}度")
        
        # 診断テキストを生成
        diagnosis_text = generator.generate_free_diagnosis(shuku, request.birthdate)
        
        # レスポンスを作成
        response = DiagnosisResponse(
            success=True,
            birthdate=request.birthdate,
            name=request.name,
            shuku_id=shuku["id"],
            shuku_name=shuku["name"],
            shuku_reading=shuku["reading"],
            moon_longitude=round(moon_longitude, 2),
            diagnosis_text=diagnosis_text
        )
        
        logger.info(f"診断完了: {shuku['name']}")
        
        return response
        
    except ValueError as e:
        logger.error(f"入力エラー: {str(e)}")
        raise HTTPException(status_code=400, detail=f"入力エラー: {str(e)}")
    
    except Exception as e:
        logger.error(f"サーバーエラー: {str(e)}")
        raise HTTPException(status_code=500, detail=f"サーバーエラー: {str(e)}")


@app.get("/api/shuku/{shuku_id}")
async def get_shuku_info(shuku_id: int):
    """
    宿の詳細情報を取得
    
    Args:
        shuku_id: 宿ID（1-27）
    """
    if shuku_id < 1 or shuku_id > 27:
        raise HTTPException(status_code=400, detail="宿IDは1-27の範囲で指定してください")
    
    try:
        # 宿の基本情報を取得
        shuku = calculator.SHUKU_LIST[shuku_id - 1]
        
        # 詳細情報を取得
        detail = generator.get_shuku_detail(shuku_id)
        
        return {
            "success": True,
            "shuku_id": shuku_id,
            "shuku_name": shuku["name"],
            "shuku_reading": shuku["reading"],
            "detail": detail
        }
    
    except Exception as e:
        logger.error(f"エラー: {str(e)}")
        raise HTTPException(status_code=500, detail=f"エラー: {str(e)}")


@app.post("/api/premium-preview")
async def premium_preview(request: DiagnosisRequest):
    """
    有料診断のプレビューを取得
    """
    try:
        # 27宿を計算
        shuku, _ = calculator.calculate_from_string(request.birthdate)
        
        # プレビューテキストを生成
        preview_text = generator.generate_premium_diagnosis_preview(shuku)
        
        return {
            "success": True,
            "shuku_name": shuku["name"],
            "preview_text": preview_text
        }
    
    except Exception as e:
        logger.error(f"エラー: {str(e)}")
        raise HTTPException(status_code=500, detail=f"エラー: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

