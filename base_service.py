import threading
import time
from abc import abstractmethod


class BaseService(threading.Thread):
    def __init__(self, output_paths, polling_period_in_seconds, logger, file_to_process_handler):
        threading.Thread.__init__(self)
        self.file_to_process_handler = file_to_process_handler
        self.should_stop = False
        self.logger = logger
        self.polling_period_in_seconds = polling_period_in_seconds
        self.output_paths = output_paths

    def run(self):
        self.logger.info("Start running")
        while not self.should_stop:
            file_to_process = self.file_to_process_handler.get_file()
            if file_to_process is None:
                self.logger.info("No new files to process")
                time.sleep(self.polling_period_in_seconds)
            else:
                self.process_files(file_to_process)
        self.logger.info("Done running")

    def stop(self):
        self.logger.info("Got stop request, stopping...")
        self.should_stop = True

    @abstractmethod
    def process_files(self, file_to_process):
        pass
