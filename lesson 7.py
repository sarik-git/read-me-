all_products = {'весь склад':{}}


admin = input('что вы хотите добавить? ')

product_name = input("введите название продукта: ")
product_count = input('введите количество: ')
all_products['весь склад'][product_name] = product_count

print(all_products)