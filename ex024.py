cidade = input('Digite o nome da cidade: ').strip()
cidade_sem_espaço = cidade.replace(' ','')
cidade_que_aparece = cidade.title()
if cidade_sem_espaço.lower().startswith('santo'):
  print (f'A cidade "{cidade_que_aparece}" começa com a palavra "santo"')
else:
  print(f'A cidade "{cidade_que_aparece}" não começa com a palavra "santo"')
  
'''
cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
'''