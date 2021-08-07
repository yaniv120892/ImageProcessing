import urllib.request
import os

import helpers


class UrlDownloader:
    def __init__(self, logger):
        self.logger = logger

    def try_download(self, url, new_file_path):
        try:
            file_extension = helpers.get_file_extension(url)
            new_file = f"{new_file_path}{file_extension}"
            urllib.request.urlretrieve(url, new_file)
        except Exception as e:
            self.logger.error(f"Failed to download file from {url}, {str(e)}")
            return False
        return True
