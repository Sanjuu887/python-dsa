"""
4. Password Strength Checker

Take password from user.

Check:

length should be >= 8
must contain at least one digit
must contain at least one uppercase letter

If weak:
print reason.

Example:

Password too short
Missing uppercase letter
Missing digit
"""
password = input("Enter password: ")

has_digit = False
has_upper = False

# Check length
if len(password) < 8:
    print("Password too short")

# Check characters one by one
for ch in password:

    # Check digit
    if ch.isdigit():
        has_digit = True

    # Check uppercase
    if ch.isupper():
        has_upper = True

# Final checks
if not has_digit:
    print("Missing digit")

if not has_upper:
    print("Missing uppercase letter")

# Strong password
if len(password) >= 8 and has_digit and has_upper:
    print("Strong Password")
