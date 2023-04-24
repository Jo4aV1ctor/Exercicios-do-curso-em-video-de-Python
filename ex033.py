while True:
  try:
   lista = []
   limite = 3
   for i in range(limite):
     numero = int(input('Digite um numero: '))
     lista.append(numero)
   numero_maior = max(lista)
   numero_menor = min(lista)
  print(f'O maior numero é o {numero_maior}!\nE o menor numero é o {numero_menor}!')
 resposta = input('Gostaria de verificar outros numeros? (s/n)')
    if resposta == "n":
        break
  except ValueError:
    print('Por favor digite um numero valido!')

'''
while True:
    try:
        lista = []
        limite = 3
        for i in range(limite):
            numero = int(input('Digite um numero: '))
            lista.append(numero)
        numero_maior = max(lista)
        numero_menor = min(lista)
        print(f'O maior numero é o {numero_maior}!\nE o menor numero é o {numero_menor}!')
        resposta = input('Gostaria de verificar outros numeros? (s/n)')
        if resposta == "n":
            break
    except ValueError:
        print('Por favor, digite um número válido!')
'''