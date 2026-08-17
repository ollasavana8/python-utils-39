def validate_input(data):
    """
    Validate the input data. It checks for required fields and basic data types.
    """
    required_fields = ['name', 'age', 'email']
    errors = []

    for field in required_fields:
        if field not in data:
            errors.append(f"Missing field: {field}")

    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0:
            errors.append("Invalid age: must be a non-negative integer")

    if 'email' in data:
        if not isinstance(data['email'], str) or '@' not in data['email']:
            errors.append("Invalid email: must be a valid email address")

    if errors:
        raise ValueError("Input validation errors: " + ", ".join(errors))

# Example usage
if __name__ == '__main__':
    input_data = {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
    try:
        validate_input(input_data)
        print("Input is valid.")
    except ValueError as e:
        print(e)