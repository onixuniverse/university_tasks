# 3.55 В заданном списке, состоящем из целых чисел, вычислить сумму модулей элементов списка, расположенных после
# первого отрицательного элемента.

def find_sum_of_abs(arr: list):
    negative_number_index = -1

    for i in arr:
        if i < 0:
            negative_number_index = arr.index(i)
            break

    sum_of_abs = sum([abs(arr[i]) for i in range(negative_number_index + 1, len(arr))]) \
        if negative_number_index != -1 else 0

    return sum_of_abs


if __name__ == "__main__":
    while True:
        try:
            input_text = "Пример последовательности: 1 -1 0 -11 -33\nВведите последовательность целых чисел: "
            seq = list(map(int, list(input(input_text).split())))

            print(find_sum_of_abs(seq))
        except ValueError:
            print("Неверная последовательность!\n")
