def read_file(filepath):
    """ Reads the content of a file. """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def write_file(filepath, content):
    """ Writes content to a file. """
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def parse_json(json_string):
    """ Parses a JSON string into a Python dictionary. """
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        print("Invalid JSON string.")
        return None


def format_date(date_obj, format_string='%Y-%m-%d'):
    """ Formats a date object into a string. """
    if not isinstance(date_obj, (datetime.date, datetime.datetime)):
        print("Provided argument is not a date object.")
        return None
    return date_obj.strftime(format_string)


import datetime
