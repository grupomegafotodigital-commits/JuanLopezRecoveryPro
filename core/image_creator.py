import hashlib
import os
import time

from core.logger import Logger


class ImageCreator:

    BUFFER_SIZE = 1024 * 1024  # 1 MB

    def __init__(self):

        self.cancelled = False

    def cancel(self):

        self.cancelled = True

    def create_image(
        self,
        source_path,
        destination_path,
        total_size,
        progress_callback=None,
    ):

        Logger.info(f"Iniciando imagen de {source_path}")

        copied = 0

        start_time = time.time()

        sha256 = hashlib.sha256()

        with open(source_path, "rb") as source:

            with open(destination_path, "wb") as destination:

                while True:

                    if self.cancelled:

                        Logger.warning("Proceso cancelado")

                        return False

                    data = source.read(self.BUFFER_SIZE)

                    if not data:
                        break

                    destination.write(data)

                    sha256.update(data)

                    copied += len(data)

                    if progress_callback:

                        percent = int((copied / total_size) * 100)

                        progress_callback(percent)

        elapsed = time.time() - start_time

        Logger.info(
            f"Imagen creada correctamente en {elapsed:.2f} segundos"
        )

        Logger.info(
            f"SHA256: {sha256.hexdigest()}"
        )

        return {
            "path": destination_path,
            "sha256": sha256.hexdigest(),
            "seconds": elapsed,
        }