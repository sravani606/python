import string
import secrets

print("=== GUNDRE SRAVANI PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4")
    exit()

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

all_chars = upper + lower + digits + symbols

password = [
    secrets.choice(upper),
    secrets.choice(lower),
    secrets.choice(digits),
    secrets.choice(symbols)
]

while len(password) < length:
    password.append(secrets.choice(all_chars))

secrets.SystemRandom().shuffle(password)

print("Generated Password:", "".join(password))
