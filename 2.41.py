from string import ascii_uppercase


def change_string():
    original_string = "AtTimesYouMayWantToReadDataFromTheKeyBoard"
    original_string_arr = [i for i in original_string]

    for i in range(len(original_string_arr)):
        if original_string_arr[i] in ascii_uppercase:
            original_string_arr[i] = " " + original_string[i]

    print("".join(original_string_arr)[1:])


if __name__ == "__main__":
    change_string()
