import configparser


class Config:

    config = configparser.ConfigParser()
    config.read("config/config.ini")

    BASE_URL = config["DEFAULT"]["BASE_URL"]

    HEADLESS = config.getboolean("DEFAULT", "HEADLESS")

    VIEWPORT_WIDTH = config.getint("DEFAULT", "VIEWPORT_WIDTH")

    VIEWPORT_HEIGHT = config.getint("DEFAULT", "VIEWPORT_HEIGHT")

    TIMEOUT = config.getint("DEFAULT", "TIMEOUT")