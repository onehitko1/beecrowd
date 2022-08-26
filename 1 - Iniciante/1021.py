n = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

if 0 <= n <= 1000000.00:
    print('NOTAS:')
    for i in notas:
        print('%.f nota(s) de R$ %.2f' % ((n//i), i))
        n %= i
    print('MOEDAS:')
    for i in moedas:
        print('%.f moeda(s) de R$ %.2f' % ((n//i), i))
        n %= i
else:
    exit()