salario = float(input('Digite o valor do salário: '))
aumento = salario + (salario * 15 / 100)
print(
  f'Como o salário atual é de R${salario:2.2f} com 15% de aumento o valor do novo salário é de R${aumento:2.2f}!'
)
