while True:
 try:
  numero = int(input('Digite um numero: '))
  if numero % 2 == 0:
    print (f'O numero {numero} é par!')
  else:
    print (f'O numero {numero} é impar!')
    
  resposta = input('Deseja verificar outro número? (s/n)')
  if resposta.lower() == "n":
     print ('Volte sempre!')
     break
 except ValueError:
   print ('Digite um numero inteiro por favor!')