import os
import json

class FileUtils:
    @staticmethod
    def read_json(file_path):
        """Reads a JSON file and returns its content."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def write_json(file_path, data):
        """Writes data to a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def list_files(directory, extension=None):
        """Lists files in a directory, optionally filtered by file extension."""
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"{directory} is not a valid directory.")
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if extension:
            files = [f for f in files if f.endswith(extension)]
        return files

    @staticmethod
    def delete_file(file_path):
        """Deletes a file if it exists."""
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"{file_path} does not exist and cannot be deleted.")
