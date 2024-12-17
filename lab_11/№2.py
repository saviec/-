import re
def read_f(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return ""


def write_f(sentences, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sentences))

def filter_sentences(text, min_word_count):
    sentences = re.split(r'(?<=[.!?]) +', text)
    filtered = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > min_word_count:
            filtered.append(sentence.strip())
    return filtered


input_file = '2.text.txt'
output_file = 'result_filtered_text.txt'
try:
    min_word_count = int(input("Введите минимальное количество слов для фильтрации предложений: "))
    if min_word_count < 0:
        raise ValueError("Количество слов не может быть отрицательным.")
    text = read_f(input_file)
    filtered_sentences = filter_sentences(text, min_word_count)
    write_f(filtered_sentences, output_file)
    print(f"Фильтрованные предложения записаны в файл {output_file}.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
