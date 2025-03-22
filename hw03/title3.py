#원의 면적구하기
import math
def circle_area(circle_r):
    area = pow(circle_r,2) * math.pi
    return area
circle_r = int(input("원의 반지름을 입력하시오.: "))
area = circle_area(circle_r)
print("반지름이 {}cm인 원의 면적은 {:.2f}cm2입니다.".format(circle_r,area))
