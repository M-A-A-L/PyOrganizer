import os
import shutil
from categories import categories

def create_paths(folder, category):
        path = os.path.join(folder, category)
        os.makedirs(path, exist_ok=True)
        return path

def is_valid_folder(folder):
     return os.path.isdir(folder)

def organize_folder(folder):
    for item in os.listdir(folder):
        path = os.path.join(folder, item)
        if os.path.isfile(path):
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
        