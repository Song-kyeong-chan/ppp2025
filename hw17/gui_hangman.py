import tkinter as tk
from tkinter import simpledialog
from rich import print
import random as r

def gui_input(text:str) -> str:
    return simpledialog.askstring(title="행맨게임", prompt = text)

def gui_hangman(item:list = ['apple','banana','melon'],trial: int = 7) -> str:
    window = tk.Tk()
    window.withdraw()
    solution = r.choice(item)
    sol = ['_' for i in range(len(solution))]

    while trial > 0 :
        a = ' '.join(sol)
        text = f'{a}(trial = {trial}) 답을 입력하세요 => '
        ans = gui_input(text)
        if ans in solution:
            for i in range(len(solution)):
                if ans == solution[i]:
                    sol[i] = ans
                    print('좋습니다!')
                if not '_' in sol:
                    win = '승리, 정답은' + solution
                    print(win)
                    return ''
        else:
            trial -= 1
            print('다른 문자를 입력해보세요.')
            
    lose = '패배, 정답은' + solution 
    print(lose)
    return ''

def main():
    gui_hangman()

if __name__ == "__main__":
    main()