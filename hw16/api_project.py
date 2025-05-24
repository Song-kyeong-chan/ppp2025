import requests
import os
from sfarm_hw import submit_to_api

'''
1) 전주시(146)의 2015년 연 강수량은?
2) 전주시(146)의 2022년 최대기온은? max of tavg
3) 전주시(146)의 2024년 최대 일교차(tmax-tmin)는?
4) 수원시(119)와 전주시(146)의 2024년 총강수량 차이는(절대값)? 

'''

# 날씨데이터 불러오기
def download_weather(station_id, year, filename):
    URL = f'https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv'
    with open(filename, 'w', encoding='utf-8-sig') as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

# 날씨 데이터 저장
def get_weather_data(filename, col_idx):
    datas = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        files = f.readlines()
        for file in files[1:]:
            line = file.strip().split(',')
            try:
                datas.append(float(line[col_idx]))
            except:
                continue
    return datas

def total_rainfall(rainfall_idx):
    return sum(rainfall_idx)

def max_of_tavg(tavg_idx):
    return max(tavg_idx)

def max_of_temp_diff(tmax_idx, tmin_idx):
    max_diff = tmax_idx[0] - tmin_idx[0]
    for i in range(len(tmax_idx)):
        t_diff = tmax_idx[i] - tmin_idx[i]
        if t_diff > max_diff:
            max_diff = t_diff
    
    return max_diff

def main():
    jeonju_weather_2015 = './jeonju_weather_2015.csv'
    jeonju_weather_2022 = './jeonju_weather_2022.csv'
    jeonju_weather_2024 = './jeonju_weather_2024.csv'
    suwon_weather_2024 = './suwon_weather_2024.csv'
    download_weather(146, 2015, jeonju_weather_2015)
    download_weather(146, 2022, jeonju_weather_2022)
    download_weather(146, 2024, jeonju_weather_2024)
    download_weather(119, 2024, suwon_weather_2024)

    # 1) 전주시(146)의 2015년 연 강수량은?
    rainfall_list_2015 =  get_weather_data(jeonju_weather_2015, 3)
    total_rainfall_2015 = round(total_rainfall(rainfall_list_2015),1)

    # 2) 전주시(146)의 2022년 최대기온은? max of tavg
    tavg_list_2022 = get_weather_data(jeonju_weather_2022,4)
    max_of_tavg_2022 = round(max_of_tavg(tavg_list_2022),1)

    # 3) 전주시(146)의 2024년 최대 일교차(tmax-tmin)는?
    tmax_list_2024 = get_weather_data(jeonju_weather_2024,4)
    tmin_list_2024 = get_weather_data(jeonju_weather_2024,3)
    max_temp_diff_2024 = round(max_of_temp_diff(tmax_list_2024, tmin_list_2024),1)

    # 4) 수원시(119)와 전주시(146)의 2024년 총강수량 차이는(절댓값)?
    suwon_rainfall_list_2024 = get_weather_data(suwon_weather_2024,3)
    jeonju_rainfall_list_2024 = get_weather_data(jeonju_weather_2024,3)
    total_rainfall_diff_2024 = round(abs(sum(suwon_rainfall_list_2024) - sum(jeonju_rainfall_list_2024)),1)

    name = "송경찬"
    affiliation = "스마트팜학과"
    student_id = "202217713"

    answer1 = total_rainfall_2015
    answer2 = max_of_tavg_2022
    answer3 = max_temp_diff_2024
    answer4 = total_rainfall_diff_2024

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)
if __name__ == "__main__":
    main()
