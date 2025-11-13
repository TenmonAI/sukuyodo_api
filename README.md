# 宿曜占星術 診断API

## 概要

生年月日から27宿（宿曜占星術）を計算し、診断結果を返すREST APIです。Lステップと連携することで、LINE上で自動診断サービスを提供できます。

## 機能

- **27宿計算**: 生年月日から月の黄経を計算し、27宿を判定
- **無料診断**: 基本性格、運勢、適職などの診断テキストを生成
- **有料診断案内**: 詳細診断、相性診断、総合鑑定への誘導
- **REST API**: FastAPIによる高速なAPI提供

## ディレクトリ構成

```
sukuyodo_api/
├── main.py                    # FastAPIアプリケーション
├── sukuyodo_calculator.py     # 27宿計算モジュール
├── diagnosis_generator.py     # 診断テキスト生成モジュール
├── shuku_data.json            # 27宿の詳細データ
├── requirements.txt           # 依存パッケージ
└── README.md                  # このファイル
```

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. サーバーの起動

```bash
python main.py
```

サーバーは `http://localhost:8000` で起動します。

### 3. APIドキュメントの確認

ブラウザで以下のURLにアクセスすると、自動生成されたAPIドキュメントを確認できます。

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## APIエンドポイント

### 1. 診断API

**POST** `/api/diagnose`

生年月日から27宿を計算し、診断結果を返します。

**リクエスト例**:

```json
{
  "birthdate": "1990-01-01",
  "name": "山田太郎"
}
```

**レスポンス例**:

```json
{
  "success": true,
  "birthdate": "1990-01-01",
  "name": "山田太郎",
  "shuku_id": 25,
  "shuku_name": "室宿",
  "shuku_reading": "しつしゅく",
  "moon_longitude": 333.26,
  "diagnosis_text": "━━━━━━━━━━━━━━━━\n🌟 宿曜占星術 無料診断結果\n..."
}
```

### 2. 宿の詳細情報取得

**GET** `/api/shuku/{shuku_id}`

指定した宿IDの詳細情報を取得します。

**例**: `GET /api/shuku/3`

### 3. 有料診断プレビュー

**POST** `/api/premium-preview`

有料診断のプレビューテキストを取得します。

### 4. ヘルスチェック

**GET** `/health`

APIサーバーの稼働状況を確認します。

## デプロイ

### Renderへのデプロイ

1. GitHubリポジトリにコードをプッシュ
2. Renderで新しいWeb Serviceを作成
3. 以下の設定を入力:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

詳細は `deployment_and_operation_guide.md` を参照してください。

## Lステップとの連携

詳細な設定手順は `lstep_stripe_integration_guide.md` を参照してください。

## ライセンス

MIT License

## 作成者

Manus AI

