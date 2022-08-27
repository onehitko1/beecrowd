cod, quant = map(int, input().split())

cods = {1: 'Cachorro Quente', 2: 'X-Salada', 3: 'X-Bacon', 4: 'Torrada simples', 5: 'Refrigerante'}
especificacao = {cods[1]: 4, cods[2]: 4.5, cods[3]: 5, cods[4]: 2, cods[5]: 1.5}

if cod in cods:
    especificacao[cods[cod]] *= quant
    print(f'Total: R$ {especificacao[cods[cod]]:.2f}')
else:
    print('Digite um código válido.')