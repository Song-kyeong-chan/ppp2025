def text2list(input_text): 
    return [int(x) for x in input_text.split()] 

def average(a):
    b = 0
    c = 0
    for i in a:
        b += i
        c += 1
    return b/c

def median(a):
    a = sorted(a)
    b = len(a)//2
    return a[b]

def read_text(filename):
    with open(filename, 'r' , encoding= 'utf-8') as f:
        text = f.readlines()
        line = ""
        for t in text:
            line += " " + t.strip()
    return line

def read_numbers(filename):
    nums = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums
def main():
    text = './number1.txt'
    # read_number(text) 활용
    # print(read_numbers(text)) 출력: [1, 2, 3, 4, 5, 6, 7]
    # print(f'총 숫자의 개수 : {len(read_numbers(text))}') 출력: 총 숫자의 개수 : 7
    # print(f'주어진 숫자의 평균 : {average(read_numbers(text))}') 출력: 주어진 숫자의 평균 : 4.0
    # print(f'주어진 숫자의 최댓값 : {max(read_numbers(text))}') 출력: 주어진 숫자의 최댓값 : 7
    # print(f'주어진 숫자의 최솟값 : {min(read_numbers(text))}') 출력: 주어진 숫자의 최솟값 : 1
    # print(f'중앙값 : {median(read_numbers(text))}') 출력: 중앙값 : 4 
    
    # read_text() , text2list() 함수 활용            
    b = text2list(read_text(text))
    # print(b) 출력: [1, 2, 3, 4, 5, 6, 7]
    print(f'1) 총 숫자의 개수 : {len(b)}')
    print(f'2) 중앙값 : {median(b)}')
    print(f'3) 퍙균깂 : {average(b)}')
    print(f'4) 주어진 숫자의 최댓값 : {max(b)}') 
    print(f'5) 주어진 숫자의 최솟값 : {min(b)}')
if __name__ == "__main__":
    main()
