import random
import string


def generate_pw():
    password = ''

    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + \
            random.choice(string.ascii_lowercase) + \
            random.choice(string.digits) + \
            random.choice(string.punctuation)

    for y in range(random.choice(range(12, 16)) - 4):
        password = password + random.choice(string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.digits +
                                            string.punctuation)

    return password
