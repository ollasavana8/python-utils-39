import re

def is_valid_email(email: str) -> bool:
    """Check if the provided email is valid."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


def is_valid_phone(phone: str) -> bool:
    """Check if the provided phone number is valid."
    phone_regex = r'^\+?\d{10,15}$'
    return re.match(phone_regex, phone) is not None


def validate_user_input(email: str, phone: str) -> tuple:
    """Validate user email and phone number."
    return is_valid_email(email), is_valid_phone(phone)


def main():
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    email_valid, phone_valid = validate_user_input(email, phone)
    if email_valid:
        print('Email is valid.')
    else:
        print('Email is invalid.')
    if phone_valid:
        print('Phone number is valid.')
    else:
        print('Phone number is invalid.')


if __name__ == '__main__':
    main()