# 2. 기상자료를 받아서 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수, 총 강우량을 구하시오.
# 4) 최장연속강우일수는?
# 5) 강우이벤트 중 최대 강수량은? 비가 연속으로 올 때, 하나의 강우 이벤트로 가정
# 6) 가장 더운날 top 3(tmax의 최대값 3개)
# 7) 여름철(6월-8월) 총 강수량은? sumifs(rainfall, months, selected=[6,7,8])

def sumifs(rainfalls, months, selected=[6,7,8]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain
    return total
def t_max_top_3(t_max_data):
    # 가장 더운날 top3 
    top_3_temp = sorted(t_max_data, reverse=True)
    return top_3_temp[:3]

def get_rain_events(rainfalls):
    events = []
    continued_raindays = 0
    for rain in rainfalls:
        if rain > 0 :
            continued_raindays += 1
        else : 
            events.append(continued_raindays)
            continued_raindays = 0
    if continued_raindays != 0:
        events.append(continued_raindays)
    return max(events)

def event_rain_max(rainfall):
    a = []
    continued_rain_max = 0
    for rain in rainfall:
        if rain > 0 :
            a.append(rain)
        else:
            if sum(a) > continued_rain_max :
                continued_rain_max = sum(a)
            a.clear()
    if a :
        if sum(a) > continued_rain_max:
            continued_rain_max = sum(a)
    return continued_rain_max
    
def get_weather_data(fname,col_idx):
    with open(fname,'r',encoding='utf-8-sig') as f:
        files = f.readlines()
        weather_data = []
        for file in files[1:]:
            b = file.strip().split(',')
            weather_data.append(float(b[col_idx]))
    return weather_data

def average(nums):
    return sum(nums) / len(nums)

def count_bigger_days(nums,criteria):
    count = 0
    for num in nums:
        if num >= criteria:
            count +=1
    return count

def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw09/weather(146)_2022-2022.csv'
    rainfalls = get_weather_data(filename,9)
    months = get_weather_data(filename,1)
    t_max = get_weather_data(filename,3)
    t_avg = get_weather_data(filename,4)
    rainfall_over_5 = count_bigger_days(rainfalls,5)
    total_rain = sum(rainfalls)
    continued_rain_days = get_rain_events(rainfalls)
    event_max_rain = event_rain_max(rainfalls)
    temp_top_3 = t_max_top_3(t_max)
    rainfall_6_to_8 = sumifs(rainfalls,months)
    print(f'연평균 기온 : {average(t_avg):.2f}℃') # 과제10 1번
    print(f'5mm 이상 강우일수 : {rainfall_over_5}일') # 과제10 2번
    print(f'총 강우량 : {total_rain:.2f}mm') # 과제10 3번
    print(f'최장 연속 강우일수 : {continued_rain_days}일') # 과제10 4번
    print(f'강우 이벤트 중 최대 강수량 : {event_max_rain:.2f}mm') # 과제10 5번
    print(f'가장 더운 날 top 1 : {temp_top_3[0]}℃') # 과제10 6번
    print(f'가장 더운 날 top 2 : {temp_top_3[1]}℃') # 과제10 6번
    print(f'가장 더운 날 top 3 : {temp_top_3[2]}℃') # 과제10 6번
    print(f'여름철(6월-8월) 총 강수량은? : {rainfall_6_to_8:.2f}mm') # 과제10 7번
if __name__ == "__main__":
    main()
