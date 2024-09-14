all_products = {'Весь склад': {}}
korzina = []

while True:
    admin = input('Выберите действие: ')
    if admin.upper() == 'ДОБАВИТЬ':
        product_name = input('Введите название продукта:')
        product_count = int(input('Введите кол-во продукта: '))
        all_products['Весь склад'][product_name] = product_count
        print("Продукт добавлен!")
    elif admin.upper() == 'ПРОДУКТЫ':
        print(all_products)
    elif admin.upper() == 'КУПИТЬ':
        print(all_products)
        pr_name = input('Выберите продукт:')
        pr_count = int(input('Выберите количество продукта: '))
        if pr_name in all_products['Весь склад'] and all_products['Весь склад'][pr_name] >= pr_count:
            new_order = (pr_name, pr_count)
            korzina.append(new_order)
            all_products['Весь склад'][pr_name] -= pr_count
            print ("Товар успешно помещен в корзину!")
    else:
        print('Error')


    print(korzina)