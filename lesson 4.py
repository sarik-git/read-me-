names = []
numbers = []
services = []

while True:
    polzovatel = input("Введите 'Имя', 'Номер' или 'Услуга' для добавления информации: ")

    if polzovatel == 'имя':
        name = input("Введите имя: ")
        names.append(name)
        print(f"Имя {name} добавлено")
        print(names)
    elif polzovatel == 'номер':
        number = input('введите комер: ')
        numbers.append(number)
        print(f'номер {number} добавлено')
        print(numbers)
    elif polzovatel == 'услуга':
        service = input('введите услугу')
        services.append(service)
        print(f'услуга {service} доюавлено')
        print(services)
    elif polzovatel == 'стоп':
        break
    else:
        print('неверный ввод')


