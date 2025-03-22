# 키와 몸무게가 임의로 주어졌을떄 BMI구하기
weight = 60
height = 170
bmi = weight / (height/100) ** 2
print("키 {}, 몸무게 {}일떄 BMI는 {:.2f}입니다.".format(height,weight,bmi))
