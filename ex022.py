nome = str (input('Digite seu nome: '))
nome_sem_espaços = nome.replace(' ','')
nome_maiusculo = nome.upper()
print ('Analisando seu nome...')
print (f'Seu nome em maíusculo é "{nome_maiusculo}"')
nome_minusculo = nome.lower()
print (f'Seu nome em minúsculo é "{nome_minusculo}"')
nome_total = len(nome_sem_espaços.strip())
print (f'Ao todo seu nome tem {nome_total} letras' )
primeiro_nome = nome.split()[0]
primeiro_nome_total = len(primeiro_nome)
print (f'O primeiro nome tem {primeiro_nome_total} letras')

'''
nome = str(input('Digite seu nome completo: ')).strip()
print ('Analisando seu nome ...')
print (f'Seu nome em maíusculas é {nome.upper()}')
print (f'Seu nome em minúsculas é {nome.lower()}')
print ('Seu nome tem ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print ('Seu primerio nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print (f'Seu primeiro nome é "{separa[0]}" e ele tem {len(separa[0])} letras')
'''