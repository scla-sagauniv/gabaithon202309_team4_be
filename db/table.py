import psycopg2
import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# 接続情報の構成と接続
host = os.environ['SERVER_NAME']
dbname = ""
user = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

# テーブル作成
cursor.execute(
    "CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")

# 保存・終了
conn.commit()
cursor.close()
conn.close()
