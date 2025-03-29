# 칼로리 계산 프로그램(과제#04-03)를 수정하여, 총 칼로리를 계산하시오.(반복문, 사전 활용)
def total_calories(fruits,calories_g):
    calories = 0
    f_calories ={}
    for fruit in fruits:
        a = int(input(f'먹은 {fruit}의 g수를 입력하세요: '))
        f_calories[fruit] = calories_g[fruit] * a
        calories += f_calories[fruit]
    print(f'먹은 과일 당 kcal : {f_calories}')
    return calories
def main():
    fruits = ["hanrabong", "apple", "raisin"] # 과일
    calories_g = {"hanrabong": 0.5, "apple" : 0.52, "raisin" : 2.97} # 한라봉 : 50kcal/100g, 사과 : 52kcal/100g, 건포도 297kcal/100g
    a = total_calories(fruits,calories_g)
    print(f'total_calrories : {a:,.2f}')    
if __name__ == "__main__":
        main()

