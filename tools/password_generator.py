from random import randint

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_="
PASSWORD_LENGTH = 32

def generate_password():
    return "".join([CHARS[randint(0,63)] for i in range(PASSWORD_LENGTH)])
