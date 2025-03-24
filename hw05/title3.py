#과제03에서 칼로리 계산 프로그램을 사전형(딕셔너리)를 이용하여 구현하시오.
eat_calories = {} # 먹은 과일 칼로리
fruits = ["hanrabong", "apple", "raisin"] # 과일
calories_g = {"hanrabong": 0.5, "apple" : 0.52, "raisin" : 2.97} # 한라봉 : 50kcal/100g, 사과 : 52kcal/100g, 건포도 297kcal/100g
eat_g = dict(zip(fruits, map(int, input("먹은 한라봉 사과 건포도 g수를 입력하시오 ex)10 10 20: ").split(' ')))) # 먹은 과일 그램
total_calories = 0
for fruit in fruits:
    eat_calories[fruit] = eat_g[fruit] * calories_g[fruit]
    total_calories += eat_calories[fruit]

print(f"{eat_g['hanrabong']}g 한라봉은 {eat_calories['hanrabong']:.2f}kcal이고 {eat_g['apple']}g 사과는 {eat_calories['apple']:.2f}kcal이고 \
    {eat_g['raisin']}g 건포도는 {eat_calories['raisin']:.2f}kcal 이며 총{total_calories:.2f}kcal 입니다.")


