valor = int(input())

for i in range(valor + 12):
    if i % 2 != 0 and i >= valor:
        print(i)
