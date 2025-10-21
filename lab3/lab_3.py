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

def run_tests():
    key = 'ABCDEFGH'  # length 8 >=7
    msg = 'HELLO'
    cipher = vigenere_cipher(msg, key, 'encrypt')
    print("Test 1: Encrypt 'HELLO' with key 'ABCDEFGH'")
    print(f"Cipher: {cipher}")
    decrypted = vigenere_cipher(cipher, key, 'decrypt')
    print(f"Decrypted: {decrypted}")
    print(f"Should be 'HELLO': {decrypted == msg}")

    invalid_msg = 'ABC123'  # contains number, not accepted
    print(f"\nTest for invalid input: '{invalid_msg}' not accepted (contains non-letters)")

    print("\nTest with Romanian letters:")
    key = 'ABCDEFGH'
    msg = 'BUNĂȘ'  # contains Ă, Ș
    cipher = vigenere_cipher(msg, key, 'encrypt')
    print(f"Msg: {msg}, Cipher: {cipher}")
    decrypted = vigenere_cipher(cipher, key, 'decrypt')
    print(f"Decrypted: {decrypted}")
    print(f"Should be 'BUNĂȘ': {decrypted == msg}")

def main():
    while True:
        print("\nVigenère Cipher Menu")
        print("1. encrypt a message")
        print("2. decrypt a ciphertext")
        print("3. run test examples")
        print("0. exit")
        choice = input("pick 0/1/2/3: ").strip()

        if choice == '0':
            print("Goodbyeee!")
            sys.exit()

        elif choice == '3':
            run_tests()
            continue

        elif choice not in ['1', '2']:
            print("please pick 0/1/2/3")
            continue

        op = 'encrypt' if choice == '1' else 'decrypt'
        label = "message" if op == 'encrypt' else "ciphertext"

        # Get key
        while True:
            key = input("enter key: ").strip().upper().replace(' ', '')
            if len(key) < 7:
                print("key must be at least 7 characters long")
            elif not validate_input(key):
                print("key must contain only letters A-Z a-z or Romanian special ĂÂÎȘȚ")
            else:
                # Check if all in RO_ALPHABET, since we have special, but input doesn't
                if all(c in RO_ALPHABET for c in key):
                    break
                else:
                    print("key contains invalid characters")

        # Get text
        while True:
            text = input(f"Enter the {label} (letters A-Z a-z or Romanian special only): ").strip().replace(' ', '')
            if not text:
                print("Input cannot be empty")
            elif not validate_input(text):
                print("Input must contain only letters A-Z a-z or Romanian special ĂÂÎȘȚ")
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
