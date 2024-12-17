import random

def print_stones(n):
    print("Осталось камней: ", n)


def player_turn(n):
    while True:
        stones = input("Сколько камней вы хотите взять (1, 2 или 3)? ")
        try:
            stones = int(stones)
            if stones in [1, 2, 3] and stones <= n:
                return stones
            else:
                print("Недопустимое количество камней. Попробуйте еще раз.")
        except ValueError:
            print("Пожалуйста, введите число.")


def computer_turn(n):
    stones = random.randint(1, min(3, n))
    print(f"Компьютер берет {stones} камней.")
    return stones


def main():
    n = random.randint(4, 30)
    while n > 0:
        print_stones(n)


        n -= player_turn(n)
        if n <= 0:
            print("Вы выиграли! ♡(⌒▽⌒)♡")
            break

        n -= computer_turn(n)
        if n <= 0:
            print("Компьютер выиграл! (ಥ﹏ಥ)")



main()
