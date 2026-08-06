# File Organizer

My first Python automation project.

## Goal

Automatically organize files into folders.

## File Organizer V2

The File Organizer automatically organizes files into folders based on their file extensions.

### Features

- Organizes images, documents, music, videos, and archives
- Uses a dictionary to map file extensions to folders
- Creates destination folders automatically
- Moves unknown file types to the `Other` folder
- Ignores folders and processes files only
- Uses a reusable `move_file()` function

### Supported File Types

- Images: `.jpg`, `.jpeg`, `.png`
- Documents: `.pdf`, `.txt`, `.docx`
- Music: `.mp3`, `.wav`
- Videos: `.mp4`, `.mov`
- Archives: `.zip`, `.rar`

## How to Run

1. Put files inside the `test_files` folder.
2. Run:

```bash
python main.py
```

3. The program will automatically move each file to the correct folder.

## Technologies

- Python
- pathlib
- shutil