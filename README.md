# BruteSHA1
Simple Python brute-forse tool for crack SHA1 hashes.
Hello=)
from urllib.request import urlopen, hashlib

sha1hash = input("Введите ваш хэшь для его взлома:\n>")
list_of_common_ps =str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for guess in list_of_common_ps.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("Ваш пароль: ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Пароль ", str(guess), " не совпадает, попробуйте следующий...")
print("Пароля нет в базах данных, мы это исправим в следующих обновлениях")

Ссылку на список паролей можно менять, так что можете вставлять свои списки паролей в формате .txt, или найденые в инете=)
