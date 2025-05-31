import tkinter as tk
from tkinter import simpledialog
from rich import print
import random as r
def gui_input(text:str,title:str ="구구단시험") -> str:
    return simpledialog.askstring(title=title, prompt = text)

def gui_gugudan(start: int = 1 , end: int = 10, problem_number: int = 5) -> float:
    is_collect = 0
    problem_number = 5
    window = tk.Tk()
    window.withdraw()
    for i in range(problem_number):
        gugudan_number1 = r.randint(start,end)
        gugudan_number2 = r.randint(start,end)
        solution = gugudan_number1 * gugudan_number2
        text = f"{gugudan_number1} * {gugudan_number2} = ?"
        user_input = int(gui_input(text))

        try:
            if user_input == solution:
                is_collect += 1
                print(f'정답! {is_collect}/{problem_number}')
            else:
                print(f'오답, 정답은 {solution}입니다 ㅋ {is_collect}/{problem_number}')
        except:
            print('error')
    total_score = 100/problem_number * is_collect      
    print(f'총 {total_score}점 맞았습니다.')
    
def main():
    gui_gugudan()

if __name__ == "__main__":
    main()