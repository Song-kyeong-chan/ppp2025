import time as t
def count_down(count):
    for i in range(count,0,-1):
        if i > 1:
            print(f'주어진 시간: {i}', end = '\r')
            t.sleep(1)
        else:
            print(f'주어진 시간: {i}')
            t.sleep(1)
    print("bomb")

def main():
    t = int(input('초를 입력하시오: '))
    count_down(t)

if __name__ == "__main__":
    main()
