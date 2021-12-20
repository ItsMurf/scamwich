import requests
import time
import random

print()
print('Scamwich - formSpam')
print('Spam Online Forms')
print()

def initial():
    contIn = ''
    while(contIn != 'Y' and contIn != 'y' and contIn != 'N' and contIn != 'n'):
        contIn = input('Continue? Y/N: ').upper()

    if contIn == 'Y':
        url = input('Enter Request URL: ')  # request URL destination
        delayCount = float(input('Delay Time: '))  # seconds between each request
        spamCount = int(input('Spam Count: ')) # number of forms sent (~16 until flagged)

        for i in range(spamCount):
            line = random.choice(open('names.txt').readlines())

        data = { # change the following variables to match the request
            'EMAIL': input('Enter Form Email: '),
            'LASTNAME': input('Enter Form Lastname (User): '),
            'FIRSTNAME': line # input('Enter Form Firstname (Password): ')
        }

        return url, delayCount, spamCount, data, line

    elif contIn == 'N':
        print()
        print('Exiting.')
        print()
        exit()

    else:
        print()


def main(url, delayCount, spamCount, data, line):
    for i in range(spamCount):
        response = requests.post(url, allow_redirects=False, data=data).text
        print()
        print(str(i + 1) + ': ' + response)
        print('Ctrl + C to Exit.')
        print()

        time.sleep(delayCount)


url, delayCount, spamCount, data, line = initial()
main(url, delayCount, spamCount, data, line)
