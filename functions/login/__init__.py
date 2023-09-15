import jwt
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
            email = req_body.get('email')
            inputpassword = req_body.get('password')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        cursor.execute("SELECT * FROM users WHERE email = %s ;", (email,))
        row = cursor.fetchall()
        username = row[0][1]
        password = row[0][3]

        # 保存・終了
        conn.commit()
        cursor.close()
        conn.close()
        if password == inputpassword:
            payload = {
                "username": username,
                "email": email,
                "password": password
            }
            key = "secret"
            token = jwt.encode(payload, key, algorithm="HS256")
            return func.HttpResponse(
                json.dumps(token),
                status_code=200
            )
        else:
            return func.HttpResponse(
                "The password is in correct",
                status_code=400
            )
