# 5. 1번과제에서 만든 함수를 이용하며, 메인에서 split()함수를 이용하여 여러 값을 한줄로 입력받아 평균을 출력할 수 있는 프로그램을 완성하시오.
'''
def average(nums):
    a = 0
    b = 0
    for num in nums:
        a += num # 총합
        b += 1 # 리스트 길이
    return a/b
'''
def average(nums):
    return sum(nums)/len(nums)

def main():
        num_list = list(map(int,input("숫자를 입력하시오. ex) 1 2 4 5 6\n입력칸 : ").split()))
        print(average(num_list))
        
if __name__ == "__main__":
    main()