def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def sort_row_descending(row):
    row.sort(reverse=True)
    return row


def main():
    try:
        size = int(input('Введите размер квадратной матрицы: '))
        matrix = []

        for i in range(size):
            row = []
            for j in range(size):
                value = int(input(f'Введите значение в [{i}][{j}]: '))
                row.append(value)
            matrix.append(row)

        print('\nИсходная матрица:')
        print_matrix(matrix)

        row_num = int(input('\nВведите № строки для сортировки (от 1 до {size}): '))
        if 1 <= row_num <= size:
            sort_row_descending(matrix[row_num - 1])

            print('\nМатрица с отсортированной строкой:')
            print_matrix(matrix)
        else:
            print('Некорректный номер строки!')

    except ValueError:
        print('Ошибка: введены некорректные данные!')


if __name__ == "__main__":
    main()
