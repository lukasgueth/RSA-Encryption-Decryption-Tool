def encrypt(text, public_key):
    encrypted_codes = []
    print('\n\n===== encrypting... =====\n')
    i = 1
    char_list = [char for char in text]
    for char in char_list:
        encrypted_codes.append((ord(char)**public_key[0]) % public_key[1])
        print(f'Encrypted {(i / len(char_list))*100} %!')
        i += 1
    print('\n===== done! =====\n\n')

    return encrypted_codes
