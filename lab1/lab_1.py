def caesar_cipher(msg, key, op):
    # prepare message: uppercase, remove spaces
    msg = msg.upper().replace(' ', '')
    normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for char in msg:
        if char.isalpha():
            # find position in alphabet
            pos = normal.index(char)
            if op == 'encrypt':
                new_pos = (pos + key) % 26
            elif op == 'decrypt':
                new_pos = (pos - key) % 26
            # get shifted letter
            result.append(normal[new_pos])
    return ''.join(result)

def build_permuted_alphabet(perm_key):
    # use set to avoid duplicates
    seen = set()
    perm = []
    # add unique letters from key
    for c in perm_key.upper():
        if c not in seen:
            perm.append(c)
            seen.add(c)
    # add remaining alphabet letters
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in seen:
            perm.append(c)
            seen.add(c)
    return ''.join(perm)

def caesar_with_perm(msg, shift_key, perm_key, op):
    # prepare message: uppercase, remove spaces
    msg = msg.upper().replace(' ', '')
    # build permuted alphabet
    perm_alphabet = build_permuted_alphabet(perm_key)
    normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for c in msg:
        if c.isalpha():
            if op == 'encrypt':
                # find normal position, shift, get permuted letter
                pos = normal.index(c)
                new_pos = (pos + shift_key) % 26
                result.append(perm_alphabet[new_pos])
            elif op == 'decrypt':
                # find permuted position, unshift, get normal letter
                pos = perm_alphabet.index(c)
                new_pos = (pos - shift_key) % 26
                result.append(normal[new_pos])
    return ''.join(result)

def main():
    while True:
        print("1. standard caesar cipher")
        print("2. caesar with permutation")
        print("0. exit")
        choice = input("pick 0/1/2: ").strip()

        if choice == '0':
            print("byeeee!")
            break
        elif choice not in ['1', '2']:
            print("please choose 0/1/2")
            continue

        while True:
            op = input("encrypt or decrypt? (e/d): ").strip().lower()
            if op in ['e', 'encrypt']:
                op = 'encrypt'
                break
            elif op in ['d', 'decrypt']:
                op = 'decrypt'
                break
            else:
                continue

        while True:
            msg = input("enter the message: ").strip()
            if msg:
                break
            else:
                print("message can't be empty, try again")

        if choice == '1':
            while True:
                try:
                    key = int(input("enter key (1-25): ").strip())
                    if 1 <= key <= 25:
                        break
                    else:
                        print("key must be 1-25")
                except ValueError:
                    print("enter a number")

            result = caesar_cipher(msg, key, op)
            print(f"result: {result}")

        elif choice == '2':
            while True:
                try:
                    shift_key = int(input("enter shift key (1-25): ").strip())
                    if 1 <= shift_key <= 25:
                        break
                    else:
                        print("shift key must be 1-25")
                except ValueError:
                    print("enter a number")

            while True:
                perm_key = input("enter permutation word (at least 7 letters): ").strip().upper()
                if len(set(perm_key)) >= 7 and all(c.isalpha() for c in perm_key) and perm_key:
                    break
                else:
                    print("need at least 7 unique letters")

            result = caesar_with_perm(msg, shift_key, perm_key, op)
            print(f"result: {result}")

if __name__ == "__main__":
    main()
