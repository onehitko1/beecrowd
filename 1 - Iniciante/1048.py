salario = float(input())

if salario < 0:
    print('Digite um salario válido.')

elif salario >=0 and salario <= 400:
    percentual = (salario / 100) * 15
    novo_salario = salario + percentual
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {percentual:.2f}')
    print('Em percentual: 15 %')

elif salario > 400 and salario <= 800:
    percentual = (salario / 100) * 12
    novo_salario = salario + percentual
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {percentual:.2f}')
    print(f'Em percentual: 12 %')

elif salario > 800 and salario <=1200:
    percentual = (salario / 100) * 10
    novo_salario = salario + percentual
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {percentual:.2f}')
    print(f'Em percentual: 10 %')

elif salario > 1200 and salario <= 2000:
    percentual = (salario / 100) * 7
    novo_salario = salario + percentual
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {percentual:.2f}')
    print(f'Em percentual: 7 %')

else:
    percentual = (salario / 100) * 4
    novo_salario = salario + percentual
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {percentual:.2f}')
    print(f'Em percentual: 4 %')