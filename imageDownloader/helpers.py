import json


def json_file_reader(file_full_path):
    f = open(file_full_path, )
    data = json.load(f)
    return data
