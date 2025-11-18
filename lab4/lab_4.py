import random
import sys
import time

# des initial permutation table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


def validate_input(text):
    """validate that input contains only printable ASCII characters"""
    return all(32 <= ord(c) <= 126 for c in text)


def text_to_binary(text):
    """convert 8 characters to 64-bit binary string"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary


def apply_permutation(bits, table):
    """apply permutation table to bit string"""
    return ''.join(bits[i - 1] for i in table)


def format_binary_output(bits, bits_per_group=4, groups_per_line=8):
    """format binary string for readable output"""
    result = []
    for i in range(0, len(bits), bits_per_group):
        result.append(bits[i:i + bits_per_group])

    formatted = []
    for i in range(0, len(result), groups_per_line):
        formatted.append(' '.join(result[i:i + groups_per_line]))

    return '\n'.join(formatted)


def compute_L1(message):
    print("\n" + "=" * 60)
    print(f"\n1. INPUT MESSAGE:")
    print(f"   '{message}'")
    print(f"   ASCII values: {[ord(c) for c in message]}")
    time.sleep(1)

    # convert to binary
    binary_message = text_to_binary(message)
    print(f"\n2. BINARY REPRESENTATION (64 bits):")
    print(f"   {format_binary_output(binary_message)}")
    time.sleep(1)

    print(f"\n3. INITIAL PERMUTATION TABLE:")
    for i in range(0, len(IP), 8):
        print(f"   {IP[i:i+8]}")
    time.sleep(1)

    # apply initial permutation
    permuted = apply_permutation(binary_message, IP)
    print(f"\n4. AFTER INITIAL PERMUTATION (64 bits):")
    print(f"   {format_binary_output(permuted)}")
    time.sleep(1)

    L0 = permuted[:32]
    R0 = permuted[32:]

    print(f"\n5. SPLIT INTO L0 AND R0:")
    print(f"   L0 (32 bits):")
    print(f"   {format_binary_output(L0)}")
    print(f"\n   R0 (32 bits):")
    print(f"   {format_binary_output(R0)}")
    time.sleep(1)

    L1 = R0

    print(f"\n6. COMPUTE L1:")
    print(f"   According to DES algorithm: L1 = R0")
    print(f"\n   L1 (32 bits):")
    print(f"   {format_binary_output(L1)}")
    time.sleep(1)

    L1_hex = hex(int(L1, 2))[2:].upper().zfill(8)
    print(f"\n   L1 (hexadecimal): {L1_hex}")
    time.sleep(1)

    print("\n" + "=" * 60)

    return L1


def main():
    while True:
        print("\nDES Algorithm:")
        print("1. Enter custom 8-character message")
        print("2. Generate random 8-character message")
        print("0. Exit")
        choice = input("Choose 0/1/2: ").strip()

        if choice == '0':
            print("byeeeee!")
            sys.exit()

        elif choice not in ['1', '2']:
            print("Please choose 0, 1, or 2.")
            continue

        if choice == '1':
            while True:
                message = input("Enter 8-character message: ").strip()
                if len(message) != 8:
                    print("Error: Message must be exactly 8 characters!")
                elif not validate_input(message):
                    print("Error: Message must contain only printable ASCII characters!")
                else:
                    break
        else:
            # generate random
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            message = ''.join(random.choice(chars) for _ in range(8))

        L1 = compute_L1(message)

if __name__ == "__main__":
    main()
