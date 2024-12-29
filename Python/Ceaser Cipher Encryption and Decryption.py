text = input("Enter text: ")
shift = int(input("Enter shift: "))
mode = input("Type 'encrypt' or 'decrypt': ")

cipher_text = ""
for char in text:
    if char.isalpha():
        shift_amount = shift if mode == "encrypt" else -shift
        ascii_offset = 65 if char.isupper() else 97
        new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        cipher_text += new_char
    else:
        cipher_text += char

print(f"The result is: {cipher_text}")
