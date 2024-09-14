names = ['Pavel', 'Jordan', 'Sasha']
new_name = input ('Введите новое имя: ')
names.append(new_name)
print(names)
name_to_delete = input( 'Введите имя для удаления: ')
if name_to_delete in names:
    names.remove(name_to_delete)
    print (names)
else:
    print( 'Такого имени нет!')
name_to_change = input ('Введите имя для изменения: ')
if name_to_change in names:
    change_name = input('введите измененное имя: ')
    names[names.index(name_to_change)] = change_name
    print(names)