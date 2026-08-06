import shutil
from pathlib import Path

folder = Path("test_files")

# print("Enter your name...")
# name = input()

# def greet_user(user_name):
#     print("Welcome, ", user_name)

# greet_user(name)

file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".zip": "Archives",
    ".rar": "Archives"
}


def move_file(file, folder):
    destination = folder / file.name
    shutil.move(file, destination)


for file in folder.iterdir():

    if file.is_file():

        # Get the file extension
        extension = file.suffix.lower()

        # Find which folder the file belongs to
        folder_name = file_types.get(extension, "Other")

        # Create the destination path
        destination_folder = folder / folder_name

        # Create the folder if it doesn't exist
        destination_folder.mkdir(exist_ok=True)

        # Move the file
        move_file(file, destination_folder)

        print(f"{file.name} -> {folder_name}")