salario = float(input())

if salario < 0:
    print('Digite um salario válido.')

elif salario >=0 and salario <= 400:
    reajuste = (salario / 100) * 15
    novo_salario = salario + reajuste
    percentual = 15

elif salario > 400 and salario <= 800:
    reajuste = (salario / 100) * 12
    novo_salario = salario + reajuste
    percentual = 12

elif salario > 800 and salario <=1200:
    reajuste = (salario / 100) * 10
    novo_salario = salario + reajuste
    percentual = 10

elif salario > 1200 and salario <= 2000:
    reajuste = (salario / 100) * 7
    novo_salario = salario + reajuste
    percentual = 7

else:
    reajuste = (salario / 100) * 4
    novo_salario = salario + reajuste
    percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')