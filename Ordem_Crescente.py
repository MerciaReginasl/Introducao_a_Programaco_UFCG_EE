'''
Faça um programa que leia valores para duas variáveis e mostre estas duas variáveis com os valores
em ordem crescente.
'''

print("\n")

primeira = int(input("Informe o valor da primeira variável: "))
segunda = int(input("Informe o valor da segunda variável: "))

if primeira > segunda:
	
	##auxiliar = primeira
	##primeira = segunda
	##segunda = auxiliar
	
	'''
	Também pode ser inscrito desta forma:
	'''
	
	primeira, segunda = segunda, primeira
	

print(f"Variável_1 = {primeira} e Variável_2 = {segunda}")
