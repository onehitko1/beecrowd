a, b, c = map(float, input().split())

if a == 0 or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print('R1 = %.5f\nR2 = %.5f' % (x1, x2))