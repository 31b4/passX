from interface import TerminalInterface, clear
from login import verify_password


if __name__ == "__main__":
    KEY = input("Enter the KEY: ")
    if not verify_password(KEY):
        exit(0)

    clear()
    TerminalInterface().run(KEY)