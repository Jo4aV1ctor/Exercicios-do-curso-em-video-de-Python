dias_alugados = int(input(
'Quantos dias o carro foi alugado?'
))
km = float(input(
  'quantos km o carro rodou?'
 ))
pago = (dias_alugados * 60) + (km *0.15)
print (f'Como o carro rodou {km:2.3f} e foi alugado por {dias_alugados:2.0f} dias, o total a pagar é {pago:2.2f}')