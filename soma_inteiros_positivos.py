'''Faça um programa que mostre a soma dos digitos de 10 números inteiros positivos'''

contador = 1

while contador <= 10:
	numero = int(input("Informe um inteiro positivo: "))
	copia = numero
	soma = 0
	while numero > 0:
		soma += numero % 10
		numero //= 10
	print(f"A soma dos digitos do número {copia} é {soma}")
	
	contador += 1
	
print("Fim do programa!")
