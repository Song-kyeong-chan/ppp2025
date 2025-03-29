def main():
    print("Hello, World!")

if __name__ == "__main__":
        main()

def gugudan(dan):
    for i in range(1,10):
        print(f'{dan} x {i} = {dan*i}')
    return ;

dan = int(input("구구단 몇단 출력할까요?: "))
gugudan(dan)