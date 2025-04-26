# 2. 해당기간동안 각 연도별로 5월부터 9월까지 적산온도를 구하시오.
'''
def gdd(tavg, base_temp = 5):
    temp_cum = 0
    for t in tavg:
        if t >= base_temp:
            temp_cum += (t-base_temp)
    return temp_cum 
'''

def get_weather_data(filename, col_idx):
    with open(filename,'r',encoding='utf-8-sig') as f:
        weather_data = []
        files = f.readlines()
        for file in files[1:]:
            a = file.strip().split(',')
            weather_data.append(float(a[col_idx]))
        return weather_data

def get_weather_date(filename):
    with open(filename,'r',encoding='utf-8-sig') as f:
        weather_date = []
        files = f.readlines()
        for file in files[1:]:
            a = file.strip().split(',')
            weather_date.append(list(map(int,a[0:3])))
        return weather_date
 
                
def gdd_season(tavg,dates, base_temp = 5, start_year = 2001):
    temp_cum = 0
    for i in range(len(tavg)):
        if dates[i][0] == start_year:
            if dates[i][1] in [5,6,7,8,9]:
                t = tavg[i]
                if t >= base_temp:
                    temp_cum += (t-base_temp)
        else:
            print(f'{dates[i][0]-1} {temp_cum:.1f}')
            temp_cum = 0
            start_year = dates[i][0]
            if dates[i][1] in [5,6,7,8,9]:
                t = tavg[i]
                if t >= base_temp:
                    temp_cum += (t-base_temp)
    print(f'{start_year} {temp_cum:.1f}')


def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw10/weather(146)_2001-2022.csv'
    dates = get_weather_date(filename)
    tavg = get_weather_data(filename,4)
    gdd_season(tavg,dates)
    
if __name__ == "__main__":
    main()
