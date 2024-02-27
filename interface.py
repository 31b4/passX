from confidentials import ALL
from DatabaseManager import DatabaseManager
import os
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

# Example usage:

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class TerminalInterface:
    def __init__(self):
        pass

    def display_options(self):
        print("———————————————————————————————")
        print("—————————————PassX—————————————")
        print("1:\tAdd new password")
        print("2:\tGet password")
        print("3:\tRemove Password")
        print("q:\tQuit")
        print("———————————————————————————————\n")

    def addPass(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        ALL[username] = password
        DatabaseManager('passwords.db').insert_password('site', username, password)
        clear()


    def getPass(self):
        clear()
        find_username = input("Enter username: ")
        password = DatabaseManager('passwords.db').get_password('site', find_username)
        if password is None:
            print("No password found for this username.")
            return

        print("Password:", password)
        copy_to_clipboard(str(password))
        print("Password copied to clipboard.")

    def removePass(self):
        clear()
        username = input("Enter username: ")
        DatabaseManager('passwords.db').delete_account('site', username)


    def run(self):
        DatabaseManager('passwords.db').create_table()
        clear()

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
