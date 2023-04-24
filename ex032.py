while True:
 try: 
    ano = int(input('Digite um ano qualquer: '))
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
     print (f'O ano de {ano} é bissexto!')
    else:
     print (f'O ano de {ano} não é bissexto!')
    resposta = str(input ('Gostaria de verificar outro numero? (s/n)'))
    if resposta.lower() == "n":
      print('Até a proxima vez!')
      break
 except ValueError:
    print ('Por favor digite um numero valido!(0,1,829...)')