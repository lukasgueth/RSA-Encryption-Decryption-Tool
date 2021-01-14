from generate_keys import generate_keys
from encrypt import encrypt
from decrypt import decrypt


def index(n):
    if n == 1:
        keys = generate_keys()
        print('Public key:',
              f'{keys["public_key"][0]},{keys["public_key"][1]}')
        print('Private key:',
              f'{keys["private_key"][0]},{keys["private_key"][1]}')
        return

    elif n == 2:
        text = input('Type in a text\n: ')
        print('\n')
        public_key = input('Paste a public key\n: ').split(',')
        print('\n')
        public_key[0] = int(public_key[0])
        public_key[1] = int(public_key[1])

        if len(public_key) == 2 and type(public_key[0]) == int and type(public_key[1]) == int:
            encrypted_codes = encrypt(text, public_key)
            codes_str = ''
            i = 0
            for code in encrypted_codes:
                codes_str += f'{str(code)}'
                if i < len(encrypted_codes)-1:
                    codes_str += ','
                i += 1

            return print('Encrypted codes\n: ', codes_str)
        else:
            return print('Invalid public key!')

    elif n == 3:
        codes = input('Paste a list of codes\n: ')
        print('\n')
        private_key = input('Paste your private key\n: ').split(',')
        print('\n')
        private_key[0] = int(private_key[0])
        private_key[1] = int(private_key[1])

        codes_list = []
        codes = codes.split(',')
        for code in codes:
            codes_list.append(int(code))

        if len(private_key) == 2 and type(private_key[0]) == int and type(private_key[1]) == int:
            return print(decrypt(codes_list, private_key))
        else:
            return print('Invalid private key!')

    elif n == 4:
        exit()

    else:
        print('Please select a valid action!')
        return


while True != False:
    print("Actions:\n1: Generate keys\n2: Encrypt text\n3: Decrypt codes list\n4: Close the program")
    n = int(input('Type in a number to select an action\n: '))
    print('\n')
    index(n)
    print('\n\n\n')
