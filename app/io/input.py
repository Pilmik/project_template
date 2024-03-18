from pandas import read_csv as r_csv


def console_input():
    """Read lines from the console.

    Returns:
        str: Returns the string that was typed into the console.
    """
    text = input("Enter your text: ")
    return text


def default_file_input(filename):
    """Reads lines from a file using Python's built-in capabilities.

    Args:
        filename (str): The path to the file to which the function is applied.

    Returns:
        str: Strings from the file specified in filename.

    Raises:
        FileNotFoundError: A file with the specified path and name was not found.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")


def pandas_file_input(filename):
    """Reads lines from a file using Pandas capabilities.

    Args:
        filename (str): The path to the file to which the function is applied.

    Returns:
        str: Strings from the file specified in filename.

    Raises:
        FileNotFoundError: A file with the specified path and name was not found.
    """
    try:
        text = r_csv(filename)
        return text
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
