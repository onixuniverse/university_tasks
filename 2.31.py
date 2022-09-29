from string import punctuation


def search(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    for symbol in punctuation:
        str1 = str1.replace(symbol, "")
        str2 = str2.replace(symbol, "")

    split_str1 = str1.split()
    count = 0

    for word in split_str1:
        if word in str2:
            count += 1

    return count


if __name__ == "__main__":
    while True:
        main_string = input("Введите строку 1: ")
        sub_string = input("Введите строку 2: ")

        print(f"Количество вхождений: {search(main_string, sub_string)}\n")


