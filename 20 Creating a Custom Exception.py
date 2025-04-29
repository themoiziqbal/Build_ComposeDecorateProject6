# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be at least 18.")
    else:
        print("Access granted.")

# Using try...except to handle the custom exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")
