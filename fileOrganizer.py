import os
import shutil
from categories import categories
from datetime import datetime

def create_paths(folder, category):
        path = os.path.join(folder, category)
        os.makedirs(path, exist_ok=True)
        return path

def is_valid_folder(folder):
     return os.path.isdir(folder)

def organize_folder(folder):
    modifications = []
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path) and item != "pyOrganizer.log":
            suffix = os.path.splitext(item)[1]
            found = False
            for category in categories:
                if suffix in categories[category]:
                    found = True
                    break
            if not found:
                category = "Others"
            destination = create_paths(folder, category)
            shutil.move(path, destination)
            destination_file = os.path.join(destination, item)
            relative_destination = os.path.relpath(destination_file, folder)
            modifications.append(item+" → "+relative_destination)
    return modifications

def generate_log(folder, modifications):
    log_path = os.path.join(folder, "pyOrganizer.log")
    date_format = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    headboard = [
        "="*100,
        "MODIFICATION LOG",
        date_format,
        "Guidance = 'file' → 'destination'",
        "="*100,
        ""
    ]
    with open (log_path, "a", encoding="utf-8") as log_file:
        for line in headboard:
            log_file.write(f"{line}\n")
        for line in modifications:
            log_file.write("\n")
            log_file.write(f"{line}\n")
            log_file.write("\n")
        log_file.write(f"Total modifications: {len(modifications)}\n")
        log_file.write("="*100+"\n\n")