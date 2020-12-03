from loguru import logger

from src.objects.factory import create_app


def main():
    logger.info("Start flask application")
    app = create_app()


if __name__ == '__main__':
    main()
