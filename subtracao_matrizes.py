def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{val:.2f}" for val in row))

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(3):
        row = []
        for j in range(4):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Inicializando duas matrizes 3x4 com valores reais
matrix1 = [
    [1.0, 2.5, 3.3, 4.7],
    [5.2, 6.8, 7.1, 8.4],
    [9.0, 10.1, 11.5, 12.3]
]

matrix2 = [
    [0.5, 1.5, 2.3, 3.7],
    [4.2, 5.8, 6.0, 7.4],
    [8.0, 9.1, 10.5, 11.3]
]

# Subtraindo as matrizes
result_matrix = subtract_matrices(matrix1, matrix2)

# Imprimindo a matriz resultante
print("Resultado da subtração das matrizes:")
print_matrix(result_matrix)
