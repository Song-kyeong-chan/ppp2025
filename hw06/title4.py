# 숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)
def sum_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def main():
    a = int(input("숫자를 입력하시오: "))
    total = sum_n(a)
    print(total)
if __name__ == "__main__":
    main()
