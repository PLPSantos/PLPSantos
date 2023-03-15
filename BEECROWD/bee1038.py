cod, quant = input().split(" ")
cod = int(cod)
quant = int(quant)

if (cod == 1):
    print(f'Total: R$ {4 * quant:.2f}')
elif (cod == 2):
    print(f'Total: R$ {4.50 * quant:.2f}')
elif (cod == 3):
    print(f'Total: R$ {5 * quant:.2f}')
elif (cod == 4):
    print(f'Total: R$ {2 * quant:.2f}')
elif (cod == 5):
    print(f'Total: R$ {1.50 * quant:.2f}')
