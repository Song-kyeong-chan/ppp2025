# 섭씨를 화씨로 바꾸는 함수 c2f(t_c) 함수를 만드시오.
def c2f(t_c):
    temp_f = t_c * 9/5 + 32
    return temp_f

def main():
    temp_c = int(input("섭씨온도를 입력하세요!: "))
    temp_f = c2f(temp_c)
    print(f"섭씨 {temp_c}℃ => 화씨 {temp_f}℉")

if __name__ == "__main__":
    main()

