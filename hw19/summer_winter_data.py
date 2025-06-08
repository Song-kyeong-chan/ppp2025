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
        download_weather(146,1980,2024,filename)
    
    df = pd.read_csv(filename)
    df.columns = df.columns.str.strip()
    summer = df[df['month'].isin([6,7,8])]
    winter = df[df['month'].isin([12,1,2])]
    
    # 여름 온도 데이터
    t_max_summer = summer['tmax']
    t_min_summer = summer['tmin']
    t_avg_summer = summer['tavg']
    
    # 겨울 온도 데이터
    t_max_winter = winter['tmax']
    t_min_winter = winter['tmin']
    t_avg_winter = winter['tavg']
    
    fig, ax = plt.subplots(1,2, figsize = (12,5))
    
    # 평균 온도 빈도
    ax[0].hist([t_avg_summer,t_avg_winter], label = ['여름철 평균 온도','겨울철 평균 온도'])
    ax[0].set_xlabel('온도(°C)')
    ax[0].set_ylabel('빈도')
    ax[0].set_title("평균 온도 빈도")
    ax[0].legend()
    
    # 최저/최고 온도 빈도
    ax[1].hist([t_max_summer,t_max_winter,t_min_summer,t_min_winter],label = ['여름철 최고온도','겨울철 최고온도','여름철 최저온도','겨울철 최저온도'])
    ax[1].set_xlabel('온도(°C)')
    ax[1].set_ylabel('빈도')
    ax[1].set_title("최저/최고 온도 빈도")
    ax[1].legend()
    plt.savefig('./hw19/frequency_summer_winter_temp_1980_2024')
    
    plt.show()
if __name__ == "__main__":
    main()
