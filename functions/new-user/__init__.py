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

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            new_email = req_body.get('email')
            new_username = req_body.get('username')
            new_password = req_body.get('password')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        # 新しいデータをデータベースに挿入
        cursor.execute(
            "INSERT INTO users (email, username, password, status) VALUES (%s, %s, %s, %s);",
            (new_email, new_username, new_password, 0)
        )

        # 保存・終了
        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse(
            "signin successfully",
            status_code=200
        )
