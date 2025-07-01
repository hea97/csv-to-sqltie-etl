import pandas as pd
import os

csv_file_path = os.path.join('data', '경찰청_범죄 발생 장소별 통계_20231231.csv')

try:
    df = pd.read_csv(csv_file_path, encoding='cp949')  
    print("CSV 파일 로드 성공\n")
    print(df.head())
    df.info()
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {csv_file_path}")
except Exception as e:
    print(f"CSV 파일 로드 중 오류 발생: {e}")