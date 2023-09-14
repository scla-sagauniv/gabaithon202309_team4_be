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
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        # データの読み込み
        cursor.execute("SELECT * FROM opinions WHERE status = 0 ;")
        rows = cursor.fetchall()
        print("rows", rows)
        # コンソールに出力
        for row in rows:
            print("Data row = (%s, %s, %s, %s)" %
                  (str(row[0]), str(row[1]), str(row[2]), str(row[3])))
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
