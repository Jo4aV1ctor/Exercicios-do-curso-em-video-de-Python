try:
  numero = int (input('Digite um numero: '))
  if numero > 9999 or numero < 0:
     print('Digite um número entre 0 e 9999!')
  else:
     unidade = numero % 10
     dezena = (numero // 10 ) % 10
     centena = (numero // 100) % 10
     milhar = (numero // 1000) % 10
  print (f'A unidade desse número é: {unidade}')
  print (f'A dezena desse número é: {dezena}')
  print (f'A centena desse número é: {centena}')
  print (f'O milhar desse número é: {milhar}')
except ValueError:
  print ('Digite um número valido!')
'''
num = int (input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print (f'Analisando o número {num}...')
print (f'Unidade: {u}')
print (f'Dezena: {d}')
print (f'Milhar: {c}')
print (f'Milhar: {m}')
'''