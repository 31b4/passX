from interface import TerminalInterface, clear
from login import Login

if __name__ == "__main__":
    while not Login.authenticate():
        clear()
        print("Wrong password.")
    TerminalInterface().run()

