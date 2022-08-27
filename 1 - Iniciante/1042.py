a, b, c = map(int, input().split())

lista = [a, b, c]
lista.sort()
for i in lista:
    print(i)
print()
print(a, b, c, sep='\n')