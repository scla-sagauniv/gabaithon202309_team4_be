import logging
import psycopg2
import json
import os
from dotenv import load_dotenv
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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

    id = req.params.get('id')

    if id:
        cursor.execute("DELETE FROM users WHERE id = %s;", id)
        print("delete complete")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        # コンソールに出力
        for row in rows:
            print("Data row = (%s, %s, %s, %s)" %
                  (str(row[0]), str(row[1]), str(row[2]), str(row[3])))
        return func.HttpResponse("user delete successfully")
    else:
        return func.HttpResponse(
            "user delete successfully",
            status_code=200
        )
