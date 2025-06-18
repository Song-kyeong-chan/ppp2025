import sqlite3
import pandas as pd

# 🔧 사용할 DB 파일 지정 (경로 맞춰서 수정 가능)
db_path = "yogiyo_separated.db" # yogiyo.db

# 🔌 DB 연결
conn = sqlite3.connect(db_path)

# 1. 테이블 목록 출력
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("테이블 목록:")
print(tables)

# 2. 각 테이블의 상위 5행 미리보기 (존재하는 경우만)
for table_name in tables["name"]:
    try:
        print(f"\n{table_name} 미리보기:")
        preview = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5;", conn)
        print(preview)
    except Exception as e:
        print(f"  {table_name} 조회 실패: {e}")
