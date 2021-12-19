import requests

url = input('Enter Request URL: ')
varCount = int(input('Number of Data Variables: '))

for i in range(varCount):
    var = input('Variable Name: ')

'''
data = {
    'EMAIL': input('Enter Form Email: '),
    'LASTNAME': input('Enter Form Lastname: '),
    'FIRSTNAME': input('Enter Form Firstname: ')
}
'''

'''
while True:
    response = requests.post(url, data=data).text

    print(response)
'''
