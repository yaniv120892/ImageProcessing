import pathlib
import os
from . import helpers
from base_service import BaseService


class ImageAnalyzerService(BaseService):
    def __init__(self, output_paths, polling_period_in_seconds, logger,
                 analyzers, file_to_process_handler):
        BaseService.__init__(self, output_paths, polling_period_in_seconds, logger, file_to_process_handler)
        self.analyzers = analyzers

    def process_files(self, file_to_process):
        self.logger.info(f"Start processing {file_to_process}")
        file_name = os.path.basename(file_to_process)
        for output_path in self.output_paths:
            self.analyzer_and_save(file_name, file_to_process, output_path)
        self.logger.info(f"Done processing {file_to_process}")
        self.file_to_process_handler.delete_file(file_to_process)

    def analyzer_and_save(self, file_name, file_to_process, output_path):
        new_file_path = pathlib.Path(output_path, f"{file_name}_analysis.json")
        analysis_obj = {}
        for analyzer in self.analyzers:
            analysis_result = analyzer.analyze(file_to_process)
            if analysis_result is None:
                self.logger.error(f"Failed to analyze {analyzer.get_type()} for {file_to_process}")
            analysis_obj[analyzer.get_type()] = analysis_result
        helpers.write_to_json_file(analysis_obj, new_file_path)
