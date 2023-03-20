nome = (input())
salariofixo = float(input())
comissa = float(input())


certo = (comissa / 100 * 15) + salariofixo

print(f'TOTAL = R$ {certo:.2f}')
