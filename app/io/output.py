def console_output(output_text):
    """Outputs text to the console.

    Examples:
        >>> console_output("Hello!")
        'Hello!'

    Args:
        output_text (str): The text to be output to the console by the function.

    """
    print(output_text)


def file_output(filename, output_text) -> None:
    """Outputs text to the specified file.

    Args:
        filename (str): Path to the file where the text will be written using the function.
        output_text (str): The text to be written to the file using the function.

    Raises:
        FileNotFoundError: A file with the specified path and name was not found.
    """
    try:
        with open(filename, 'w') as file:
            file.write(str(output_text))
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
