# 4.20 Проверить введенную пользователем строку на наличие недопустимых символов. В качестве первого символа
# допустимы только буквы и знак подчеркивания. Остальные символы могут быть буквами, цифрами и знаком подчеркивания.

from string import ascii_letters, digits


def check_string(string: str):
    characters = ascii_letters + "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ_"
    invalid_chars = []

    if string[0] not in characters:
        invalid_chars.append(f"0 - \"{string[0]}\"")

    characters += digits

    for i in range(1, len(string)):
        if string[i] not in characters:
            invalid_chars.append(f"{i} - \"{string[i]}\"")

    if len(invalid_chars) > 0:
        invalid_result_str = f"В строке найдены недопустимые символы на позициях:\n" + "\n".join(invalid_chars)

        return invalid_result_str

    return "В строке не найдено недопустимых символов!"


if __name__ == "__main__":
    while True:
        try:
            user_input = input()

            result = check_string(user_input)
            print(result)
        except Exception:
            print("Произошла ошибка!")

