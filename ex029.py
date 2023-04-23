while True:
 try:
  velocidade = int(input('Digite a velocidade do carro: '))
  if velocidade > 80:
    multa = (velocidade - 80) * 7
    print (f'O carro ultrapassou o limite de velocidade e foi multado em R${multa}!')
  else:
   print ('O carro esta no limite de velocidade e não foi multado.')
  break
 except ValueError:
   print ('Por favor digite um número inteiro para a velocidade!')