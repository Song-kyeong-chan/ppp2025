"""
과제#03에서 반지름을 입력받아서, 원의 둘레와 원의 면적을 출력하는 프로그램을 작성
하시오. 단 둘레는 소수점 1자리까지, 원의 면적은 소수점 2번째 자리까지 표시하시오.
round 함수를 쓸 수 있겠으나, 출력시 포맷 기능을 활용하는 것을 권장함.
"""

import math

circle_r = int(input("원의 반지름을 입력하시오.: "))
circle_c = 2 * circle_r * math.pi
circle_area = pow(circle_r,2) * math.pi
print(f"반지름이 {circle_r}인 원의 둘레은 {circle_c:.1f}입니다.")
print(f"반지름이 {circle_r}인 원의 면적은 {circle_area:.2f}입니다.")