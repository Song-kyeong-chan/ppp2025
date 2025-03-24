# 구구단을 외우자
a = [[i*j for i in range(1,10)] for j in range(1,10)]
ss = int(input("숫자를 입력하세요: ")) 

for i in range(9):
    if ss == a[i][0]:
        for j in range(9):
            print(f'{i+1} x {j+1} = {a[i][j]}')

