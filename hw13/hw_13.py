def str2float(text:str, default_value: float = -999) -> float :
    try:
        return float(text)
    except ValueError:
        print(f"에러났어요...! {text}!")
        return default_value

def int_list():
    l = []
    while True:
        int_num = input('X=? ')
        try:
            int_num = int(int_num)
            if int_num == -1 :
                break
            elif int_num < 0:
                continue
            else:
                l.append(int_num)
        except ValueError:
            continue
    print(f'입력된 값은 {l}입니다. 총 {len(l)}개의 자연수가 입력되었고, 평균은 {sum(l)/len(l)}입니다.')
def main():
    # print(str2float("0.5"))
    # print(str2float("3.555"))
    # print(str2float("3.5.55"))
    int_list()
if __name__ == "__main__":
    main()