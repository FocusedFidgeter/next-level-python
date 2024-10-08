# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Create a context manager
# Implement a context manager decorator named file_manager that allows you to open a file
# and write content to it. Use this decorator to write the content "Hello, world!" to the file.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from contextlib import contextmanager

@contextmanager
def file_manager(file_name: str, mode: str):
    file = open(file_name, mode)
    try:
        yield file
    finally:
        file.close


def write_file_content(content: str):
    with file_manager("sample.txt", "w") as file:
        file.write(content)


def main() -> None:
    write_file_content("Hello, world!")


if __name__ == "__main__":
    main()
