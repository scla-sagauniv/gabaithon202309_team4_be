import psycopg2
import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# 接続情報の構成と接続
host = os.environ['SERVER_NAME']
dbname = "contents"
user = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS opinions;")
print("Finished dropping table (if existed)")
# テーブル作成
cursor.execute(
    "CREATE TABLE opinions (id serial PRIMARY KEY, genre VARCHAR(50), content VARCHAR(50), status INTEGER);")
print("Finished creating contents table")

cursor.execute(
    "INSERT INTO opinions (genre, content, status) VALUES (%s, %s, %s);", ("生徒会", "ヘアゴムの色を自由にしてほしい！", 0))

cursor.execute("SELECT * FROM opinions;")
rows = cursor.fetchall()

for row in rows:
    print("Data row = (%s, %s, %s, %s)" %
          (str(row[0]), str(row[1]), str(row[2]), str(row[3])))
# 保存・終了
conn.commit()
cursor.close()
conn.close()


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

cursor.execute("DROP TABLE IF EXISTS users;")
print("Finished dropping table (if existed)")

# テーブル作成
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), status INTEGER);")
print("Finished creating users table")

cursor.execute(
    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s);", ("admin", "admin@gabaithon.com", "admin"))

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

for row in rows:
    print("Data row = (%s, %s, %s, %s)" %
          (str(row[0]), str(row[1]), str(row[2]), str(row[3])))

# 保存・終了
conn.commit()
cursor.close()
conn.close()
