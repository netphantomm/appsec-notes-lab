from werkzeug.security import generate_password_hash, check_password_hash

stored_hash = generate_password_hash("training-password")

def verify_password(password):
    return check_password_hash(stored_hash, password)
input_password = input("Enter password: ")
is_valid = verify_password(input_password)

print(is_valid)
if is_valid:
    print("Access granted")
else:
    print("Access denied")