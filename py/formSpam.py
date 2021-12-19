import requests
import time

print()
print('Scamwich - formSpam')
print('Spam online forms with your choice of inputs.')
print()


def initial():
    contIn = ''
    while(contIn != 'Y' and contIn != 'y' and contIn != 'N' and contIn != 'n'):
        contIn = input('Continue? Y/N: ').upper()

    if contIn == 'Y':
        url = input('Enter Request URL: ')  # request URL destination
        delayCount = int(input('Delay Time: '))  # seconds between each request
        # number of forms sent (~17 until flagged)
        spamCount = int(input('Spam Count: '))
        data = {
            'EMAIL': input('Enter Form Email: '),
            'LASTNAME': input('Enter Form Lastname (User): '),
            'FIRSTNAME': input('Enter Form Firstname (Password): ')
        }
        return url, delayCount, spamCount, data

    elif contIn == 'N':
        print()
        print('Exiting.')
        print()
        exit()

    else:
        print('Try again.')


def main(url, delayCount, spamCount, data):
    for i in range(spamCount):
        response = requests.post(url, data=data).text
        print(response)

        time.sleep(delayCount)


url, delayCount, spamCount, data = initial()
main(url, delayCount, spamCount, data)
