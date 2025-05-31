import tkinter as tk
from rich import print
import time as t
def gui_input():
    try:
        count = int(entry.get())
    except ValueError:
        print("입력 오류", "숫자를 입력하세요!")
        return
    countdown(count)
    
def countdown(count):
    for i in range(count,0,-1):
        if i > 1:
            print(f'주어진 시간: {i}', end = '\r')
            t.sleep(1)
        else:
            print(f'주어진 시간: {i}')
            t.sleep(1)
    print("bomb")
    
def gui_count_down():
    global entry
    window = tk.Tk()
    text = tk.Label(window,text="카운트를 입력하세요.")
    text.pack(pady=5)
    entry = tk.Entry(window)
    entry.pack(pady=5)
    button = tk.Button(window,text='시작',command=gui_input)
    button.pack(pady=5)
    label = tk.Label(window, text="")
    label.pack(pady=10)

    window.mainloop()
def main():
    gui_count_down()

if __name__ == "__main__":
    main()