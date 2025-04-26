
# 3. 2001년부터 2022년까지 각 해마다 4월부터 시작해서, 적산온도가 200이 넘는 최초일을 구하시오.
    
def get_weather_date_tavg(filename, col_idx = 4 , year_start = 2001, year_last = 2022):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        files = f.readlines()
        dates = {i : [] for i in range(year_start,year_last+1)}
        for file in files[1:]:
            weather_date = file.strip().split(',')
            data = [int(weather_date[1]),int(weather_date[2]),float(weather_date[col_idx])]
            year = int(weather_date[0])
            dates[year].append(data)
    return dates

             
def gdd_200_over_2001_2022(tavg_dates,base_temp = 5, base_month = 4):
    for year,data in tavg_dates.items():
        total_gdd = 0
        for month,day,tavg in data:
            if month >= base_month:
                if tavg >= base_temp:
                    total_gdd += tavg - base_temp
                    # print(f'적산온도의 합 : {a}, {year}/{month}/{day}, 평균온도 : {tavg}, 적산온도 : {tavg - base_temp}')
            if total_gdd >= 200:
                print(f'적산온도의 합 : {total_gdd:.1f}, 적산온도가 200이 넘는 최초일 : {year}/{month:02d}/{day:02d}')
                break 
def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw10/weather(146)_2001-2022.csv'
    weather_dates_tavg = get_weather_date_tavg(filename)
    gdd_200_over_2001_2022(weather_dates_tavg)
if __name__ == "__main__":
    main()
