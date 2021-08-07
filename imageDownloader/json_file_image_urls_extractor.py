from . import helpers
from imageDownloader.image_urls_extractor import ImageUrlsExtractor


class JsonFileImageUrlsExtractor(ImageUrlsExtractor):
    def __init__(self, logger):
        self.logger = logger

    def extract(self, file_full_path):
        json_object = helpers.json_file_reader(file_full_path)
        if "image_list" in json_object:
            return json_object["image_list"]
        else:
            self.logger.error(f"Failed to extract images list from {file_full_path}")
            return []


