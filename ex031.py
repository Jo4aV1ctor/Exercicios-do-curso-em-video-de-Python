while True:
  try:
   km = float(input('Digite a distancia da viagem: '))
   if km < 200:
    km_rodados = km * 0.50
    print (f'Como a viagem vai ser de {km}km vai custar somente R${km_rodados:2.2f}!')
   else:
    km_rodados2 = km * 0.45
    print (f'Como a viagem vai ser de {km}km vai custar apenas R${km_rodados2:2.2f}!')
    resposta = input ('Deseja verificar outra viagem? (s/n)')
    if resposta.lower() == "n":
      print('Certo, até a proxima vez!')
      break
  except ValueError:
   print ('Digite um numero valido por favor!')
  