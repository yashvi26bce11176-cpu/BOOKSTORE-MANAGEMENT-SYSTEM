```python
# Check that the input is not empty
def validate_nonempty(value, field_name):
    while not value.strip():
        print(field_name, "cannot be empty.")
        value = input("Enter " + field_name + ": ")

    return value.strip()


# Validate that the input is a non-negative integer
def validate_int(value, field_name):
    while True:
        try:
            number = int(value)

            # Do not allow negative numbers
            if number < 0:
                raise ValueError

            return number

        except ValueError:
            print("Please enter a valid non-negative integer.")
            value = input("Enter " + field_name + ": ")


# Validate that the input is a non-negative decimal number
def validate_float(value, field_name):
    while True:
        try:
            number = float(value)

            # Do not allow negative numbers
            if number < 0:
                raise ValueError

            return number

        except ValueError:
            print("Please enter a valid non-negative number.")
            value = input("Enter " + field_name + ": ")


# Pause the program until the user presses Enter
def pause():
    input("\nPress Enter to continue..")
```
