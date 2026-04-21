import json
import termcolor
from pathlib import Path


jsonstring = Path("people-e1.json").read_text()
person = json.loads(jsonstring)

print()
for n in person:
    termcolor.cprint("Name: ", 'green', end="")
    print(n['Firstname'], n['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(n['age'])

    phoneNumbers = n['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')

    print(len(phoneNumbers))

    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
