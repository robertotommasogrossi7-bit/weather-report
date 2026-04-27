from db.connection import get_connection

def run_sql_file(filepath: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    with open(filepath, "r") as f:
        sql = f.read()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def run_sql_files(filepaths: list[str]) -> None:
    for path in filepaths:
        run_sql_file(path)