def decrypt(codes_list, private_key):
    text = ''
    print('\n\n===== decrypting... =====\n')
    i = 1
    for code in codes_list:
        text += chr(pow(code, private_key[0], private_key[1]))
        print(f'Decrypted {(i / len(codes_list))*100} %!')
        i += 1

    print('\n===== done! =====\n\n')
    return text
