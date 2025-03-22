def temp_change(temp_c):
    temp_f = temp_c * 9 / 5 + 32
    print("섭씨{}도는 화씨{}도 입니다.".format(temp_c,temp_f))
    return 0

temp_c = int(input("온도를 입력하시오. : "))
temp_change(temp_c)
