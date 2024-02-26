from confidentials import ALL
import os
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

# Example usage:


def clear_console():
    # For POSIX systems (Linux, Mac)
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

clear_console()
class TerminalInterface:
    def __init__(self):
        pass

    def display_options(self):
        print("———————————————————————————————")
        print("—————————————PassX—————————————")
        print("1:\t\tAdd new password")
        print("2:\t\tGet password")
        print("3:\t\tRemove Password")
        print("q:\t\tQuit")
        print("——————————————————————————————\n")

    def addPass(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        ALL[username] = password
        clear_console()


    def getPass(self):
        find_username = input("Enter username: ")
        copy_to_clipboard(ALL[find_username])
        print("Password copied to clipboard.")

    def removePass(self):
        print("...")

    def run(self):
        while True:
            self.display_options()
            choice = input("What you want: ")

            if choice == '1':
                self.addPass()
            elif choice == '2':
                self.getPass()
            elif choice == '3':
                self.removePass()
            elif choice == 'q':
                print("Good bye.")
                break
            else:
                print("Retard")
