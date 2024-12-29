import os

folder_path = input("Enter the folder path: ")
new_name = input("Enter the new name: ")

files = os.listdir(folder_path)
for index, file in enumerate(files):
    file_extension = os.path.splitext(file)[1]
    new_filename = f"{new_name}_{index + 1}{file_extension}"
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_filename))

print("Files renamed successfully!")
