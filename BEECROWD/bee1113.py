X, Y = input().split(" ")
X = int(X)
Y = int(Y)
lista = []
crescente = 'Crescente'
decrescente = 'Decrescente'
if X < Y: 
    lista.append(crescente)
else:
    lista.append(decrescente)
while X != Y:
    X, Y = input().split(" ")
    if X < Y:
        lista.append(crescente)
    elif X > Y:
        lista.append(decrescente)

for i in lista:
    print(i)
# Não finalizado erro no beecrowd aparenta estar certo
    
       