# task1
import random
import sys

salary = int(input("Введите вашу зарплату: "))
bonus = random.choice([True, False])

if bonus:
    salary += random.randrange(100, 5001)

print(f"${salary}")
print(f"Bonus applied: {bonus}")

# task2
sys.set_int_max_str_digits(1_000_000)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

positions = [5, 200, 1000, 100_000]

results = {}
index = 0

for num in fib:
    index += 1
    if index in positions:
        results[index] = num
        if len(results) == len(positions):
            break

for pos in positions:
    num_str = str(results[pos])
    print(f"{pos}-е число Фибоначчи имеет {len(num_str)} цифр")
