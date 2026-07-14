import os


class ImageCreator:
    """
    Crea una imagen binaria (.img) de un dispositivo.

    Esta es una primera versión.
    Más adelante agregaremos:
    - Barra de progreso
    - Cancelar
    - Pausar
    - Reanudar
    - Verificación CRC
    - Hash MD5/SHA256
    """

    BUFFER_SIZE = 1024 * 1024  # 1 MB

    def __init__(self):
        self.cancelled = False

    def cancel(self):
        self.cancelled = True

    def create_image(self, source_path, destination_path, progress_callback=None):
        """
        source_path:
            Ejemplo:
            \\\\.\\PhysicalDrive1

        destination_path:
            Ejemplo:
            D:\\Backup\\sdcard.img
        """

        total_size = os.path.getsize(source_path)

        copied = 0

        with open(source_path, "rb") as source:

            with open(destination_path, "wb") as destination:

                while True:

                    if self.cancelled:
                        return False

                    data = source.read(self.BUFFER_SIZE)

                    if not data:
                        break

                    destination.write(data)

                    copied += len(data)

                    if progress_callback:

                        percent = int((copied / total_size) * 100)

                        progress_callback(percent)

        return destination_path