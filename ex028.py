import random

jogando = True

while jogando:
  numero_aleatorio = random.randint(1, 5)
  try:
      chute = int(input('Digite um número entre 1 e 5: '))
      if chute == numero_aleatorio:
       print('Parabéns, você acertou!')
      else:
       print(f'Você errou, o número correto era {numero_aleatorio}')
       resposta = "" 
       while resposta not in ["s", "n"]:
        resposta = input('Deseja continuar o jogo? s/n: ')
       if resposta == "n":
         jogando = False
  except ValueError:
    print ('Por favor digite um numero inteiro!')
  
print ('Obrigado por jogar!')
