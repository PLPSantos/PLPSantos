entrada = int(input())
medias = []

for i in range(entrada):
    n1,n2,n3 = input().split(" ")
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    media = (n1 * 2 + n2 * 3 + n3 * 5) / (2 + 3 + 5)
    medias.append(media)
for i in medias:
    print(i)