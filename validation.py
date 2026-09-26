def validate_nonempty(value, field_name):
    while not value.strip():
        print(field_name, "cannot be empty.")
        value = input("Enter " + field_name + ": ")

    return value.strip()


def validate_int(value, field_name):
    while True:
        try:
            number = int(value)

            if number < 0:
                raise ValueError

            return number

        except ValueError:
            print("Please enter a valid non-negative integer.")
            value = input("Enter " + field_name + ": ")


def validate_float(value, field_name):
    while True:
        try:
            number = float(value)

            if number < 0:
                raise ValueError

            return number

        except ValueError:
            print("Please enter a valid non-negative number.")
            value = input("Enter " + field_name + ": ")


def pause():
    input("\nPress Enter to continue..")
