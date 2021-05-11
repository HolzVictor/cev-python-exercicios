n1 = float(input('Qual é o salário do funcionário? R$'))
aumento  = n1 + (n1 * 15 / 100)
print(f'Um funcionário que ganhava R${n1}, com 15% de aumento, passa a receber R${aumento:.2f}.')
