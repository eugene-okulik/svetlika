# task1
def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("finished")

    return wrapper


@finish_me
def example(text):
    print(text)


example("print me")


# task2
def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop("count", 1)

        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me", count=2)

# task3
def smart_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, lambda x, y: x * y)

        if first == second:
            return func(first, second, lambda x, y: x + y)

        if first > second:
            return func(first, second, lambda x, y: x - y)

        return func(first, second, lambda x, y: x / y)

    return wrapper


@smart_operation
def calc(first, second, operation):
    return operation(first, second)


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Результат:", calc(a, b))

# task4
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in PRICE_LIST.split('\n')}

print(price_dict)
