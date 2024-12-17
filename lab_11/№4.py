# №4
def read_f(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return []


def write_f(contents, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(contents))


def extract_contents(chapters):
    result = []
    current_chapter = ""
    current_subtitle = ""
    for line in chapters:
        line = line.strip()
        if line.startswith("Глава") or line.startswith("Chapter"):
            if current_chapter and current_subtitle:
                result.append(f"{current_chapter}. {current_subtitle.strip()}")
            current_chapter = line
            current_subtitle = ""
        elif line and not current_subtitle:
            current_subtitle = line
    if current_chapter and current_subtitle:
        result.append(f"{current_chapter}. {current_subtitle.strip()}")
    return result


input_file = '4.chapters.txt'
output_file = 'result_chapters.txt'
chapters = read_f(input_file)
contents = extract_contents(chapters)
write_f(contents, output_file)
print(f"Оглавление записано в файл {output_file}.")