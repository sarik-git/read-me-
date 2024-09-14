import requests

url = 'https://httpbin.org/post'
data = { 
    'custname': 'elon musk',
    'custtel': '+998903211111',
    'custemail': 'real_elon@mail.com',
    'size': 'large',
    'topping': 'large',
    'delivery': '21:00',
    'comments':'i love pizza'
}
response = requests.post(url, data=data)
print(response)