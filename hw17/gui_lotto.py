import tkinter as tk
from rich import print
import random as r

def gui_input() -> str:
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        print("입력 오류", "1 이상의 숫자를 입력하세요.")
        return
    
    random_lotto(n)

def random_lotto(trial):
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
        print(f'{i+1}번 로또번호 {total_lotto_list[i]}')
    return total_lotto_list

def gui_get_lotto() -> list:
    global entry
    window = tk.Tk()
    window.title('행운의로또')
    label = tk.Label(window,text='횟수를 입력하세요.')
    label.pack(pady= 5)
    entry = tk.Entry(window)
    entry.pack(pady=5)
    button = tk.Button(window,text='로또번호생성',command=gui_input)
    button.pack(pady=10)
    window.mainloop()
    

def main():
    gui_get_lotto()

if __name__ == "__main__":
    main()