def read_files(file_paths: list[str]):
    """Returns the texts of given files"""
    file_texts = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            file_texts.append(file.read())

    return file_texts
