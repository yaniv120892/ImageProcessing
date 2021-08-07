from PIL import Image
from imageAnalyzer.analyzers.base_analyzer import AnalyzerBase


class DimensionAnalyzer(AnalyzerBase):
    def analyze(self, file_to_analyzer):
        image = Image.open(file_to_analyzer)
        width, height = image.size
        return {"width": width, "height": height}

    def get_type(self):
        return "Dimension"

