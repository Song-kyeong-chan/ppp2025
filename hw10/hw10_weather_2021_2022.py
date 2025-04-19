# 2021년과 2022년 총 강수량은?
def get_weather_data(filename,col_num):
    with open(filename,'r',encoding='utf-8-sig') as f:
        files = f.readlines()
        weather_data = []
        for file in files[1:]:
            a = file.strip().split(',')
            weather_data.append(float(a[col_num]))
    return weather_data

def sumifs(rainfalls, years, selected = [2021,2022]):
    rain_sum = 0
    for i in range(len(rainfalls)):
        if years[i] in selected:
            rain_sum += rainfalls[i]
    return rain_sum        

def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw09/weather(146)_2001-2022.csv'
    rainfalls = get_weather_data(filename,9)
    years = get_weather_data(filename,0)
    print(f'2021년 총 강수량은? {sumifs(rainfalls,years,selected=[2021]):.2f}mm')
    print(f'2022년 총 강수량은? {sumifs(rainfalls,years,selected=[2022]):.2f}mm')
    return ;
if __name__ == "__main__":
    main()