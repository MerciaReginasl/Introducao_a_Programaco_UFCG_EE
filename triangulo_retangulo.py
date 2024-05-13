 # Solicita ao usuário para inserir o comprimento da base e da altura
    base = float(input("Insira o comprimento da base do triângulo: "))
    altura = float(input("Insira a altura do triângulo: "))

    # Chama a função para calcular a área
    area = calcular_area(base, altura)

    # Imprime a área do triângulo
    print("A área do triângulo é:", area)

# Chamada da função principal
if __name__ == "__main__":
    main()
