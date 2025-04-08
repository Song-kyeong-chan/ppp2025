# 1. 숫자 리스트를 매개변수로 받아서 평균을 구하는 함수를 완성하시오. 함수는 average(nums)
def average(nums):
    a = 0
    b = 0
    for num in nums:
        a += num # 총합
        b += 1 # 리스트 길이
    return a/b

def main():
        num_list = [1,23,24,53,56]
        print(average(num_list))
        
if __name__ == "__main__":
    main()
