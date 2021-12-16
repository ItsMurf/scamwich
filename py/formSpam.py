import requests

url = input('Enter Request URL: ')

data = {
    'EMAIL': input('Enter Form Email: '),
    'LASTNAME': input('Enter Form Lastname: '),
    'FIRSTNAME': input('Enter Form Firstname: ')
}

while True:
    response = requests.post(url, data=data).text

    print(response)
