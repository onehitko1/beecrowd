n1, n2, n3, n4 = map(float, input().split())
media = (float(n1)*2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1)/10

print('Media: %.1f' % media)
if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    nota2 = float(input())
    print('Nota do exame: %.1f' % nota2)
    media_nova = (media + nota2)/2
    if media_nova >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' % media_nova)
    else:
        print('Aluno reprovado.')


