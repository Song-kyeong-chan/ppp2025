def hangman(item:list = ['apple','banana','melon'],trial: int = 7) -> str:
    solution = r.choice(item)
    sol = ['_' for i in range(len(solution))]

    while trial > 0 :
        a = ' '.join(sol)
        print(f'{a}(trial = {trial}) 답을 입력하세요 => ', end='')
        ans = input('')
        if ans in solution:
            for i in range(len(solution)):
                if ans == solution[i]:
                    sol[i] = ans
                if not '_' in sol:
                    win = '승리, 정답은' + solution
                    return win
        else:
            trial -= 1
            
    lose = '패배, 정답은' + solution 
    return lose

def main():
    item = ['apple','banana','pineapple','lemon']
    print(hangman(item))

if __name__ == "__main__":
    main()
