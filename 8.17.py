# 8.17 Даны символьные файлы f и g. Определить, совпадают ли компоненты файла f с компонентами файла g. Если нет,
# то получить номер первой компоненты, в которой файлы f и g отличаются между собой. В случае, когда один из файлов
# имеет n компонент (n>=0) и повторяет начало другого (более длинного) файла, ответом должно быть число n+1.
from utils import read_files


def verify_texts(*args):
    f_text, g_text = args[0], args[1]

    max_length = len(f_text) if len(f_text) > len(g_text) else len(g_text)
    mismatched_component = 0

    for i in range(max_length):
        try:
            if f_text[i] != g_text[i]:
                mismatched_component = i + 1
                break
        except IndexError:
            mismatched_component = i + 1
            break
    if mismatched_component == 0:
        return "Компоненты совпадают в обоих файлах."

    return mismatched_component


if __name__ == "__main__":
    try:
        texts = read_files(["f.txt", "g.txt"])
        first_text, second_text = texts[0], texts[1]

        result = verify_texts(first_text, second_text)
        print(result)

    except Exception as exc:
        print("Произошла ошибка:", exc)
