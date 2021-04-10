from random import seed, choice


def get_num_attempts():
    seed(24896725)
    i = 0
    while True:
        flips = (choice([1, 2]), choice([1, 2]))
        i += 1
        if flips != (2, 2):
            return i * 2
