a, b, c = map(float, input().split())

triArea = (a*c)/2
circArea = 3.14159 * (c ** 2)
trapArea = ((a + b)/2) * c
quadArea = b ** 2
retArea = a * b

print('TRIANGULO: %.3f' % triArea)
print('CIRCULO: %.3f' % circArea)
print('TRAPEZIO: %.3f' % trapArea)
print('QUADRADO: %.3f' % quadArea)
print('RETANGULO: %.3f' % retArea)