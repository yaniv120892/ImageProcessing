import os
import pathlib


def assert_folder_exists(folder_name):
    if not os.path.isdir(folder_name):
        raise Exception(f"folder {folder_name} doesn't exist")


def get_files_in_folder(folder_name, extension):
    files = []
    for file in os.listdir(folder_name):
        file_full_path = pathlib.Path(folder_name, file)
        if extension == "":
            files.append(file_full_path)
        elif file.endswith(extension):
            files.append(file_full_path)
    return files


def get_file_extension(file):
    return os.path.splitext(file)[-1]

