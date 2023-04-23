#Exemplo de conversor de moedas (incompleto)
'''print ('Moedas disponiveis para conversão: \nFranco Suíço CHF1 = R$5,53\nDólar Australiano AUD1 = R$3,39\nIene ¥1 = R$0,038\nLibra esterlina £1 = R$6,25\nEuro €1 = R$5,50\nDólar americano US$1 = R$5,06')
moeda = float( input ('Escolha a moeda que deseja converter: '))
print('Exemplo: Real para dolar')'''
print('1 Dolar = 5,06R eais')
moeda = float(input('Digite o valor que possui na carteira:'))
dolar = 5.06
resultado = moeda * dolar
print(
  f'Como você possui {moeda:2.2f} reais, você pode comprar {dolar:2.2f} dolares!'
)
