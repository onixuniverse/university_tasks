import sys

# test commit 
def sum_search():
    n = int(input("Введите целочисленное N: "))

    total_sum = 0

    for k in range(1, n + 1):
        total_sum += 2 * k / (3 * k**2 + k + 4)

    return total_sum


def members_of_series():
    e = float(input("Введите число E: "))
    k = 1
    while True:
        total = 2 * k / (3 * k**2 + k + 4)
        k += 1
        if total >= e:
            print(total)
        else:
            break


if __name__ == "__main__":
    while True:
        number_of_function = input("1 - вычисление суммы первых N членов\n"
                                   "2 - вычисление всех членов ряда, не меньших заданного числа E\n"
                                   "exit - выход из программы\n\n"
                                   "Введите номер программы: ")

        try:
            if number_of_function == "1":
                print(sum_search())
            elif number_of_function == "2":
                members_of_series()
            elif number_of_function == "exit":
                print("Завершение работы программы...")
                sys.exit()
            else:
                print("Программы под таким номером нет.")
        except Exception:
            print("Произошла ошибка. Рестарт...")
