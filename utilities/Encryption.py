from cryptography.fernet import Fernet


key = b"Uhgmy0Q9XzP3A0F60K5H3v6M1jyMB9nYlUdMiv520vQ="
fernet = Fernet(key)
encoding = "utf-8"


def encrypt(string):
    return fernet.encrypt(bytes(string, encoding))


def decrypt(string):
    return fernet.decrypt(bytes(string, encoding)).decode(encoding)
