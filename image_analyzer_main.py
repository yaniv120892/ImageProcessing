import logger_initializer
import service_factory

service_name = "ImageAnalyzer"


def wait_for_exit_input(logger):
    while input() != "exit":
        print("Enter 'exit' to stop execution")
    logger.info("got exit request")


def main():
    logger = logger_initializer.initialize_logger()
    service = service_factory.create_service(service_name, logger)
    logger.info(f"Start {service_name} service")
    service.start()
    wait_for_exit_input(logger)
    logger.info(f"Stopping {service_name} service")
    service.stop()
    service.join()
    logger.info(f"{service_name} service stopped")


if __name__ == '__main__':
    main()
