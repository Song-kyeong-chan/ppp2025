# 키와 몸무게가 임의로 주어졌을떄 BMI구하기
import math
def Bmi():
    bmi = bmi_list[1] / pow(bmi_list[0]/100,2)
    return bmi
bmi_list = list(map(int,input("키와 몸무게를 입력하세요.(ex:170 60) : ").split(" ")))
bmi = Bmi()
print("키 {}cm에 몸무게 {}kg 인 사람의 bmi는 {:.2f}kg/m2입니다.".format(bmi_list[0],bmi_list[1],bmi))


