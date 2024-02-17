import logging


def read_file(file_path):
    """Read and return the content of a file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                logging.info("File is empty.")
            return content
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        raise


def write_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        logging.error(f"Error writing to file {file_path}: {e}")
        raise