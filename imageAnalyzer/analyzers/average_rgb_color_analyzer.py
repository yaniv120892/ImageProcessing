from imageAnalyzer.analyzers.base_analyzer import AnalyzerBase
import cv2
import numpy


def analyze_image_obj(img):
    avg_color_per_row = numpy.average(img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    return {
        'b': avg_color[0],
        'g': avg_color[1],
        'r': avg_color[2]
    }


class AverageRGBColorAnalyzer(AnalyzerBase):
    def analyze(self, file_to_analyzer):
        img = cv2.imread(str(file_to_analyzer))
        return analyze_image_obj(img)

    def get_type(self):
        return "Average RGB Color"
