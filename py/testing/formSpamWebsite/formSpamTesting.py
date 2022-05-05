import requests
import time
import random
import string
import json

def emailGen(spamCount, fNames, lNames, domain):
    emails = []

    for i in range(spamCount):
        randInt = ''.join(random.choice(string.digits))
        number = randInt if random.randint(0, 1) else ""

        fName = random.choice(fNames)
        lName = random.choice(lNames)

        email = f"{fName}.{lName}{number}@{random.choice(domain)}"

        emails.append(email.lower())
    return emails

def passGen(spamCount):
    passwords = []

    for i in range(spamCount):
        lower = "abcdefghijklmnoprstuvyz"
        upper = "ABCDEFGHIJKMLMNOPRSTUVYZ"
        number = "0123456789"
        symbol = "!@#$%*"

        passw = lower + upper + number + symbol 
        password = ''.join(random.sample(passw, 12))

        passwords.append(password)
    return passwords

def phoneGen(spamCount):
    phones = []
    
    for i in range(spamCount):
        number = "0123456789"
        phone = '555' + ''.join(random.sample(number, 7))
        phones.append(phone)
    return phones    
        
def requestsVal(dataCount, emails, passwords, fNames):
    requestData = {
        'EMAIL': random.choice(emails),
        'PASSWORD': random.choice(passwords),
        'USER': random.choice(fNames)
        # 'LNAME': random.choice(lNames)
    }
    return requestData

def wait():
    print('\nWould you like to use the randomized timer (16-30 seconds) or choose your own delay? ')
    waitInput = input('\nType "R" (Randomized) or "C" (Choose): ')

    if waitInput == "R" or waitInput == "r":
        print('Randomized Delays Chosen. Starting...')
        delay = random.randint(16, 30)
    elif waitInput == "C" or waitInput == "c":
        delay = int(input('\nEnter a delay integer (in seconds): '))
    else: 
        print('\nLooks like your input was invalid, try again. ')
        exit()

    return delay


def main():
    domain = ['gmail.com', 'usu.edu', 'suu.edu', 'byu.edu']

    fNames = json.loads(open('names.json').read())
    lNames = json.loads(open('lnames.json').read())

    print('\n               Scamwich - formSpam')
    print('           Spamming Online Forms Since 2022\n')

    print('Ctrl + C to Exit.')

    url = input('\nEnter the forms URL: ')
    spamCount = int(input('\nEnter the amount of times to loop: '))
    dataCount = int(input('\nEnter the request variable count: '))

    emails = emailGen(spamCount, fNames, lNames, domain)
    passwords = passGen(spamCount)
    phones = phoneGen(spamCount)
    headers = requestsVal(dataCount, emails, passwords, fNames)
    delay = wait()

    for i in range(spamCount):
        response = requests.post(url, allow_redirects=False, data=headers).text
        print('\n' + str(i + 1) + ': ' + response + ' ' + random.choice(emails) + ' ' + random.choice(passwords) + '\n')

        time.sleep(delay)

if __name__ == '__main__':
    main()
    
