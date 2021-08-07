import pathlib
import os
from base_service import BaseService


class ImageEdgeDetectionService(BaseService):
    def __init__(self, output_paths, polling_period_in_seconds, logger,
                 edge_detection_extractor, file_to_process_handler):
        BaseService.__init__(self, output_paths, polling_period_in_seconds, logger, file_to_process_handler)
        self.edge_detection_extractor = edge_detection_extractor

    def process_files(self, file_to_process):
        self.logger.info(f"Start processing {file_to_process}")
        file_name = os.path.basename(file_to_process)
        for output_path in self.output_paths:
            self.extract_edge_detection_and_save(file_name, file_to_process, output_path)
        self.logger.info(f"Done processing {file_to_process}")
        self.file_to_process_handler.delete_file(file_to_process)

    def extract_edge_detection_and_save(self, file_name, file_to_process, output_path):
        new_file_path = pathlib.Path(output_path, f"projection_{file_name}")
        if not self.edge_detection_extractor.try_extract(file_to_process, new_file_path):
            self.logger.error(f"Failed to extract edge detection for {file_to_process}")
