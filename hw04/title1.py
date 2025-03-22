'''
과제#03의 BMI 계산결과에 따라 아래 텍스트를 참고하여, 비만 정도를 표시하시오.
 “2020년 비만 진료지침에서는 체질량지수(BMI) △23~24.9kg/㎡를 비만 전단계
△25~29.9kg/㎡를 1단계 비만 △30~34.9kg/㎡를 2단계 비만 △35kg/㎡ 이상을 3단
계 비만으로 정의했다.”
'''

import math

def Bmi(bmi_list):
    bmi = bmi_list[1] / pow(bmi_list[0]/100,2)
    if bmi >= 23 and bmi <= 24.9 : 
        print("키 {}cm에 몸무게 {}kg 인 사람의 bmi는 {:.2f}이고 비만 전단계입니다.".format(bmi_list[0],bmi_list[1],bmi))
    elif bmi >= 25 and bmi <= 29.9 :
        print("키 {}cm에 몸무게 {}kg 인 사람의 bmi는 {:.2f}이고 1단계 비만입니다.".format(bmi_list[0],bmi_list[1],bmi))
    elif bmi >= 30 and bmi <= 34.9 :
        print("키 {}cm에 몸무게 {}kg 인 사람의 bmi는 {:.2f}이고 2단계 비만입니다.".format(bmi_list[0],bmi_list[1],bmi))
    elif bmi >= 35 :
        print("키 {}cm에 몸무게 {}kg 인 사람의 bmi는 {:.2f}이고 3단계 비만입니다.".format(bmi_list[0],bmi_list[1],bmi))
    else :
        print("비만은 아닙니다.")
bmi_list = list(map(int,input("키와 몸무게를 입력하세요.(ex:170 60) : ").split(" ")))
Bmi(bmi_list)


