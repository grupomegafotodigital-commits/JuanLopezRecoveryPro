import os
from datetime import datetime


class Logger:

    LOG_FOLDER = "logs"

    @staticmethod
    def write(text):

        if not os.path.exists(Logger.LOG_FOLDER):
            os.makedirs(Logger.LOG_FOLDER)

        filename = datetime.now().strftime("%Y%m%d") + ".log"

        path = os.path.join(Logger.LOG_FOLDER, filename)

        with open(path, "a", encoding="utf8") as f:
            hora = datetime.now().strftime("%H:%M:%S")
            f.write(f"[{hora}] {text}\n")
            