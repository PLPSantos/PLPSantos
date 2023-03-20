X = int(input())
Y = int(input())
Lista = []
soma_impar = 0

for i in range(Y + 1, X):
    if i % 2 != 0:
        Lista.append(i)

soma_impar = sum(Lista)
print(soma_impar)
