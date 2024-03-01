from interface import TerminalInterface, clear

if __name__ == "__main__":
    KEY = input("Enter the KEY: ")
    clear()
    TerminalInterface().run(KEY)