# 1. 수업시간 제시한 코드 혹은 본인이 작성한 코드를 활용하여, 칼로리 계산 프로그램을 완성하시오. 식품별 칼로리 정보를 파일에서 읽어서 처리

def read_db(filename):
    with open(filename,'r',encoding='utf-8-sig') as f:
        lines = f.readlines()
        fruits_cal = {}
        a = 0
        for line in lines[1:]:
                token = line.strip('\n').split(',')
                fruits_cal[token[0]] = int(token[1])
    return fruits_cal

def main():
    fruit_kcal = read_db('./calorie_db.csv')
    fruit_eat = {'쑥' : 200, '바나나': 200}
    total = 0
    for item in fruit_eat:
        total += fruit_eat[item] * fruit_kcal[item]
    print(f'총 칼로리는 {total}kcal 입니다.') 
    
if __name__ == "__main__":
    main()
