hI, mI, hF, mF = map(int, input().split())

minuto_total = mF - mI
hora_total = hF - hI

if minuto_total < 0:
	minuto_total += 60
	hora_total -= 1

if hora_total < 0:
    hora_total += 24

if hora_total == 0 and minuto_total == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)')