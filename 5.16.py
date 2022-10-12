# 5.16 Сгенерировать десять списков из случайных чисел. Вывести их и сумму их элементов на экран. Найти среди них
# один с максимальной суммой элементов. Указать какой он по счету, повторно вывести этот список и сумму его
# элементов. Заполнение списка и подсчет суммы его элементов оформить в виде отдельных функций (стандартную функцию
# подсчета суммы элементов списка использовать нельзя).
from random import randint


def sum_of_list(lst: list):
    result = 0

    for num in lst:
        result += num

    return result


def create_matrix(n: int):
    matrix = [[randint(-100, 100) for _ in range(10)] for _ in range(n)]

    return matrix


def find_max_lst(count: int):
    matrix = create_matrix(count)
    amounts = [sum_of_list(lst) for lst in matrix]

    for lst in matrix:
        print(f"list: {lst} sum: {sum_of_list(lst)}")

    max_sum = max(amounts)
    max_sum_index = amounts.index(max_sum)
    max_lst = matrix[max_sum_index]

    print(f"\npos: {max_sum_index + 1} list: {max_lst} sum: {max_sum}")


if __name__ == "__main__":
    try:
        find_max_lst(10)
    except Exception as exc:
        print(f"Произошла ошибка! {exc}")
