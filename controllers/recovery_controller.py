from core.disk_scanner import DiskScanner
from core.image_creator import ImageCreator
from core.logger import Logger


class RecoveryController:

    def __init__(self):
        self.scanner = DiskScanner()
        self.image_creator = ImageCreator()

    def scan_disks(self):

        Logger.info("Escaneando dispositivos...")

        return self.scanner.scan()

    def create_image(
        self,
        disk,
        destination,
        progress_callback=None,
    ):

        Logger.info(
            f"Creando imagen de {disk.deviceid}"
        )

        return self.image_creator.create_image(
            source_path=disk.deviceid,
            destination_path=destination,
            total_size=disk.size,
            progress_callback=progress_callback,
        )