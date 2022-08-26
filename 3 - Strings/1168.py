ntestes = int(input())
numeros = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
contador = 0

while contador < ntestes:
    n = str(input())
    nleds = 0
    contador+=1
    for i in n:
        if i in numeros.keys():
            nleds += numeros[i]
    print(str(nleds) + ' leds')