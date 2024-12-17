# №3
import random


def read_f(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip().split('; ') for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return []


def generation(phrases, count):
    sentences = []
    for _ in range(count):
        sentence = f"{random.choice(phrases[0])} {random.choice(phrases[1])} {random.choice(phrases[2])} {random.choice(phrases[3])}"
        sentences.append(sentence)
    return sentences


def write_f(sentences, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        if file.tell() > 0:
            file.write('\n')
        file.write('\n'.join(sentences))


input_file = '3.phrases.txt'
output_file = 'result_phrases.txt'
phrases = read_f(input_file)
while True:
    try:
        count = int(input("Сколько предложений сгенерировать?: "))
        if count < 0:
            raise ValueError("Количество предложений не может быть отрицательным.")
        sentences = generation(phrases, count)
        write_f(sentences, output_file)
        print(f"Сгенерированные предложения записаны в файл {output_file}.")
        cont = input("Хотите продолжить генерацию текста? (Да/Нет): ")
        if cont.lower() == 'нет':
            break
        else:
            continue
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
