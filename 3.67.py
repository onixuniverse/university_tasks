# 3.67 Для списка целых чисел вычислить произведение первого, третьего и шестого положительных элементов и
# определить их номера в списке.

def find_multiply(arr: list):
    result = 1
    i = 0

    for num in arr:
        if num > 0:
            i += 1

            if i in (1, 3, 6):
                result *= num

    return result


if __name__ == "__main__":
    while True:
        try:
            input_text = "Пример последовательности: 1 -1 0 12 24 -11 15\n" \
                         "Введите последовательность целых чисел: "
            seq = list(map(int, list(input(input_text).split())))

            print(find_multiply(seq))
        except ValueError:
            print("Неверная последовательность!\n")
