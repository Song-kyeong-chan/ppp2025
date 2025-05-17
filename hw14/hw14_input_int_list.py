'''
숫자를 입력 받아서 그 리스트를 출력하시오.
숫자는 정수만 입력 받고, 자연수가 아닌 입력 값은 무시하시오.
-1를 입력하면 입력을 더 이상받지 않고 현재까지 입력 받은 값을 출력하시오.
또한 총 개수와 평균을 구하시오.
'''
def int_list():
    l = []
    while True:
        int_num = input('X=? ')
        try:
            int_num = int(int_num)
            if int_num == -1 :
                try:
                    avg = sum(l)/len(l)
                    print(f'입력된 값은 {l}입니다. 총 {len(l)}개의 자연수가 입력되었고, 평균은 {avg}입니다.')
                    break
                except ZeroDivisionError:
                    print(f'입력된 값은 {l}입니다. 총 0개의 자연수가 입력되었고 평균은 0입니다.')
                    break
            elif int_num <= 0:
                print(f"자연수가 아닌 입력값 무시: {int_num}; 종료키: -1")
                continue
            else:
                l.append(int_num)
                print(f"입력된 값: {int_num}; 종료키: -1")
        except ValueError:
            print(f"자연수가 아닌 입력값 무시: {int_num}; 종료키: -1")
            continue
def main():
    int_list()
if __name__ == "__main__":
    main()
