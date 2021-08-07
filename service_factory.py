import consts
import helpers
from configuration.configuration_reader import ConfigurationReader
from file_to_process_handler import FileToProcessHandler
from imageAnalyzer.analyzers.average_rgb_color_analyzer import AverageRGBColorAnalyzer
from imageAnalyzer.analyzers.dimensions_analyzers import DimensionAnalyzer
from imageAnalyzer.image_analyzer_service import ImageAnalyzerService
from imageDownloader.image_downloader_service import ImageDownloaderService
from imageDownloader.json_file_image_urls_extractor import JsonFileImageUrlsExtractor
from imageDownloader.url_image_downloader import UrlDownloader
from imageEdgeDetection.edge_detection_extractor import EdgeDetectionExtractor
from imageEdgeDetection.image_edge_detection_service import ImageEdgeDetectionService
from imageProjection.genomic_projection_converter import GenomicProjectionConverter
from imageProjection.image_projection_service import ImageProjectionService


def create_image_downloader_service(logger, input_path, output_paths):
    image_downloader = UrlDownloader(logger)
    file_to_process_handler = FileToProcessHandler(input_path, '.json')
    image_url_extractor = JsonFileImageUrlsExtractor(logger)
    return ImageDownloaderService(output_paths, consts.POLLING_PERIOD_IN_SECONDS, logger,
                                  image_downloader, file_to_process_handler,
                                  image_url_extractor)


def create_detection_extractor_service(logger, input_path, output_paths):
    file_to_process_handler = FileToProcessHandler(input_path)
    edge_detection_extractor = EdgeDetectionExtractor(logger)
    return ImageEdgeDetectionService(output_paths, consts.POLLING_PERIOD_IN_SECONDS, logger,
                                     edge_detection_extractor, file_to_process_handler)


def create_image_projector_service(logger, input_path, output_paths):
    file_to_process_handler = FileToProcessHandler(input_path)
    genomic_projection_converter = GenomicProjectionConverter(logger)
    return ImageProjectionService(output_paths, consts.POLLING_PERIOD_IN_SECONDS, logger,
                                  genomic_projection_converter, file_to_process_handler)


def create_image_analyzer_service(logger, input_path, output_paths):
    file_to_process_handler = FileToProcessHandler(input_path)
    analyzer = [DimensionAnalyzer(), AverageRGBColorAnalyzer()]
    return ImageAnalyzerService(output_paths, consts.POLLING_PERIOD_IN_SECONDS, logger,
                                analyzer, file_to_process_handler)


def create_service(service_name, logger):
    try:
        configuration_reader = ConfigurationReader('config.ini')
        input_path = configuration_reader.get_input_path(service_name)
        helpers.assert_folder_exists(input_path)
        output_paths_str = configuration_reader.get_output_path(service_name)
        output_paths = output_paths_str.split(',')
        for output_path in output_paths:
            helpers.assert_folder_exists(output_path)
    except Exception as e:
        logger.error(f"Failed to load input and output files, {str(e)}")
        return None

    if service_name == "ImageDownloader":
        return create_image_downloader_service(logger, input_path, output_paths)
    if service_name == "ImageEdgeDetection":
        return create_detection_extractor_service(logger, input_path, output_paths)
    if service_name == "ImageProjector":
        return create_image_projector_service(logger, input_path, output_paths)
    if service_name == "ImageAnalyzer":
        return create_image_analyzer_service(logger, input_path, output_paths)
    logger.error(f"Service name not supported {service_name}")
    raise Exception(f"Unknown service name {service_name}")
