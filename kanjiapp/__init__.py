import os

class App:

    def __init__(self):
        os.environ["VERSION"] = "0.1.0" # will use dotenv for a config file in the near future

    def start(self):
        """ Start program execution """