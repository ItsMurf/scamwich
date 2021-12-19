import requests
import time

url = input('Enter Request URL: ') # request URL destination
delayCount = int(input('Delay Time: ')) # seconds between each request
spamCount = int(input('Spam Count: ')) # number of forms sent (~17 until flagged)


data = {
    'EMAIL': input('Enter Form Email: '),
    'LASTNAME': input('Enter Form Lastname (User): '),
    'FIRSTNAME': input('Enter Form Firstname (Password): ')
}

for i in range(spamCount):
    response = requests.post(url, data=data).text
    print(response)

    time.sleep(delayCount)
