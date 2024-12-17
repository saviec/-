def read_f(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(map(float, file.read().strip().split()))
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return []
    except ValueError:
        print("Ошибка: некорректные данные в файле.")
        return []


def remove(vector, count):
    if not isinstance(vector, list) or not all(isinstance(x, (int, float)) for x in vector):
        raise ValueError("Вектор должен быть списком чисел.")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Количество чисел для удаления должно быть неотрицательным целым числом.")
    if count == 0:
        return vector
    return vector[:-count] if count <= len(vector) else []


def write_f(vector, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, vector)))


input_file = '1.vector.txt'
output_file = 'result_vector.txt'
vector = read_f(input_file)
try:
    count_to_remove = int(input("Введите количество элементов для удаления: "))
    new_vector = remove(vector, count_to_remove)
    write_f(new_vector, output_file)
    print(f"Новый вектор записан в файл {output_file}.")
except ValueError as e:
    print(f"Ошибка: {e}")
