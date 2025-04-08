'''
3. 연도(y)를 주면, 윤년인지(True) 아닌지를(False) 알려주는 is_leap_year(y) 함수를 만드시오.
단 윤년의 조건은 주어진 조건으로 구현하시오. 4로 나누었을 때 나누어 떨어지면 윤년. 4로 나
누어떨어지더라도, 100으로 나누어 떨어진다면, 윤년 아님.
'''
def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            return False # 윤년 아님.
        else:
            return True # 윤년.
    else:
        return False # 윤년 아님.
    
def main():
	y_input = int(input('연도를 입력하세요: '))
	print(is_leap_year(y_input))
 
if __name__ == "__main__":
	main()
