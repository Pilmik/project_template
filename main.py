import app.io.input as inp
import app.io.output as out


def main():
    text_from_console = inp.console_input()
    path_to_file = "./data/table.csv"
    path_to_output_1 = "data/output_1.txt"
    path_to_output_2 = "data/output_2.txt"
    path_to_output_3 = "data/output_3.txt"

    out.console_output(text_from_console)
    out.console_output(inp.default_file_input(path_to_file))
    out.console_output(inp.pandas_file_input(path_to_file))

    out.file_output(path_to_output_1, text_from_console)
    out.file_output(path_to_output_2, inp.default_file_input(path_to_file))
    out.file_output(path_to_output_3, inp.pandas_file_input(path_to_file))


if __name__ == "__main__":
    main()
