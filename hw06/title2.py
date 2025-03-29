# 숫자를 입력받아, 해당하는 구구단을 출력하는 함수 gugudan(dan)를 만드시오.
def gugudan(dan):
    for i in range(1,10):
        print(f'{dan} x {i} = {dan*i}')
    return ;

def main():
    dan = int(input("구구단 몇단 출력할까요?: "))
    gugudan(dan)
    
if __name__ == "__main__":
        main()

