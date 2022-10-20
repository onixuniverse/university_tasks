# 7.21 Выберите самую высокую вершину из заданного словаря.


world_peaks = {
    "Чогори": 8611,
    "Чо-Ойю": 8188,
    "Нангапарбат": 8126,
    "Хималчули": 7893,
    "Нандадеви": 7816,
    "Джомолунгма (Эверест)": 8848,
    "Жанну": 7711,
    "Чонгтар": 7315,
    "Пик Победы": 7439
}


def find_highest_peak(peaks: dict):
    peaks_list = list(peaks.items())

    highest_peak = ("", 0)
    for elem in peaks_list:
        if elem[1] > highest_peak[1]:
            highest_peak = elem

    return highest_peak


if __name__ == "__main__":
    try:
        result = find_highest_peak(world_peaks)
        print(f"{result[0]} - {result[1]}м")
    except Exception as exc:
        print("Произошла ошибка...", exc)
