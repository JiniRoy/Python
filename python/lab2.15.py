import random
import string

character=list(string.ascii_letters+string.digits+ "!@#$%^&*()")

def random_password():
    random.shuffle(character);
    password = [];
    for i in range (0,12):
        password.append(random.choice(character));
    random.shuffle(password)
    print("".join(password))

random_password()