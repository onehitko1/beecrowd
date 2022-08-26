    x1, y1 = input().split()
    x2, y2 = input().split()

    distancia = pow(((float(x2) - float(x1))*(float(x2) - float(x1)) + ((float(y2) - float(y1))*(float(y2) - float(y1)))), 0.5)

    print('%.4f' % distancia)
