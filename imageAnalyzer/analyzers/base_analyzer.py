from abc import ABC, abstractmethod


class AnalyzerBase(ABC):
    @abstractmethod
    def analyze(self, file_to_analyzer):
        pass

    @abstractmethod
    def get_type(self):
        pass


