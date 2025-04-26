def maximum_temp_gap(dates,tmax,tmin, start_year = 2001):
    max_gap_date = dates[0]
    max_gap = tmax[0] - tmin[0]
    year = start_year
    for i in range(len(dates)):
        if year == dates[i][0]:
            date = dates[i]
            tx = tmax[i]
            tm = tmin[i]
            gap = tx - tm
            if max_gap < gap : 
                max_gap = gap
                max_gap_date = date
        else:
            print(f'{max_gap_date[0]}/{max_gap_date[1]:02d}/{max_gap_date[2]:02d}  {max_gap:.1f}')
            max_gap_date = dates[i]
            max_gap = tmax[i] - tmin[i]
            year = dates[i][0]
    print(f'{max_gap_date[0]}/{max_gap_date[1]:02d}/{max_gap_date[2]:02d}  {max_gap:.1f}')
    return 

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


def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw10/weather(146)_2001-2022.csv'
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    dates = get_weather_date(filename)
    maximum_temp_gap(dates, tmax, tmin)

if __name__ == "__main__":
    main()