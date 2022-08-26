valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for i in notas:
    print(str(valor//i) + ' nota(s) de R$ ' + str(i) + ',00')
    valor %= i
