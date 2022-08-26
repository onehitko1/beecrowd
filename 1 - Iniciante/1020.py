idadeDias = int(input())

anos = idadeDias // 365

meses = (idadeDias % 365) // 30

dias = (idadeDias % 365) % 30

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')