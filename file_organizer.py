import os
import shutil


def organize_folder(path):
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # remove the dot

        if extension:
            if not os.path.exists(path + '/' + extension):
                os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    print("Folder Organized!")

# Usage: Put the path to your messy folder here
# organize_folder('/Users/yourname/Downloads')