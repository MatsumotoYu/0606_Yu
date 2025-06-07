from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import platform
from pathlib import Path

print("platform:", platform.uname())

# .envファイルのパス設定と読み込み
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / ".env"
load_dotenv(dotenv_path=env_path)

# .envファイルを読み込む
#load_dotenv()
#print("DB_PORT from .env:", os.getenv("DB_PORT"))

print("✅ .env 読み込み完了")
print("DB_PORT:", os.getenv("DB_PORT"))
    
# パス調整
main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)
print("cwd:", os.getcwd())

# 環境変数からDB情報を取得
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
SSL_CA_PATH = os.getenv("SSL_CA_PATH")

if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("Missing one or more required environment variables.")

# ✅ 数値で使う前に変換
DB_PORT = int(DB_PORT)

# 接続URLを構築（MySQL + pymysql）
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"?ssl_ca={SSL_CA_PATH}"
)

# エンジン定義（これがないと「engineが未定義」のエラーになります）
engine = create_engine(DATABASE_URL)

print("DATABASE_URL:", DATABASE_URL)  # 確認用

# DB接続テスト
with engine.connect() as conn:
    print("✅ DBに接続成功しました！")