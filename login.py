KEY = "admin1234"
class Login:
    def authenticate():
        KEY = input("Enter password: ")
        if KEY == "admin1234":
            return True
        return False