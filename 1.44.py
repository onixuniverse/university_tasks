# 1.44 Дана последовательность чисел, состоящих только из цифр 0 и 5, в порядке возрастания: 0 5 50 55 500 505 5000
# 5005 5050 и так далее. Найти k-ое по порядку в этой последовательности число.


def number_find(k):
    i = 0
    for i in range(0, k+1):
        num = bin(i)[2:].replace("1", "5")
        i += 1
        if i == k:
            return num


if __name__ == "__main__":
    while True:
        try:
            k = int(input("Введите натуральное число: "))
            if k > 0:
                print(number_find(k))
            else:
                raise ValueError
        except Exception:
            print("Произошла ошибка...")
