N1, N2, N3, N4 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)


media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1)/10


if (media >= 7):
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')

elif (media < 5):
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')


elif (media >= 5 and media < 7):
    N5 = float(input())
    exame = (media + N5) / 2
    if (exame >= 5):

        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        print(f'Nota do exame: {N5:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {exame:.1f}')
    else:
        print(f'Media: {media:.1f}')
        print('Aluno em exame.')
        print(f'Nota do exame: {N4:.1f}')
        print('Aluno reprovado.')
        print(f'Media final: {exame:.1f}')
