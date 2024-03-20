'''

Faça um programa que mostre a soma dos fatoriais de dois números naturais.
O programa usará uma função fatorial que recebe um número natural e retorna 
seu fatorial

'''

def fatorial(natural):
	fat = 1
	for fator in range (1, natural+1, 1):
		fat *= fatorial
	return fat
	
nat1 = int(input("Informe um número natural: "))
nat2 = int(input("Informe um número natural: "))

print(f"A soma dos fatorais de {nat1} e {nat2} é {fatorial(nat1)+fatorial(nat2)}")
