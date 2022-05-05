import requests
import time
import random
import string
import json
import threading


def emailGen(spamCount, fNames, lNames, domain):
    emails = []

    for i in range(spamCount):
        randInt = "".join(random.choice(string.digits))
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

        length = random.randint(10, 17)

        passw = lower + upper + number + symbol
        password = "".join(random.sample(passw, length))

        passwords.append(password)
    return passwords


def phoneGen(spamCount):
    phones = []

    for i in range(spamCount):
        number = "0123456789"
        phone = "555" + "".join(random.sample(number, 7))
        phones.append(phone)
    return phones


def requestsVal(emails, passwords, fNames, lNames, phones):
    requestData = {
        "EMAIL": random.choice(emails),
        "STATUS": random.choice(passwords),
        "USER": random.choice(fNames),
        "FIRSTNAME": random.choice(fNames),
        "LASTNAME": random.choice(lNames),
    }
    return requestData


def wait():
    print(
        "\nWould you like to use the randomized timer (16-30 seconds) or choose your own delay? "
    )
    waitInput = input('Type "R" (Randomized) or "C" (Choose): ')

    if waitInput == "R" or waitInput == "r":
        print("Randomized Delays Chosen. Starting...")
        delay = random.randint(16, 30)
    elif waitInput == "C" or waitInput == "c":
        delay = int(input("\nEnter a delay integer (in seconds): "))
    else:
        print("\nLooks like your input was invalid, try again. ")
        exit()

    return delay


def main():
    domain = ["gmail.com", "usu.edu", "suu.edu", "byu.edu"]

    fNames = json.loads(open("names.json").read())
    lNames = json.loads(open("lnames.json").read())

    print("\n                               Scamwich - formSpam")
    print("                         Spamming Online Forms Since 2022\n")

    print("Ctrl + C to Exit.")

    url = input("\nEnter the forms URL: ")
    spamCount = int(input("\nEnter the amount of times to loop: "))
    # dataCount = int(input("\nEnter the request variable count: "))

    emails = emailGen(spamCount, fNames, lNames, domain)
    passwords = passGen(spamCount)
    phones = phoneGen(spamCount)
    delay = wait()

    for i in range(spamCount):
        headers = requestsVal(emails, passwords, fNames, lNames, phones)
        response = requests.post(url, allow_redirects=False, data=headers)
        print(
            "\n"
            + str(i + 1)
            + ": "
            + "\n"
            + "Response: "
            + str(response)
            + "\n"
            + "Email: "
            + headers["EMAIL"]
            + "\n"
            + "Password: "
            + headers["STATUS"]
            + "\n"
            + "First Name: "
            + headers["FIRSTNAME"]
            + "\n"
            + "User: "
            + headers["USER"]
            + "\n"
            + "Last Name: "
            + headers["LASTNAME"]
            + "\n"
            # + "Phone: "
            # + headers["SMS"]
        )

        time.sleep(delay)


if __name__ == "__main__":
    main()

# threads = []

# for i in range(50):
#     t = threading.Thread(target=main)
#     t.daemon = True
#     threads.append(t)

# for i in range(50):
#     threads[i].start()

# for i in range(50):
#     threads[i].join()
