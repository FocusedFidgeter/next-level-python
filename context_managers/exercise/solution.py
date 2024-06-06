from contextlib import contextmanager

# Implement a context manager decorator named file_manager
# I'm using a generator together with the contextmanager decorator
# to implement a context manager - this is the easiest way to do it!


@contextmanager
def file_manager(filename: str, mode: str):
    file = open(filename, mode, encoding="utf8")
    yield file
    file.close()

def write_file_content(content: str):
    with file_manager("sample.txt", "w") as file:
        file.write(content)

def main() -> None:
    write_file_content("Hello, world!")



if __name__ == "__main__":
    main()
