# 삼각함수 표를 구하시오. (0~90)
import math
# n = int(input("숫자를 입력하세요"))
n = 90
for i in range(n+1):
    a = math.radians(i)
    print(f"각{i} => 라디안{i} : {a:.4f}, sin{i} : {math.sin(a):.4f}, cos{i} : {math.cos(a):.4f}, tan{i} : {math.tan(a):.4f}")


v = [[] for j in range(n+1)]
for i in range(n+1):
    a = math.radians(i)
    v[i].append(round(a,4))
    v[i].append(round(math.sin(a),4))
    v[i].append(round(math.cos(a),4))
    v[i].append(round(math.tan(a),4))
print(v)