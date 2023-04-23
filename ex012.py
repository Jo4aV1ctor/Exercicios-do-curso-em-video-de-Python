preço = float(input('Digite a valor do produto R$: '))
desconto = preço - (preço * 5 / 100)
print(
  f'O produto custa {preço:2.2f}R$ ,com desconto de 5% seu novo preço vai ser {desconto:2.2f}!'
)
