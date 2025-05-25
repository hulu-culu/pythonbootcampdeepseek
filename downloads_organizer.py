import os
import shutil
import logging

# Configure logging
logging.basicConfig(filename='result.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



# Define folders
TARGET_DIRS = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    'Archives': ['.zip', '.tar', '.gz', '.rar']
}

# Create folders if they don’t exist
for folder in TARGET_DIRS:
    os.makedirs(folder, exist_ok=True)

# Source folder (current working directory)
source_folder = os.getcwd()

# Core logic to move files
def get_unique_filename(destination_path):
    """
    If file exists, rename by appending _1, _2, etc.
    """
    base, ext = os.path.splitext(destination_path)
    counter = 1
    while os.path.exists(destination_path):
        destination_path = f"{base}_{counter}{ext}"
        counter += 1
    return destination_path

def move_file(file_path):
    _, filename = os.path.split(file_path)
    file_ext = os.path.splitext(filename)[1].lower()

    for folder, extensions in TARGET_DIRS.items():
        if file_ext in extensions:
            dest_path = os.path.join(source_folder, folder, filename)
            unique_dest = get_unique_filename(dest_path)
            try:
                shutil.move(file_path, unique_dest)
                logging.info(f"Moved: {file_path} -> {unique_dest}")
                print(f"Moved: {file_path} -> {unique_dest}")
            except Exception as e:
                logging.error(f"Failed to move {file_path}: {str(e)}")
                print(f"Failed to move {file_path}: {str(e)}")
            return
    logging.info(f"Skipped (no matching type): {file_path}")
    print(f"Skipped: {file_path}")

# Process all files in the folder
for item in os.listdir(source_folder):
    item_path = os.path.join(source_folder, item)
    if os.path.isfile(item_path):
        move_file(item_path)

