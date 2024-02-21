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
        print("...")


    def getPass(self):
        print("...")


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
