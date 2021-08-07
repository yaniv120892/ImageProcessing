import numpy as np
import imageio
from equirectangularToolbox.nfov import NFOV
from PIL import Image


class GenomicProjectionConverter:
    def __init__(self, logger):
        self.logger = logger

    def try_convert(self, origin_image_full_path, output_image_full_path):
        try:
            img = imageio.imread(origin_image_full_path)
            nfov = NFOV()
            center_point = np.array([0.5, .5])
            np_array_image = nfov.toNFOV(img, center_point)
            im = Image.fromarray(np_array_image)
            im.save(output_image_full_path)
        except Exception as e:
            self.logger.error(
                f"Failed to perform a genomic projection and save for {origin_image_full_path}, {str(e)}")
            return False
        return True
