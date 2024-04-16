# PassX

A secure password manager that allows you to store and retrieve passwords.

## Features

- Strongly encrypt passwords, usernames, and site information to ensure maximum security
- Retrieve passwords quickly

## Installation

To install PassX, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/passx.git`
2. Navigate to the project directory: `cd passx`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

1. To use PassX, run the following command:

```bash
python3 passx.py
```

2. Enter your unique KEY


3. Choose from the following points:
```
———————————————————————————————
—————————————PassX—————————————
1:      Add new password
2:      Get password
3:      Remove Password
4:      List all
q:      Quit
———————————————————————————————

What you want: 
```

## How is it secure?
When password, username, and site informations are stored, they are encrypted using a unique KEY.
##### For example:
`KEY = 'bence'`
```bash
site: neptun.pte.hu --> b'\x0c\x00\x1e\x17\x10\x0cK\x1e\x17\x00L\r\x1b'
username: ZTBFRU --> b'81,%77'
password: 12345678 --> b'SW]WPTRV'
```
##### With other key:
`KEY = 'timea'`
```bash
site: neptun.pte.hu --> b'\x1a\x0c\x1d\x11\x14\x1aG\x1d\x11\x04Z\x01\x18'
username: ZTBFRU --> b'.=/#3!'
password: 12345678 --> b'E[^QTB^U'
```

It is clear that with a different KEY the encryption will be different.

This encryption ensures that even if someone gains access to the interface, they cannot decrypt the passwords without the key.
##### Getting the password back:
We have to enter the `site` and `username` to get the password.
**BUT** everything is stored encrypted in `passwords.db`

so, we have to encrypt the user input first:
```py
encrypted_site = encrypt(site, KEY)
encrypted_username = encrypt(username, KEY)
```
then find the passwords where `site` and `unsername` is equal to the encrypted form
```py
encrypted_password = DatabaseManager('passwords.db').get_password(encrypted_site, encrypted_username)
```
finally decrypt it to get the real password
```py
password = decrypt(encrypted_password, KEY)
```