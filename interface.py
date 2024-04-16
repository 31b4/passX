from DatabaseManager import DatabaseManager
import os
import pyperclip
from cryption import encrypt, decrypt

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
        print("4:\tList all")
        print("q:\tQuit")
        print("———————————————————————————————\n")

    def addPass(self, KEY):
        site = input("Enter site: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        encrypted_site = encrypt(site, KEY)
        encrypted_username = encrypt(username, KEY)
        encrypted_password = encrypt(password, KEY)

        DatabaseManager('passwords.db').insert_password(encrypted_site, encrypted_username, encrypted_password)
        clear()

    def getPass(self, KEY):
        clear()
        site = input("Enter site: ")
        username = input("Enter username: ")

        encrypted_site = encrypt(site, KEY)
        encrypted_username = encrypt(username, KEY)

        encrypted_password = DatabaseManager('passwords.db').get_password(encrypted_site, encrypted_username)
        print("———————————————————————————————")

        if encrypted_password is None:
            print("No password found for this username and site.")
            print("———————————————————————————————\n")

            return

        password = decrypt(encrypted_password, KEY)

        print("Password:", password)
        copy_to_clipboard(str(password))
        print("Password copied to clipboard.")
        print("———————————————————————————————\n")


    def removePass(self, KEY):
        clear()
        site = input("Enter site: ")
        username = input("Enter username: ")

        encrypted_site = encrypt(site, KEY)
        encrypted_username = encrypt(username, KEY)

        DatabaseManager('passwords.db').delete_account(encrypted_site, encrypted_username)
    def listAll(self, KEY):
        clear()
        result = DatabaseManager('passwords.db').list_all()
        if result is None:
            print("No passwords found.")
            return
        print("{:<20}{:<20}{:<20}".format("Site", "Username", "Password"))
        print("———————————————————————————————————————————————————————")
        for site, username, password in result:
            print("{:<20}{:<20}{:<20}".format(decrypt(site, KEY), decrypt(username, KEY), decrypt(password, KEY)))
        print("———————————————————————————————————————————————————————")

    def run(self, KEY):
        DatabaseManager('passwords.db').create_table()
        clear()

        while True:
            self.display_options()
            choice = input("What you want: ")

            if choice == '1':
                self.addPass(KEY)
            elif choice == '2':
                self.getPass(KEY)
            elif choice == '3':
                self.removePass(KEY)
            elif choice == '4':
                self.listAll(KEY)
            elif choice == 'q':
                clear()
                print("Good bye.")
                break
            else:
                print("Retard")
