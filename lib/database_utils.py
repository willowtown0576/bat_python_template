import pyodbc
from typing import List, Any

def connect_to_database(
    server: str, 
    database: str, 
    username: str, 
    password: str
) -> pyodbc.Connection:
    """
    SQL Serverに接続するための関数。

    パラメータ:
        server (str): サーバーのアドレス。
        database (str): データベース名。
        username (str): ユーザー名。
        password (str): パスワード。

    戻り値:
        pyodbc.Connection: データベースへの接続オブジェクト。
    """
    connection_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
    connection_str += ';UID=' + username + ';PWD=' + password
    return pyodbc.connect(connection_str)

def execute_sql(cnxn: pyodbc.Connection, query: str, params: Optional[List[Any]] = None) -> Optional[int]:
    """
    与えられたSQLクエリを実行する関数。

    パラメータ:
        cnxn (pyodbc.Connection): データベース接続オブジェクト。
        query (str): 実行するSQLクエリ。
        params (Optional[List[Any]]): SQLクエリに渡すパラメータのリスト。

    戻り値:
        Optional[int]: SELECT文の場合はクエリ結果のリスト、それ以外の場合は影響を受けた行数。
    """
    cursor: pyodbc.Cursor = cnxn.cursor()
    cursor.execute(query, params or [])

    if cursor.description:
        return [row for row in cursor]
    else:
        rowcount = cursor.rowcount
        cursor.commit()
        return rowcount

    cursor.close()

def read_query_from_file(file_path: str) -> str:
    """
    指定されたパスからSQLクエリを読み込む関数。

    パラメータ:
        file_path (str): SQLファイルのパス。

    戻り値:
        str: ファイルから読み込まれたSQLクエリ。
    """
    with open(file_path, 'r') as file:
        return file.read()
