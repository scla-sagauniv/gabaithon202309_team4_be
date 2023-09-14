import psycopg2
import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# 接続情報の構成と接続
# 環境変数からデータベース接続情報を取得
host = os.environ['SERVER_NAME']
dbname = "contents"
user = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']
sslmode = "require"

# 接続文字列を作成
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)

# データベースに接続
conn = psycopg2.connect(conn_string)
print("Connection established")

# カーソルオブジェクトを作成
cursor = conn.cursor()

# 以下にコード作成



## 保存・終了
# トランザクションのコミット（変更を保存）
conn.commit()

# カーソルを閉じる
cursor.close()

# 接続を閉じる
conn.close()
