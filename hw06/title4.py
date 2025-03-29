def main():
    print("Hello, World!!")
if __name__ == "__main__":
    main()

def sum_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

a = int(input("숫자를 입력하시오: "))
total = sum_n(a)
print(total)
