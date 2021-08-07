from imageAnalyzer.analyzers.average_rgb_color_analyzer import analyze_image_obj
from imageAnalyzer.analyzers.base_analyzer import AnalyzerBase
import cv2


## I am not sure I understood what exactly this analyzer should return.
# At first, my toght was that I have to convert the image using cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) and just return rgb for this image
# I am getting an exception and don't have more time to fix it/better understand it so I didn't include it in the analyzers
class AverageBlackWhiteColorAnalyzer(AnalyzerBase):
    def analyze(self, file_to_analyzer):
        img = cv2.imread(str(file_to_analyzer))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return analyze_image_obj(img_gray)

    def get_type(self):
        return "Average B/W Color"
