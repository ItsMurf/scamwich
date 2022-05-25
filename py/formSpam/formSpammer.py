import requests
import time
import random
import string
import json
import threading
import subprocess
import string

namesJ = "lists/names.json"
lNamesJ = "lists/lnames.json"
rockyouJ = "lists/rockyou.json"


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


def passGen(spamCount, rockyou):
    passwords = []

    for i in range(spamCount):
        rockRand = random.choice(rockyou)
        passwords.append(rockRand)

        length = random.randint(8, 15)

        password = "".join(random.sample(string.printable, length))

        passwords.append(password)
    return passwords


def phoneGen(spamCount):  # process does work, but most forms check for 555 area code.
    phones = []

    for i in range(spamCount):
        number = string.digits
        phone = (
            "(555)"
            + " "
            + "".join(random.sample(number, 3))
            + "-"
            + "".join(random.sample(number, 4))
        )
        phones.append(phone)
    return phones


def requestsVal(emails, passwords, fNames, lNames, phones):
    requestData = {  # Change according to headers.
        "email": random.choice(emails)
        # "Password": random.choice(passwords),
    }
    # requestData["UserName"] = requestData["EMAIL"]
    return requestData


def waitTime():
    print(
        "\nWould you like to use the randomized timer (3-21 seconds) or choose your own delay?"
    )
    waitInput = input('Type "R" (Randomized) or "C" (Choose) or "T" (Threading): ')

    if waitInput == "R" or waitInput == "r":
        print("Randomized Delays Chosen. Starting...")
        delay = random.randint(3, 21)
    elif waitInput == "C" or waitInput == "c":
        delay = int(input("\nEnter a delay integer (in seconds): "))
    elif waitInput == "T" or waitInput == "t":
        delay = 0
    else:
        print("\nLooks like your input was invalid, please try again. ")
        exit()

    return delay


def goodnight(url, headers):
    response = requests.post(url, allow_redirects=False, data=headers, verify=False)

    return response


def urlCheck():
    url = input("\nEnter the Forms URL: ")

    if url.startswith("HTTP") or url.startswith("http"):
        return url
    else:
        print("\nInvalid URL. Try Again.")
        exit()


def spamCountCheck():
    spamCount = input("\nEnter the Amount of Times to Loop: ")

    if spamCount.isnumeric() and int(spamCount) > 0:
        return int(spamCount)
    else:
        print("Invalid Spam Count. Enter a Positive Integer.")
        exit()


def main():
    domain = [
        "gmail.com",
        "usu.edu",
        "suu.edu",
        "byu.edu",
        "yahoo.com",
        "bitwarden.com",
        "us.gov",
        "outlook.com",
        "live.com",
    ]

    with open(namesJ) as names:
        fNames = json.load(names)

    with open(lNamesJ) as lasts:
        lNames = json.load(lasts)

    with open(rockyouJ) as rocked:
        rockyou = json.load(rocked)

    subprocess.call("clear", shell=False)

    print(
        """
    ╭────────────────────────────────────────────────────────────────╮
    │  _                                                             │
    │ | |                                                            │
    │ | |  __   ,_    _  _  _                                        │
    │ |/  /  \_/  |  / |/ |/ |                                       │
    │ |__/\__/    |_/  |  |  |_/                                     │  
    │ |\                                                             │
    │ |/                                                             │
    │                                                                │
    │               ()                                               │
    │               /\   _   __,   _  _  _    _  _  _    _   ,_      │
    │              /  \|/ \_/  |  / |/ |/ |  / |/ |/ |  |/  /  |     │
    │             /(__/|__/ \_/|_/  |  |  |_/  |  |  |_/|__/   |_/   │  
    │                 /|                                             │
    │                 \|                                             │
    │                                                                │"""
    )
    print("╭───┴────────────────────────────────────────────────────────────────┴───╮")
    print("│                    Spamming Online Forms Since 2022                    │")
    print("╰───────────────────────────────────────────────────┬───────────────────┬╯")
    print("                                                    │ ∁trl + ∁ to Exit. │ ")
    print("                                                    ╰──────────\─\─\─\──╯ ")
    print()

    url = urlCheck()
    spamCount = spamCountCheck()
    emails = emailGen(spamCount, fNames, lNames, domain)
    passwords = passGen(spamCount, rockyou)
    phones = phoneGen(spamCount)
    delay = waitTime()

    threads = []

    for i in range(spamCount):

        headers = requestsVal(emails, passwords, fNames, lNames, phones)
        t = threading.Thread(target=goodnight(url, headers))
        t.daemon = True
        threads.append(t)
        response = goodnight(url, headers)

        print(  # Change according to headers.
            "\n"
            + str(i + 1)
            + ": "
            + "\n"
            + "   Response: "
            + str(response)
            + "\n"
            + "   Email: "
            + headers["email"]
            + "\n"
            # + "   Password: "
            # + headers["Password"]
            # + "\n"
            # + "   User: "
            # + headers["USER"]
            # + "\n"
            # + "First Name: "
            # + headers["FIRSTNAME"]
            # + "\n"
            # + "Last Name: "
            # + headers["LASTNAME"]
            # + "\n"
            # + "Phone: "
            # + headers["SMS"]
        )

        if str(response) == "<Response [429]>":
            s = 60
            print("╭──────────╮")
            print("│ CAPTURED │")
            print("╰──────────╯")
            while s:
                mins, secs = divmod(s, 60)
                timer = "{:02d}:{:02d}".format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                s -= 1

            delay = 17
            print("\nProcess Restarted - Delays May Be Longer")

        elif str(response) == "<Response [404]>":
            print("╭────────────────╮")
            print("│ PAGE NOT FOUND │")
            print("╰────────────────╯")
            exit()

        if i == spamCount:
            exit()

        time.sleep(delay)

    for i in range(spamCount):
        threads[i].start()

        if i == spamCount:
            exit()

    for i in range(spamCount):
        threads[i].join()

        if i == spamCount:
            exit()


if __name__ == "__main__":
    main()
