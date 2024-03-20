"""

def no Python é uma estrutura fundamental na programação dessa linguagem. 
Ela é utilizada para agrupar um conjunto de instruções em um bloco, 
permitindo que esse bloco seja executado quantas vezes forem necessárias.

"""

"""

return - retorna o valor da função.

"""

#def soma(parametro_1, parametro_2):
def menor_de_2(parametro_1, parametro_2):
"""

Função que soma dois valores e retorna o resultado.

"""

	return parametro_1 + parametro_2

#Programa para soma quatro valores reais

val_1 = float(input("Informe o primeiro valor a somar: "))
val_2 = float(input("Informe o segundo valor a somar: "))
val_3 = float(input("Informe o terceiro valor a somar: "))
val_4 = float(input("Informe o quarto valor a somar: "))

#print(f"Soma = {soma(val_1, soma(val_2, soma(val_3, val_4)))}")
print(f "Menor = {menor_de_2(val_1, menor_de_2(val_2, menor_de_2(val_3, val_4)))}")
