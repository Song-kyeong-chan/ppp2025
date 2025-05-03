import requests
import os

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
            datas.append(float(line[col_idx]))
    return datas

# 5mm 이상 강우일수 측정
def rainfall_over_5(data, min = 5):
    day = 0
    for rain in data:
        if rain >= min:
            day += 1
    return day

def main():
    filename = "./weather_146_2020-2020.csv"
    if not os.path.exists(filename):
        download_weather(146,2020,filename)
        
    # 평균온도 데이터
    avg_t_data = get_weather_data(filename,4)
    # 2020 연평균 온도
    avg_t_2020 = sum(avg_t_data) / len(avg_t_data)
    
    # 강우량 데이터
    rainfall_data = get_weather_data(filename,9)
    # 5mm 이상 강우일수
    rainfall_over_5_days = rainfall_over_5(rainfall_data)
    # 총 강우량
    total_rainfall = sum(rainfall_data)
    
    # 결과는 화면에 출력하지 않고, 파일에 저장하도록 하시오.
    result_data = [avg_t_2020,rainfall_over_5_days,total_rainfall]
    fname = './weather_results_hw12.txt'
    with open(fname, 'w', encoding='utf-8-sig') as f:
            # 1) 연평균 기온(일평균 기온의 연평균)
            f.write(f'2020년도 연평균 기온은 {result_data[0]:.2f}°C 입니다.\n')
            # 2) 5mm이상 강우일수
            f.write(f'2020년도 5mm 이상 강우일수는 {result_data[1]:.2f}일 입니다.\n')
            # 3) 총 강우량
            f.write(f'2020년도 총 강우량은 {result_data[2]:.2f}mm 입니다.\n')
            
if __name__ == "__main__":
    main()
    