import os
from src.config.config import Config
from src.logging.app_logger import AppLogger
from src.service.scraper import Scraper
from src.service.boxscore_service import BoxscoreService
from src.service.freethrow_service import FreethrowService
from src.service.file_service import FileService


class App(object):

    @classmethod
    def go(cls):

        FileService.delete_file("app.log")

        logger = AppLogger.set_up_logger("app.log")
        config = Config.set_up_config(".env")

        Scraper(config).scrape()

        # build the boxscore data
        BoxscoreService(config).collect_boxscore_data()
         
        # analyze FT percentages, losses 5 points or less
        # FreethrowService(config).analyze_close_game_ft_percentages("L")
        # FreethrowService(config).analyze_close_game_ft_percentages("W")





App.go()