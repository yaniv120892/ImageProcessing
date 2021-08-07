import cv2
import helpers
from PIL import Image


class EdgeDetectionExtractor:
    def __init__(self, logger):
        self.logger = logger

    def try_extract(self, origin_image_full_path, output_image_full_path):
        try:
            height = 100
            width = 150
            file_extension = helpers.get_file_extension(origin_image_full_path)
            if file_extension == ".png":
                width = 200
            img = cv2.imread(str(origin_image_full_path))
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
            edges = cv2.Canny(image=img_blur, threshold1=height, threshold2=width)
            im = Image.fromarray(edges)
            im.save(output_image_full_path)
        except Exception as e:
            self.logger.error(
                f"Failed to extract edge detection and save for {origin_image_full_path}, {str(e)}")
            return False
        return True




