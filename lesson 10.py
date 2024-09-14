# b = lambda  y,u:y+u
# print((b(2,3)))
#
# a = lambda x:x**2
# print(a(10))
#
# x = lambda e:e
# print(x(9))
#
# x = lambda r:r*4
# print(x(6))
#
# x = lambda r:r*4
# side = int(input('введите сторону квадрата: '))
# print(x(side))
from operator import truediv


# def num(a,b):
#     return a+b
#
# print(num(5,9))

# def spammer(*args):
#     for a in args:
#         print(a)
#
# spammer(1,2,3,1,2,3,'4','hello')

# def spam1(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# print(spam1(name='my',age=23))

# def numbers():
#     side = int(input('введите сторону квадрата: '))
#
#     if numbers() in side % 2 != 0:
#         print('не четное')
#         print('четное')
#     else:
#         pass



# srok = 2
# print('я стал специалистом за {} месяца'.format(srok))
# print(f'я стал специалистом за {srok} месяца')
#
# if player1 == 'ножницы' and payer2 == 'камень':
#     print('gthdsq buhjr gj,tlbk')

# sarik = ['пизда', 'sosala', 'pizda', 'chlen']
#
# print(sarik[1])
# print(sarik[3])


# names = ['ewfh', 'ehwgf']
# name = input('введите свое имя: ')
# names.append(name)
# print(names)


# x = lambda r:r*4
# side = int(input('введите сторону квадрата: '))
# print(x(side))




# clients = {}
# opened_rooms = [i for i in range(1, 41)]
# closed_rooms = []
#
# # Добавление клиента
# def add_client(name, room):
#     clients[name] = room
#     opened_rooms.remove(room)
#     closed_rooms.append(room)
#
# # Выселение клиента
# def del_client(name):
#     closed_rooms.remove(clients[name])
#     opened_rooms.append(clients[name])
#     clients.pop(name)
#
# # Список занятых номеров
# def show_rooms():
#     return closed_rooms
#
# while True:
#     choice = input('Введите действие: ')
#
#
#     if choice.lower() == 'добавить':
#         cl_name = input('Имя клиента: ')
#         print('Доступные номера:', opened_rooms)
#         cl_room = int(input('Выберите номер: '))
#         if cl_room in opened_rooms:
#             add_client(cl_name, cl_room)
#             print('Клиенты:', clients)
#         else:
#             print('Выбранный номер недоступен.')
#     elif choice.lower() == 'выселить':
#         cl_name = input('Имя клиента: ')
#         if cl_name in clients:
#             del_client(cl_name)
#             print('Клиенты:', clients)
#         else:
#             print('Такого клиента нет!')
#     elif choice.lower() == 'номера':
#         print('Занятые номера:', show_rooms())
#     else:
#         print('Ошибка. Пожалуйста, выберите одно из доступных действий.')


sum_func = lambda x, y: x + y


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))


result = sum_func(num1, num2)
print(f"Сумма чисел: {result}")


class School:
    def init(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = {
            "name": name,
            "age": age,
            "grade": grade
        }
        self.students.append(student)
        print(f"Студент {name} был добавлен.")

    def remove_student(self, name):
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                print(f"Студент {name} был удалён.")
                return
        print(f"Студент с именем {name} не найден.")

    def display_students(self):
        if not self.students:
            print("В школе нет студентов.")
        else:
            for student in self.students:
                print(f"Имя: {student['name']}, Возраст: {student['age']}, Класс: {student['grade']}")



school = School()

school.add_student("Иван", 14, 8)
school.add_student("Мария", 15, 9)

school.display_students()

school.remove_student("Иван")

school.display_students()