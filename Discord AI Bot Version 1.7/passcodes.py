import random
import string

class passcodeGen:
    def get_passcode(self):
        passcode = ''

        for x in range (0, 9):
            i = random.randint(0, 9)
            letter = random.choice(string.ascii_letters)
            passcode += letter
            passcode += str(i)

        return str(passcode)


    def randomize_passcode(self):
        rand_passcode = ""
        for x in range(0, 9):
            rand_passcode += str(x)

        return str(rand_passcode)