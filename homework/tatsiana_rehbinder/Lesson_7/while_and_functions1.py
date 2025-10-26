secret_number = 9

while True:
    guess = int(input("Угадайте число от 1 до 20: "))
    if guess == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова!")
