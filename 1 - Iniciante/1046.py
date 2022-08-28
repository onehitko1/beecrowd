a, b = map(int, input().split())

if(a < b):
    duracao_jogo = b - a
else:
    duracao_jogo = b + 24 - a
print(f"O JOGO DUROU {duracao_jogo} HORA(S)")