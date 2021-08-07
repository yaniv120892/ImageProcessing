import pathlib
import os
from base_service import BaseService


class ImageProjectionService(BaseService):
    def __init__(self, output_paths, polling_period_in_seconds, logger,
                 genomic_projection_converter, file_to_process_handler):
        BaseService.__init__(self, output_paths, polling_period_in_seconds, logger, file_to_process_handler)
        self.genomic_projection_converter = genomic_projection_converter

    def process_files(self, file_to_process):
        self.logger.info(f"Start processing {file_to_process}")
        file_name = os.path.basename(file_to_process)
        for output_path in self.output_paths:
            self.genomic_projection_convert_and_save(file_name, file_to_process, output_path)
        self.logger.info(f"Done processing {file_to_process}")
        self.file_to_process_handler.delete_file(file_to_process)

    def genomic_projection_convert_and_save(self, file_name, file_to_process, output_path):
        new_file_path = pathlib.Path(output_path, f"projection_{file_name}")
        if not self.genomic_projection_converter.try_convert(file_to_process, new_file_path):
            self.logger.error(f"Failed to perform genomic projection for {file_to_process}")
