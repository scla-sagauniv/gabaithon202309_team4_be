import psycopg2
import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# 接続情報の構成と接続
host = os.environ['SERVER_NAME']
dbname = "users"
user = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

# 以下にコード作成
#e-mail,username,passwordをデータベースに追加する
# ユーザーからの新しい入力
new_email = "new.email@example.com"
new_username = "new_username"
new_password = "new_password"

# 新しいデータをデータベースに挿入
cursor.execute(
    "INSERT INTO users (email, username, password) VALUES (%s, %s, %s);", 
    (new_email, new_username, new_password)
)


# 保存・終了
conn.commit()
cursor.close()
conn.close()
