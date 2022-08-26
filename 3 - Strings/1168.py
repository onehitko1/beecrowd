ntestes = int(input())
numeros = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}

contador = 0
while contador < ntestes:
    n = str(input())
    ledjoao = [int(i) for i in n] #separa cada número do input n em uma lista, exemplo: 123 = [1, 2, 3]
    nleds = 0
    contador+=1
    for i in range(len(ledjoao)):
        if ledjoao[i] in numeros:
            nleds += numeros[ledjoao[i]]
    print(str(nleds) + ' leds')