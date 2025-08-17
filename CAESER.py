def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Compute base for upper/lowercase to wrap correctly
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Leave non-alphabet characters unchanged
            result += char
    return result


def main():
    print("=== Caesar Cipher Program ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))

    encrypted = caesar_cipher(message, shift, mode='encrypt')
    decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

    print("\n--- Results ---")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")


if __name__ == "__main__":
    main()
