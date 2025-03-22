# 과일 칼로리 구하기
hanrabong_g = int(input("한라봉 g수를 입력하시오.: ")) # 50kcal / 100g
apple_g = int(input("사과의 g수를 입력하시오.: ")) # 52kcal / 100g
raisin_g = int(input("건포도의 g수를 입력하시오.: ")) # 297kcal / 100g
hanrabong_kcal = hanrabong_g * 0.5
apple_kcal = apple_g * 0.52
raisin_kcal = raisin_g * 2.97
print("{}g 한라봉는 {:.2f}kcal이고, {}g 사과는 {:.2f}kcal이고, {}g 건포도는 {:.2f}kcal입니다.".format(hanrabong_g,hanrabong_kcal\
    ,apple_g, apple_kcal, raisin_g, raisin_kcal))

