import hashlib

def multiply_numbers(a, b):
    return a * b

def hash_password(password):
    # Увага: MD5 вважається криптографічно небезпечним!
    hashed = hashlib.sha256(password.encode()).hexdigest()   
    return hashed

if __name__ == "__main__":
    print(multiply_numbers(5, 5))
