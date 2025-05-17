import random as r

def to_chosung(text):
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    full_text = []
    for i in text:
        try:
            t = ord(i) - ord('가')
            k = t // (21 * 28)
            full_text.append(chosung_list[k])
        except:
            full_text.append(i)
    return ''.join(full_text)

def chosung_game():
    problem = ['바나나', '딸기', '수박', '메론']
    solution = problem[r.randrange(len(problem))]
    chosung = to_chosung(solution)

    print('초성게임 시작!')
    while True:
        user_input = input(f'{chosung}?  ')
        if user_input == solution:
            print("정답입니다.")
            break
        else:
            print("오답입니다.")

def main():
    chosung_game()

if __name__ == "__main__":
    main()
