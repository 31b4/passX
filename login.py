import bcrypt

user1_hash = b'$2b$12$T.pZ35zrM5jwFd4B6SoNu.MJcd1tQchLRuwQtEFgS/9dRudIQNOfu' # "bence"
user2_hash = b'$2b$12$T.pZ35zrM5jwFd4B6SoNu.3imfOuL0L5cWhIQKfkPMBsr55/DI1ci' # "timea"
stored_salt = b'$2b$12$T.pZ35zrM5jwFd4B6SoNu.' # const

def verify_password(input_password):
    hashed_input = bcrypt.hashpw(input_password.encode(), stored_salt)
    print(hashed_input)

    if hashed_input == user1_hash or hashed_input == user2_hash:
        return True
    else:
        return False