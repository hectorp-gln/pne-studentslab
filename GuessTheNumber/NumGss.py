import random
import termcolor


class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        self.attempts.append(number)
        if int(number) == self.secret_number:
            message = termcolor.colored(f"You guessed the number after {len(self.attempts)} attempts!","yellow")
        elif int(number) < self.secret_number:
            message = termcolor.colored("Higher","blue")
        else:
            message = termcolor.colored("Lower", "red")
        return message