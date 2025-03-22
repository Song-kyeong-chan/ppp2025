#섭씨를 화씨로 변환하는 프로그램
def temp_change_from_c_to_f():
    temp_f = temp_c * 9 / 5 + 32
    return temp_f
temp_c = float(input("온도를 입력하시오. : "))
temp_f = temp_change_from_c_to_f(temp_c)
print("섭씨{}℃는 화씨{}℉ 입니다.".format(temp_c,temp_f))
