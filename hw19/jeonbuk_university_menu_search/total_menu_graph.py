import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 한글 폰트 설정 (Windows 환경 기준, macOS는 AppleGothic 사용 가능)
plt.rcParams['font.family'] = 'NanumGothic' 
plt.rcParams['axes.unicode_minus'] = False

# DB 연결
conn = sqlite3.connect("yogiyo_separated.db")  # 파일 경로에 따라 수정 필요

# 데이터 불러오기
stores_food = pd.read_sql_query("SELECT * FROM stores_food", conn)
stores_cafe = pd.read_sql_query("SELECT * FROM stores_cafe", conn)
menus_food = pd.read_sql_query("SELECT * FROM menus_food", conn)
menus_cafe = pd.read_sql_query("SELECT * FROM menus_cafe", conn)

# 수치 계산
store_labels = ['음식점', '카페', '총 가게 수']
store_values = [len(stores_food), len(stores_cafe), len(stores_food) + len(stores_cafe)]

menu_labels = ['음식점 메뉴', '카페 메뉴', '총 메뉴 수']
menu_values = [len(menus_food), len(menus_cafe), len(menus_food) + len(menus_cafe)]

# 시각화
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# 1. 가게 수 그래프
axs[0].bar(store_labels, store_values, color=['skyblue', 'lightgreen', 'lightgray'])
axs[0].set_title("가게 수 비교")
axs[0].set_ylabel("개수")

# 2. 메뉴 수 그래프
axs[1].bar(menu_labels, menu_values, color=['orange', 'salmon', 'gray'])
axs[1].set_title("메뉴 수 비교")
axs[1].set_ylabel("개수")

plt.tight_layout()

# 저장 및 표시
plt.savefig("yogiyo_summary_from_db.png")
plt.show()
