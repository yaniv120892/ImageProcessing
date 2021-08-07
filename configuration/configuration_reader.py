import configparser


class ConfigurationReader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def get_section_from_config(self, section):
        config = configparser.ConfigParser()
        config.read(self.config_file_path)
        if not config.has_section(section):
            raise Exception(f"{section} doesn't exist in config file")
        return config[section]

    def get_input_path(self, service_name):
        return self.get_section_from_config(service_name)['input_path']

    def get_output_path(self, service_name):
        return self.get_section_from_config(service_name)['output_path']
