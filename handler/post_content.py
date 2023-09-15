#pythonでPostgreSQLへ接続するためのライブラリ
import psycopg2
#OSに依存しているさまざまな機能を利用するためのモジュール
import os
#キー・バリューのペアで構成される環境変数を読み込むためのPythonライブラリ
from dotenv import load_dotenv



# 環境変数(設定したOS内で、共通して使える変数)読み込み
load_dotenv()

# 接続情報の構成と接続
# 環境変数からデータベース接続情報を取得
host = os.environ['SERVER_NAME']        #ホスト
dbname = "contents"                     #データベース名
user = os.environ['ADMIN_USERNAME']     #ユーザー名
password = os.environ['ADMIN_PASSWORD'] #パスワード
sslmode = "require"                     #セキュリティ設定

# 接続情報を作成
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)

# データベースに接続
conn = psycopg2.connect(conn_string)
print("Connection established")

# カーソルオブジェクトを作成
cursor = conn.cursor()

######################## 以下にコード作成 #####################
# ここからフロントからの情報をDBへ挿入する処理
# サンプルデータ（フロントエンドから送られてくる）

#データの取得と表示
cursor.execute("SELECT * FROM opinions;")
rows = cursor.fetchall()
for row in rows:
    print("Data row = (%s, %s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2]), str(row[3])))



# ここでフロントエンドから受け取ったデータを変数に格納（仮のデータ）
genre = "a"
content = "b"
status = 0


# SQLクエリ（データを挿入）
insert_query = "INSERT INTO opinions (genre, content,status) VALUES (%s, %s, %s);"
cursor.execute(insert_query, (genre, content, status))


## 保存・終了
# トランザクションのコミット（変更を保存）
conn.commit()

# カーソルを閉じる
cursor.close()

# 接続を閉じる
conn.close()
