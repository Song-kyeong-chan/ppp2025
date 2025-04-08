# 2. 1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 get_range_list(n)
def get_range_list(n):
    kk = []
    for i in range(1,n+1):
        kk.append(i)
    return kk

def main():
	num = int(input('숫자를 입력하세요!: '))
	order_num = get_range_list(num)
	print(order_num)
 
if __name__ == "__main__":
	main()
