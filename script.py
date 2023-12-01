from typing import Any
from lib.database_utils import connect_to_database, execute_sql, read_query_from_file
from lib.custom_warnings import GeneralWarning
import warnings

def main() -> int:
    """
    メイン関数。
    データベースに接続し、指定されたSQLクエリを実行し、結果を処理する。

    戻り値:
        int: 処理の結果。成功時は0、警告時は4、エラー時は8を返す。
    """
    try:
        cnxn = connect_to_database(
            server='YOUR_SERVER',
            database='YOUR_DATABASE',
            username='YOUR_USERNAME', 
            password='YOUR_PASSWORD'
        )
        query = read_query_from_file('sql/sample.sql')
        results = execute_sql(cnxn, query)

        if some_condition:  # ここに具体的な条件を設定
            warnings.warn("General warning message.", GeneralWarning)

        cnxn.close()
        print(results)
        return 0
    except GeneralWarning as gw:
        print(f"A general warning occurred: {gw}")
        return 4
    except Exception as e:
        print(f'An error occurred: {e}')
        return 8

if __name__ == "__main__":
    exit(main())
