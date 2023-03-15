x = input().split(" ")
v1, v2, v3 = x
v1 = float(v1)
v2 = float(v2)
v3 = float(v3)
perimetro = v1 + v2 + v3
area = ((v1 + v2) / 2) * v3

if abs(v2 - v3) < v1 < (v2 + v3) and (v1 - v3) < v2 < (v1 + v3) and (v1 - v2) < v3 < (v1 + v2):
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')
