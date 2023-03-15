linha1 = input().split(" ")

coprod = int(linha1[0])
numpeca = int(linha1[1])
valorpeca = float(linha1[2])

linha2 = input().split(" ")

coprod1 = int(linha2[0])
numpeca1 = int(linha2[1])
valorpeca1 = float(linha2[2])

preco = (numpeca * valorpeca) + (numpeca1 * valorpeca1)

print(f'VALOR A PAGAR: R$ {preco:.2f}')
