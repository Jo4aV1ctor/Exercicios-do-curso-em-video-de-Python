'''nome = str(input(('Digite um nome: '))).strip()
palavra = "silva"
if palavra.lower() in nome.lower():
  print (f'O nome "{nome}" tem "silva" no nome.')
else:
  print (f'O nome "{nome}" não tem "silva" no nome.')'''
nome = str(input('Qual seu nome completo?')).strip()
print ('Seu nom tem silva? {}'.format('silva' in nome.lower()))