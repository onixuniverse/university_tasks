# 6.16 Есть текст со списками цен. Извлечь из него цены в USD, RUR, EU. Примеры правильных выражений: 23.78 USD.
# Примеры неправильных выражений: 22 USD, 0.002 USD.
import re


def get_prices(text: str):
    entry = re.findall(r"[0-9]{1,2}.[0-9]{1,2}", text)
    return entry


if __name__ == "__main__":
    try:
        input_text = "23.78 USD 4500 RUR 4.76 EU 0.0001 USD 20 RUB 0.01 RUR"

        result = get_prices(input_text)

        for el in result:
            if float(el) != 0:
                print(el)

    except Exception as exc:
        print("Произошла ошибка...", exc)
