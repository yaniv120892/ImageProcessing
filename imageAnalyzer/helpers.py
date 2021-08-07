import json


def write_to_json_file(obj, file_to_write):
    json_string = json.dumps(obj)
    json_file = open(file_to_write, "w")
    json_file.write(json_string)
    json_file.close()
