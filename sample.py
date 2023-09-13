import psycopg2
import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# 接続情報の構成と接続
host = os.environ['SERVER_NAME']
dbname = "postgres"
user = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()

# データの読み込み
cursor.execute("SELECT * FROM inventory;")
rows = cursor.fetchall()
# コンソールに出力
for row in rows:
    print("Data row = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))

# データの挿入
cursor.execute(
    "INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute(
    "INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute(
    "INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")

# データの削除
cursor.execute("DELETE FROM inventory WHERE name = %s;", ("orange",))
print("Deleted 1 row of data")

# 保存・終了
conn.commit()
cursor.close()
conn.close()
