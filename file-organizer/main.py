import shutil
from pathlib import Path

folder = Path("test_files")

files = folder.iterdir()

images_folder = folder / "Images"
images_folder.mkdir(exist_ok=True)

documents_folder = folder / "Documents"
documents_folder.mkdir(exist_ok=True)

music_folder = folder / "Music"
music_folder.mkdir(exist_ok=True)

for file in folder.iterdir():
    extension = file.suffix.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        print(f"{file.name} -> Images")
        destination = images_folder / file.name
        shutil.move(file, destination)
        print(destination)

    elif extension in [".mp3", ".wav"]:
        print(f"{file.name} -> Music")
        destination = music_folder / file.name
        shutil.move(file, destination)
        print(destination)


    elif extension in [".mp4", ".mov"]:
        print(f"{file.name} -> Videos")

    elif extension in [".pdf", ".txt", ".docx"]:
        print(f"{file.name} -> Documents")
        destination = documents_folder / file.name
        shutil.move(file, destination)
        print(destination)

    elif extension in [".zip", ".rar"]:
        print(f"{file.name} -> Archives")

    else:
        print(f"{file.name} -> Other")