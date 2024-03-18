from Crypto.PublicKey import RSA
import random

def generate_rsa_key(num_digits):
    # Generate two prime numbers of approximately half the desired digits
    half_num_digits = num_digits // 2
    min_val = 10 ** (half_num_digits - 1)
    max_val = (10 ** half_num_digits) - 1
    p = generate_prime(min_val, max_val)
    q = generate_prime(min_val, max_val)

    # Compute the modulus
    n = p * q

    # Compute the totient
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent e
    e = 65537  # Commonly used value for e

    # Compute the private exponent d
    d = mod_inverse(e, phi_n)

    # Create an RSA key object
    key = RSA.construct((n, e, d))

    return key

def generate_prime(min_val, max_val):
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

if __name__ == "__main__":
    num_digits = 100  # Change this value to the desired number of digits
    key = generate_rsa_key(num_digits)
    print("RSA Key Pair Generated:")
    print(f"Public Key (n, e): ({key.n}, {key.e})")
    print(f"Private Key (n, d): ({key.n}, {key.d})")
