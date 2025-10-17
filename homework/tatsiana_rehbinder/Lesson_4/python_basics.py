my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [5, 10, 15, 20, 25],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {50, 100, 150, 200, 250}
}

print(my_dict['tuple'][-1])
# выведите на экран последний элемент

my_dict['list'].append(30)
# добавьте в конец списка еще один элемент

my_dict['list'].pop(1)
# удалите второй элемент списка

my_dict['dict'][('i am a tuple',)] = 11
# добавьте элемент с ключом ('i am a tuple',) и любым значением

my_dict['dict'].pop('c')
# удалите какой-нибудь элемент

my_dict['set'].add(300)
# добавьте новый элемент в множество

my_dict['set'].remove(100)
# удалите элемент из множества

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
