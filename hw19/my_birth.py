import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
def download_weather(station_id, year1, year2, filename):
    URL = f'https://api.taegon.kr/stations/{station_id}/?sy={year1}&ey={year2}&format=csv'
    with open(filename, 'w', encoding='utf-8-sig') as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = './hw19/jeonju_weather_1980_2024.csv'
    if not os.path.exists(filename):
        download_weather(146, 1980, 2024, filename)

    df = pd.read_csv(filename)
    df.columns = df.columns.str.strip()

    # 내 생일 날(9월 27일)
    birthday = df[(df['month'] == 9) & (df['day'] == 27)]
    birthday_temp = birthday[['year', 'tavg', 'tmax', 'tmin']]

    fig, ax = plt.subplots(figsize=(10, 5))
    # 평균 온도
    ax.plot(birthday_temp['year'], birthday_temp['tavg'], label='평균온도')
    # 최고/최저 온도
    ax.plot(birthday_temp['year'], birthday_temp['tmax'], label='최고온도')
    ax.plot(birthday_temp['year'], birthday_temp['tmin'], label='최저온도')
    
    ax.set_title("9월 27일 생일날의 온도 변화 (1980~2024)")
    ax.set_xlabel("연도")
    ax.set_ylabel("온도 (°C)")
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.savefig('./hw19/birthday_temp.png')
    plt.show()

if __name__ == "__main__":
    main()
