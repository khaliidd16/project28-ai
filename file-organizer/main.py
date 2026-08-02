from pathlib import Path

folder = Path("test_files")

files = folder.iterdir()

for file in folder.iterdir():
    print(f"Name: {file.name}")
    print(f"Stem: {file.stem}")
    print(f"Extension: {file.suffix}")
    print("----------------")