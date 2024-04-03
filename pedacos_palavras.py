#Faça um programa que leia uma frase e mostre as palavras que a compõe.
#Uma em cada linha de saída

pedacos = input("Digite uma frase com suas palavras separadas por espaços:").split(" ")
print(pedacos)
for indice in range(0, len(pedacos), 1):
	print(pedacos[indice])
