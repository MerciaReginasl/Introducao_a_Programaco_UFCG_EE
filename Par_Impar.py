'''
Faça um programa que leia um valor inteiro positivo e mostre o seu valor lido se é par ou impar:
'''

print("\n")

numero = int(input("Informe um valor inteiro positivo: "))

if numero % 2 == 0:       '''% 2 informa que o número é um inteiro par!'''
	print(f"O número {numero} é par!")
	
else:
	print(f"O número {numero} é impar!")
