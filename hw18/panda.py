import pandas as pd
import requests
import os
from sfarm_hw import submit_to_api
# 날씨데이터 불러오기
def download_weather(station_id, year, filename):
    URL = f'https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv'
    with open(filename, 'w', encoding='utf-8-sig') as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)
        

def main():
    weather_2012 = './hw17/jeonju_weather_2012.csv'
    if not os.path.exists(weather_2012):
        download_weather(146, 2012,weather_2012)
    weather_2024 = './hw17/jeonju_weather_2024.csv'
    if not os.path.exists(weather_2024):
        download_weather(146, 2024,weather_2024)
    weather_2020 = './hw17/jeonju_weather_2020.csv'
    if not os.path.exists(weather_2020):
        download_weather(146, 2020,weather_2020)
    weather_2019 = './hw17/jeonju_weather_2019.csv'
    if not os.path.exists(weather_2019):
        download_weather(146, 2019,weather_2019)
    weather_2019_suwon = './hw17/jeonju_weather_2019_suwon.csv'
    if not os.path.exists(weather_2019_suwon):
        download_weather(119, 2019,weather_2019_suwon)
    df_2012 = pd.read_csv(weather_2012, skipinitialspace=True)
    df_2024 = pd.read_csv(weather_2024, skipinitialspace=True)
    df_2020 = pd.read_csv(weather_2020, skipinitialspace=True)
    df_2019 = pd.read_csv(weather_2019, skipinitialspace=True)
    df_2019_suwon = pd.read_csv(weather_2019_suwon, skipinitialspace=True)
    # 과제 1) 전주시(146)의 2012년 연 강수량은?
    print(round(sum(df_2012['rainfall']),1))
    # 과제 2) 전주시(146)의 2024년 최대기온은? max of tmax
    print(round(max(df_2024['tmax']),1))
    # 과제 3) 전주시(146)의 2020년 최대 일교차(tmax-tmin)는?
    print(round(max(df_2020['tmax']-df_2020['tmin']),1))
    # 과제 4) 수원시(119)와 전주시(146)의 2019년 총강수량 차이는(절댓값)?
    print(round(abs(sum(df_2019['rainfall'])-sum(df_2019_suwon['rainfall'])),1))
    name = "송경찬"
    affiliation = "스마트팜학과"
    student_id = "202217713"

    answer1 = round(sum(df_2012['rainfall']),1)
    answer2 = round(max(df_2024['tmax']),1)
    answer3 = round(max(df_2020['tmax']-df_2020['tmin']),1)
    answer4 = round(abs(sum(df_2019['rainfall'])-sum(df_2019_suwon['rainfall'])),1)

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)
if __name__ == "__main__":
    main()
