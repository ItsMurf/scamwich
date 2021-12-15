import requests

url = ''

data = {
    'EMAIL': '',
    'LASTNAME': '',
    'FIRSTNAME': ''
}

while True:
    response = requests.post(url, data=data).text

    print(response)
