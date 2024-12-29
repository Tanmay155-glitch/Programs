key = 3  # Example key for Caesar cipher
mode = input("Type 'encrypt' or 'decrypt': ")
file_path = input("Enter file path: ")

with open(file_path, 'r') as file:
    content = file.read()

result = ""
for char in content:
    if char.isalpha():
        shift = key if mode == 'encrypt' else -key
        ascii_offset = 65 if char.isupper() else 97
        new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        result += new_char
    else:
        result += char

with open(file_path, 'w') as file:
    file.write(result)

print(f"File {mode}ed successfully!")
