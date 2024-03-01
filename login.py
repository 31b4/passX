import bcrypt

stored_hash = b'$2b$12$T.pZ35zrM5jwFd4B6SoNu.wb.xXV4wMarGs.Mfa5skxUV1eiMZ3xe'
stored_salt = b'$2b$12$T.pZ35zrM5jwFd4B6SoNu.'

def verify_password(input_password):
    hashed_input = bcrypt.hashpw(input_password.encode(), stored_salt)

    if hashed_input == stored_hash:
        return True
    else:
        return False