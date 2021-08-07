import pathlib
import uuid
from base_service import BaseService


class ImageDownloaderService(BaseService):
    def __init__(self, output_paths, polling_period_in_seconds, logger,
                 image_downloader, file_to_process_handler, image_url_extractor):
        BaseService.__init__(self, output_paths, polling_period_in_seconds, logger, file_to_process_handler)
        self.image_urls_extractor = image_url_extractor
        self.image_downloader = image_downloader

    def process_files(self, file_to_process):
        self.logger.info(f"Start processing {file_to_process}")
        image_urls = self.image_urls_extractor.extract(file_to_process)
        for image_url in image_urls:
            self.download_and_save_image(image_url, file_to_process)
        self.logger.info(f"Done processing {file_to_process}")
        self.file_to_process_handler.delete_file(file_to_process)

    def download_and_save_image(self, image_url, file_to_process):
        str_uuid = str(uuid.uuid4())
        for output_path in self.output_paths:
            new_file_path = pathlib.Path(output_path, str_uuid)
            if not self.image_downloader.try_download(image_url, new_file_path):
                self.logger.error(f"Failed to download {image_url} that included in {file_to_process}")
