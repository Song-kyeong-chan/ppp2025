def main():
    print("Hello, World!")
if __name__ == "__main__":
    main()

def c2f(t_c):
    temp_f = t_c * 9/5 + 32
    return temp_f
temp_c = int(input("섭씨온도를 입력하세요!: "))
temp_f = c2f(temp_c)
print(f"섭씨 {temp_c}℃ => 화씨 {temp_f}℉")
