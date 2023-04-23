import math 
cateto_oposto = float (input(
  'Digite o valor do cateto oposto:' 
))
cateto_adjacente = float (input(
  'Digite o valor do cateto adjacente: '
 ))
hipotenuza = math.sqrt(
cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente)
print (f'O cateto oposto vale {cateto_oposto}\nO cateto adjacente vale {cateto_adjacente}\nPortanto a hipotenusa é {hipotenuza:2.2f}.')