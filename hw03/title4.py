#사다리꼴 면적구하기
def trapezoid_area():
        area = (trapezoid_a + trapezoid_b) * trapezoid_h / 2
        return area
trapezoid_a = int(input("사다리꼴의 밑면적을 입력하시오: "))
trapezoid_b = int(input("사다리꼴의 윗면적을 입력하시오: "))
trapezoid_h = int(input("사다리꼴의 높이를 입력하시오: "))
area = trapezoid_area()
print("밑변의 길이가 {}cm고 윗변의 길이가{}cm이고 높이가 {}cm인 사다리꼴의 면적은 {}cm2입니다.".format(trapezoid_a,trapezoid_b,trapezoid_h,area))