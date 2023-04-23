frase = input('Digite uma frase: ')
letra = "a"
contagem = frase.count(letra)
primeira = frase.find(letra)
ultima = frase.rfind(letra)
print (f"A letra '{letra}' aparece {contagem} vezes na frase.\nA letra '{letra}' aparece a primeira vez no índice {primeira} e na última no índice {ultima}. ")
