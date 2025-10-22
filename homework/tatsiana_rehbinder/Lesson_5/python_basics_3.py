# task1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name)
print(last_name)
print(city)
print(phone)
print(country)

# task2
line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"

colon_index = line1.index(':')
number_str = line1[colon_index + 1:]
number = int(number_str.strip()) + 10
print(number)

colon_index = line2.index(':')
number_str = line2[colon_index + 1:]
number = int(number_str.strip()) + 10
print(number)

colon_index = line3.index(':')
number_str = line3[colon_index + 1:]
number = int(number_str.strip()) + 10
print(number)

# task3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

my_text = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
print(my_text)
