import math
X1, Y1 = input().split(" ")
X2, Y2 = input().split(" ")

X1 = float(X1)
Y1 = float(Y1)
X2 = float(X2)
Y2 = float(Y2)

distancia = (X2 - X1) ** 2 + (Y2 - Y1) ** 2

distancia = math.sqrt(distancia)

print(f'{distancia:.4f}')
