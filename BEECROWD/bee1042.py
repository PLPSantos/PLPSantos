vasco = []


A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
vasco.append(A)
vasco.append(B)
vasco.append(C)


crescente = sorted(vasco)
decrescente = sorted(vasco, reverse=True)

for i in crescente:
    print(f'{i}')
print()
for i in vasco:
    print(f'{i}')
