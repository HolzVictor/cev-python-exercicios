casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Pagar pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de {prestação:.2f}
if prestação <= mínimo:
      print('Empréstimo pode ser CONCEDIDO!')
else:
      print('Empréstimo NEGADO!')
