# PROGRAM: Caesar Cipher

from arts import logo

# Defining the alphabet list with repeated alphabets for easy shift calculation
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 3
# Multiplying to avoid IndexError for large shifts


def main():
    print(logo)  # Print the logo at the beginning
    should_continue = True
    while should_continue:
        # Get the user's choice for encoding or decoding
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower().strip()
        text = input("Type your message:-\n").lower()    # Get the message to encode/decode
        shift = int(input("Type the shift number: "))   # Get the shift amount

        if shift > 52:
            shift = shift % 26
        caesar(user_text=text, shift_amount=shift, cipher_direction=direction)

        # Ask if the user wants to go again
        result = input("Type 'yes' to continue, type 'no' to exit: ").lower().strip()
        if result == "no":
            should_continue = False  # Exit the loop if the user types 'no'
            print("Goodbye!")


def caesar(user_text, shift_amount, cipher_direction):
    modified_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in user_text:
        if char in alphabet:    # Check if the character is in the alphabet
            position = alphabet.index(char)  # Get the current position
            new_position = position + shift_amount  # Calculate the new position
            modified_text += alphabet[new_position]  # Append the shifted character to result
        else:
            modified_text += char  # Append non-alphabet characters unchanged
    print(f"The {cipher_direction}d text is:-\n{modified_text}\n")


# Entry point
if __name__ == "__main__":
    main()
