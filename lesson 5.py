usernames = []

while True:
    user = input("Введите username: ")
    usernames.append(user)
    print('user dobavlen')

    if user in usernames:
        print('занят ')



