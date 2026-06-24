import hashlib


def multiply_numbers(a, b):
    return a * b


def subtract_numbers(a, b):
    return a - b


def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


def divide_numbers(a, b):
    return a / b


if __name__ == "__main__":
    print(multiply_numbers(5, 5))
