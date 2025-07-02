import sqlite3 
import os

# DB 경로 설정
db_path = os.path.join('database', 'crime_data.db')
os.makedirs('database', exist_ok = True)

# 연결 시도
try:
    conn = sqlite3.connect(db_path)
    print("SQLite DB 연결 성공")
    conn.close()
except Exception as e:
    print(f"SQLtie 연결 오류: {e}")