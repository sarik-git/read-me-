# class car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('машина остановилась')
#
#
# chevrolet = car('jentra','black', '2021')
# print(vars(chevrolet))
# chevrolet.stop()
from main import new_name


# class Comment:
#     def __init__(self,username,text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#
# user = Comment('sarik','privet',)
# print(vars(user))


# class bank_account:
#     def __init__(self,deposit,cash,balance=0):
#         self.deposit = deposit
#         self.cash = cash
#         self.balance = balance
#
#     def deposit(self):
#         dep =int(input('введите сумму для заполнения'))                 #не правильно
#         self.deposit+=dep
#
#     def cash(self):
#         cas =int(input('введите сумму для вывода средств'))
#         self.deposit-=cas
#
#     def balance(self):
#         bal =int(input('ваш баланс'))
#         self.balance
# sasha = bank_account('sasha')
# print(vars(sasha))



# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.balance = balance
#         self.name = name
#
#
#     def deposit(self, cash_amount):
#         self.balance += cash_amount
#
#
#     def cash(self, cash_amount):
#         self.balance -= cash_amount
#
#
#     def my_balance(self):
#         return self.balance
#
# sasha = BankAccount()
# print(sasha.my_balance())
# sasha.deposit(10)
# print(sasha.my_balance())
# sasha.cash(6)
# print(sasha.my_balance())


# class User:
#     def __init__(self,name,Gmail,age,phone_number):
#         self.name = name
#         self.Gmail = Gmail
#         self.age = age
#         self.phone_number = phone_number
#
#     def change_name(self):
#         new_name = input('поменять имя: ')                       не правильно
#         name = new_name
#
#     def change_phone_number(self):
#         new_phone_number = input('поменять телефон: ')
#         phone_number = new_phone_number
#
#     def change_Gmail(self):
#         new_Gmail = input('поменять почту: ')
#         Gmail = new_Gmail
#
#
# print(vars(changed_user))


#
# class User:
#     def init(self, name, mail, age, tel_number):
#         self.name = name
#         self.mail = mail
#         self.age = age
#         self.tel_number = tel_number
#
#
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#
#     def change_number(self, new_number):
#         self.number = new_number
#
#
#     def change_mail(self, new_mail):
#         self.mail = new_mail
#
#
# pasha = User('pavel','pa@ock','23','+998903211111')
# print(pasha.name)
# name_change = input('введите новое имя: ')
# pasha.change_name(name_change)
# print(pasha.name)
#
#











# class math:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#
#     def addition(self, a ,b):
#         return a+b


# safhfj=math()
# print(safhfj.addition(3,6))



class Math:
    def __init__(self,a, b):
        self.a

        # class math:
        #     def __init__(self, a, b):
        #         self.a = a
        #         self.b = b
        #
        #     def addition(self, a=0, b=0):
        #         return a + b
        #
        #  print(math.addition(4, 7))


