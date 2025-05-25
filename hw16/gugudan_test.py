def gugudan(start: int = 1 , end: int = 10, problem_number: int = 5) -> float:
    is_collect = 0
    problem_number = 5
    for i in range(problem_number):
        gugudan_number1 = r.randint(start,end)
        gugudan_number2 = r.randint(start,end)
        solution = gugudan_number1 * gugudan_number2
        print(f"{gugudan_number1} * {gugudan_number2} =  ", end = '')
        ans = int(input())
        try:
            if ans == solution:
                is_collect += 1
                print('정답!')
            else:
                print(f'오답, 정답은 {solution}입니다 ㅋ')
        except:
            print('error')
    total_score = 100/problem_number * is_collect      
    print(f'총 {total_score}점 맞았습니다.')

def main():
    a = r.randint(1,100)
    b = r.randint(1,100)
    if a > b:
        gugudan(b,a)
    else:
        gugudan(a,b)

if __name__ == "__main__":
    main()
