import sys

RO_ALPHABET = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

def validate_input(text):
    allowed = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzĂÂÎȘȚăâîșț')
    return all(c in allowed for c in text)

def vigenere_cipher(text, key, op):
    result = []
    key_len = len(key)
    key_idx = 0
    for c in text:
        mi = RO_ALPHABET.index(c)
        ki = RO_ALPHABET.index(key[key_idx])
        if op == 'encrypt':
            new_mi = (mi + ki) % 31
        elif op == 'decrypt':
            new_mi = (mi - ki) % 31
        result.append(RO_ALPHABET[new_mi])
        key_idx = (key_idx + 1) % key_len
    return ''.join(result)

def main():
    while True:
        print("\nVigenère Cipher Menu")
        print("1. encrypt a message")
        print("2. decrypt a ciphertext")
        print("0. exit")
        choice = input("pick 0/1/2: ").strip()

        if choice == '0':
            print("Goodbyeee!")
            sys.exit()

        elif choice not in ['1', '2']:
            print("please pick 0/1/2/3")
            continue

        op = 'encrypt' if choice == '1' else 'decrypt'
        label = "message" if op == 'encrypt' else "ciphertext"

        while True:
            key = input("enter key: ").strip().upper().replace(' ', '')
            if len(key) < 7:
                print("key must be at least 7 characters long")
            elif not validate_input(key):
                print("key must contain only letters A-Z")
            else:
                if all(c in RO_ALPHABET for c in key):
                    break
                else:
                    print("key contains invalid characters")

        while True:
            text = input(f"Enter the {label} (letters A-Z): ").strip().replace(' ', '')
            if not text:
                print("Input cannot be empty")
            elif not validate_input(text):
                print("Input must contain only letters A-Z")
            else:
                text = text.upper()
                if all(c in RO_ALPHABET for c in text):
                    break
                else:
                    print("Input contains invalid characters for Romanian alphabet")

        result = vigenere_cipher(text, key, op)
        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
