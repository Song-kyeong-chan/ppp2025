import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 한글 폰트 설정 
plt.rcParams['font.family'] = 'NanumGothic'  
plt.rcParams['axes.unicode_minus'] = False

# 1. DB 연결
conn = sqlite3.connect("yogiyo_separated.db")  

# 2. 데이터 로드
stores_food = pd.read_sql_query("SELECT * FROM stores_food", conn) 
stores_cafe = pd.read_sql_query("SELECT * FROM stores_cafe", conn)

# 3. 카테고리 추가
stores_food['카테고리'] = '음식점'
stores_cafe['카테고리'] = '카페'

# 4. 두 데이터프레임 결합
combined_stores = pd.concat([stores_food, stores_cafe])

# 5. 주소에서 '동' 추출 및 분류
combined_stores['동'] = combined_stores['주소'].apply(
    lambda x: '신정문/사대부고(금암동)' if '금암동' in x else ('구정문(덕진동1가)' if '덕진동1가' in x else '기타')
) 

# 6. 그룹별 개수 집계
grouped = combined_stores.groupby(['동', '카테고리']).size().unstack(fill_value=0)

# 7. 시각화
grouped.plot(kind='bar', figsize=(8, 5), color=['skyblue', 'salmon'])
plt.title('주소별 가게 수 (음식점 vs 카페)')
plt.ylabel('개수')
plt.xticks(rotation=0) # 
plt.tight_layout()

# 8. 저장 및 출력
plt.savefig("category_by_address.png")
plt.show()
