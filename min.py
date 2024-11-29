import random

def print_menu():
    pass

def input_matrix():
    n = int(input("Введите размер матрицы (n x n): "))
    matrix = []
    print("Введите элементы матрицы (через пробел):")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def generate_random_matrix(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

def swap_rows_and_columns(matrix):
    min_row_index = None
    max_col_index = None
    min_value = float('inf')
    max_value = float('-inf')

    # Поиск минимального элемента и максимального элемента
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_col_index = j
                
    # Замена местами строки и столбца
    if min_row_index is not None and max_col_index is not None:
        for i in range(len(matrix)):
            # Смена строки с минимальным элементом на соответствующий столбец
            matrix[min_row_index][i], matrix[i][max_col_index] = matrix[i][max_col_index], matrix[min_row_index][i]

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    pass
if __name__ == "__main__":
    main()
