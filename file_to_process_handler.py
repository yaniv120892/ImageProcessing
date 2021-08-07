import helpers
import os
import pathlib


class FileToProcessHandler:
    def __init__(self, input_folder, extension_file=""):
        self.input_folder = input_folder
        self.extension_file = extension_file

    def get_file(self):
        files = helpers.get_files_in_folder(self.input_folder, self.extension_file)
        if len(files) > 0:
            return files[0]
        return None

    @staticmethod
    def delete_file(file_to_delete):
        os.remove(file_to_delete)

    @staticmethod
    def mark_as_invalid(file_to_set):
        file_name = os.path.basename(file_to_set)
        new_file_name = f"invalid_{file_name}"
        file_path = pathlib.Path(__file__).parent.resolve()
        os.rename(file_to_set, pathlib.Path(file_path, new_file_name))
