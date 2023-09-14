import logging
import psycopg2
import os
from dotenv import load_dotenv
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            genre = req_body.get('genre')
            content = req_body.get('content')
            status = 0

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        insert_query = "INSERT INTO opinions (genre, content, status) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (genre, content, status))
        print("finish")
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
