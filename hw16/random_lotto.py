import random as r

def get_lotto(trial: int = 3) -> list:
    total_lotto_list = []
    for i in range(trial):
        lotto_list = []
        while True:
            random_number = r.randint(1,45)
            if not random_number in lotto_list:
                lotto_list.append(random_number)
            if len(lotto_list) == 6:
                break
        total_lotto_list.append(sorted(lotto_list))
    for i in range(len(total_lotto_list)):
        print(f'{i}번 로또번호 {total_lotto_list[i]}')
    return total_lotto_list

def main():
    a = int(input('원하는 횟수를 입력하시오: '))
    print(get_lotto(a))
if __name__ == "__main__":
    main()
