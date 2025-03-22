# x,y 좌표
import math
x = int(input("x의 값을 입력하시오: "))
y = int(input("y의 값을 입력하시오: "))

if x > 0 and y > 0 :
    print("x={}, y={} => 입력한 좌표는 1사분면입니다.".format(x,y))
elif x < 0 and y > 0 :
    print("x={}, y={} => 입력한 좌표는 2사분면입니다.".format(x,y))
elif x < 0 and y < 0 :
    print("x={}, y={} => 입력한 좌표는 3사분면입니다.".format(x,y))
elif x > 0 and y < 0 :
    print("x={}, y={} => 입력한 좌표는 4사분면입니다.".format(x,y))
else :
    if x == 0 and y != 0: 
        print("x={}, y={} => 입력한 좌표는 y좌표위에 있습니다.".format(x,y))
    elif x != 0 and y == 0:
        print("x={}, y={} => 입력한 좌표는 x좌표위에 있습니다.".format(x,y))
    else :
        print("x={}, y={} => 입력한 좌표는 원점에 있습니다.".format(x,y))
    
   