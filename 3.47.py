# 3.47 Дано натуральное число n>=2, список списков, состоящий из n элементов по n чисел в элементе. Построить список,
# состоящий из n элементов, каждый из которых является максимальным среди элементов списков с соответствующим
# номером. Пример: дан список [[1,2,3], [4,7,2],[0,-7,1]]. Результат: [4,7,3].
from random import randint


def create_list(end_point):
    matrix = []

    for _ in range(end_point):
        matrix.append([randint(-100, 100) for _ in range(end_point)])

    return matrix


def find_max_array(matrix, end_point):
    i = 0
    res = []

    while i != end_point:
        max_arr = []

        for arr in matrix:
            max_arr.append(arr[i])

        res.append(max(max_arr))
        i += 1

    return res


if __name__ == "__main__":
    try:
        n = int(input("Введите натуральное N: "))

        if n >= 2:

            mat = create_list(n)
            print(mat)

            result = find_max_array(mat, n)
            print(result)
        else:
            raise ValueError
    except Exception:
        print("Произошла ошибка...")
