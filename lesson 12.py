# class Animal:
#     def make_sound(self,s):
#         print(s)
#
# class Hourse(Animal):
#     def galop(self):
#         print('бежит галопом')
#
#
# Pony = Hourse()
# Pony.make_sound('igogo')


# class Parents:
#     def glaza(self):
#         print('вижу')
#
# class malish(Parents):
#     def nogi(self):
#         print('играет футбол')
#
# sin = malish()


# class Car:
#     def __init__(self,model,color,year):
#         self.mode=model
#         self.color=color
#         self.year=year
#
#
# class Supercar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model,color,year)
#         self.sponsor=sponsor
#
# clk = Supercar('clk GTR',"silver",1989,'mersedes')
# print(vars(clk))
#

# class Myclass:
#     def __init__(self,value):
#         self.value=value
#
#     @classmethod
#     def from_string(cls,string):
#         return cls(int(string))
#
# my_obj = Myclass.from_string('3')
# print(my_obj.value)
#
#
#
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# qwe = Rectangle(4, 5)
# print(qwe.area)
#
#
# qwe.width = 6
# print(qwe.area)


# class Worker:
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
#
# class HR(Worker):
#     def __init__(self,name,position):
#       super().__init__(name,position)
#
#     def show_position(self,worker):
#       return worker.posion
# jordan = Worker('jordan','middle dev')
# pavel = HR ('pavel','HR')
# print(pavel.show_position(jordan))



# class Player:
#     def __init__(self,sila,tochnost,skorost,vinoslivost):
#         self.sila = sila
#         self.toschnost = tochnost
#         self.skorost = skorost
#         self.vinoslivost = vinoslivost
#
#
# class Napadaushiy(Player):
#     def __init__(self,sila,tochnost,skorost,vinoslivost,goal):
#         super().__init__(sila,tochnost,skorost,vinoslivost)
#         self.goal = goal
#
# class zashitnik(Player):
#     def __init__(self,sila,tochnost,skorost,vinoslivost,xrabrost):
#         super().__init__(sila,tochnost,skorost,vinoslivost)
#         self.xrabrost = xrabrost
#
# class poluzashitnik(Player):
#     def __init__(self,sila,tochnost,skorost,vinoslivost,meshdu):
#         super().__init__(sila,tochnost,skorost,vinoslivost)
#         self.meshdu = meshdu
#
# class goalkeeper(Player):
#     def __init__(self,sila,tochnost,skorost,vinoslivost,zashita):
#         super().__init__(sila,tochnost,skorost,vinoslivost)
#         self.zashita = zashita
#
#


# class Player:
#     def __init__(self, power, speed, accuracy, stamina):
#         self.power = power
#         self.speed = speed
#         self.accuracy = accuracy
#         self.stamina = stamina
#
#
# class Forward(Player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().init(power, speed, accuracy, stamina)
#
#     def make_goal(self):
#         print('Забил гол')
#
#
# class Goalkeeper(Player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().init(power, speed, accuracy, stamina)
#
#     def save(self):
#         print('Поймал мяч')
#
#
# class Defender(Player):
#     def __init__(self, power, speed, accuracy, stamina):
#         super().init(power, speed, accuracy, stamina)
#
#     def prevent_goal(self):
#         print('Защитил ворота')
#
#
# class Half_Defender(Player):
#     def (self, power, speed, accuracy, stamina):
#         super().init(power, speed, accuracy, stamina)
#
#     def tackle(self):
#         print('Отобрал мяч')



class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
     def make_sound(self):
                return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
                return "Мяу!"
class Cow(Animal):
     def make_sound(self):
                return "Муу!"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Марка:", self.brand, "Год выпуска:", self.year)



class Car(Vehicle):
    def __init__(self, brand, year, cost):
        super().init(brand, year)
        self.cost = cost

    def display_info(self):
        super().display_info()
        print("Цена автомобиля:", self.cost)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_type):
        super().init(brand, year)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print("Тип двигателя:", self.engine_type)


car = Car("Toyota", 2020, 20.000,)
motorcycle = Motorcycle("Harley-Davidson", 2018, "V-twin")


car.display_info()
motorcycle.display_info()


