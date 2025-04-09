# 2. 기상자료를 받아서 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수, 총 강우량을 구하시오.

def year_avg_t(files, month_index,tavg_index):
    # 1~12월 일자별 온도데이터 리스트로 기록
    tavg = {i : [] for i in range(1,13)}
    for file in files[1:]:
        tavg[int(file[month_index])].append(float(file[tavg_index]))
        
    # 총 온도
    total_t = 0
    # 일수 길이
    len_t = 0 
    for i in tavg:
        total_t += sum(tavg[i])
        len_t += len(tavg[i])
    # 평균 온도
    avg_t = total_t / len_t
    return avg_t

def rain_5_more_total(files,month_index,rainfall_index):   
    # 1~12월 일자별 강우데이터 리스트로 기록
    rainfall = {i : [] for i in range(1,13)}
    for file in files[1:]:
        month = int(file[month_index])               
        rainfall[int(file[month_index])].append(float(file[rainfall_index]))
        
    # 5mm 이상 강우일수 구하기  
    num_rain = 0
    for i in rainfall.values():
        for j in i:
            if j >= 5 :
                num_rain += 1
                
    # 총 강우량 구하기
    total = 0
    for i in rainfall:
        total += sum(rainfall[i])
        
    return num_rain, total

def main():
    filename = '/Users/song-gyeongchan/Desktop/code/ppp2025/hw09/weather(146)_2022-2022.csv'
    with open(filename,'r',encoding='utf-8-sig') as f:
        files = [a.strip().split(', ') for a in f.readlines()]
        # 기상자료 헤더부분 추출
        t_data = files[0]
        # t_data에서 month 순서 추출
        month_index = t_data.index('month')
        # t_data에서 tavg 순서 추출
        tavg_index = t_data.index('tavg')
        # t_data에서 rainfall 순서 추출
        rainfall_index = t_data.index('rainfall')
        # 연평균 기온
        y_avg_temp = year_avg_t(files,month_index,tavg_index)
        print(f'연평균 기온 : {y_avg_temp:.2f}℃')
        # 5mm 이상 강우일수 , 총 강우량
        num_rain , total_rain = rain_5_more_total(files,month_index,rainfall_index)
        print(f'5mm 이상 강우일수 : {num_rain}일')
        print(f'총 강우량 : {total_rain}mm')
        
if __name__ == "__main__":
    main()
