name = str(input())
salario = float(input())
vendas = float(input())

comissao = (15*vendas)/100
salario_total = salario + comissao

print('TOTAL = R$ %.2f' % salario_total)