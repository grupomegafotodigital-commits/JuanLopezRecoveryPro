from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
from controllers.recovery_controller import RecoveryController
from core.logger import Logger

from ui.panels.left_panel import LeftPanel
from ui.panels.right_panel import RightPanel


class MainWindow(QMainWindow):

    APP_NAME = "Juan Lopez Recovery Pro"

    def __init__(self):
        super().__init__()

        self.disks = []
        self.controller = RecoveryController()

        self.setWindowTitle(self.APP_NAME)
        self.resize(1400, 850)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()
        self.create_ui()

        # Conexiones
        self.left_panel.scan_button.clicked.connect(self.scan_disks)
        self.left_panel.device_list.itemClicked.connect(self.show_disk_info)

        self.right_panel.btn_image.clicked.connect(
            self.create_disk_image
        )

    # -------------------------------------------------
    # MENU
    # -------------------------------------------------

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("&Archivo")
        menu.addMenu("&Recuperación")
        menu.addMenu("&Herramientas")
        menu.addMenu("&Ayuda")

        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

    # -------------------------------------------------
    # TOOLBAR
    # -------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar()

        toolbar.setMovable(False)

        self.addToolBar(toolbar)

        toolbar.addAction("Escanear")
        toolbar.addAction("Crear Imagen")
        toolbar.addAction("Recuperar JPG")
        toolbar.addAction("Recuperar Todo")

    # -------------------------------------------------
    # STATUS BAR
    # -------------------------------------------------

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Listo")

        self.setStatusBar(status)
            # -------------------------------------------------
    # INTERFAZ
    # -------------------------------------------------

    def create_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        splitter = QSplitter(Qt.Horizontal)

        self.left_panel = LeftPanel()
        self.right_panel = RightPanel()

        splitter.addWidget(self.left_panel)
        splitter.addWidget(self.right_panel)

        splitter.setSizes([320, 1000])

        layout.addWidget(splitter)
            # -------------------------------------------------
    # ESCANEAR DISPOSITIVOS
    # -------------------------------------------------

    def scan_disks(self):

        self.left_panel.device_list.clear()
        self.right_panel.progress.setValue(0)

        Logger.info("Iniciando escaneo de dispositivos")

        try:

            self.disks = self.controller.scan_disks()

            if not self.disks:

                self.left_panel.device_list.addItem(
                    "No se encontraron dispositivos."
                )

                self.right_panel.info_box.setPlainText(
                    "No se encontraron dispositivos."
                )

                Logger.warning("No se encontraron dispositivos")

                return

            for disk in self.disks:

                size_gb = disk.size / (1024 ** 3)

                self.left_panel.device_list.addItem(
                    f"{disk.model} ({size_gb:.2f} GB)"
                )

            self.right_panel.progress.setValue(100)

            self.right_panel.info_box.setPlainText(
                f"Se encontraron {len(self.disks)} dispositivo(s).\n\n"
                "Seleccione uno para visualizar la información."
            )

            self.statusBar().showMessage("Escaneo finalizado")

            Logger.info(
                f"Escaneo finalizado. {len(self.disks)} dispositivo(s) encontrados."
            )

        except Exception as e:

            Logger.error(str(e))

            self.right_panel.info_box.setPlainText(str(e))

            self.statusBar().showMessage("Error durante el escaneo")

    # -------------------------------------------------
    # MOSTRAR INFORMACIÓN DEL DISCO
    # -------------------------------------------------

    def show_disk_info(self, item):

        index = self.left_panel.device_list.currentRow()

        if index < 0 or index >= len(self.disks):
            return

        disk = self.disks[index]

        texto = f"""
MODELO
-------------------------
{disk.model}

CAPACIDAD
-------------------------
{disk.size / (1024 ** 3):.2f} GB

INTERFAZ
-------------------------
{disk.interface}

FABRICANTE
-------------------------
{disk.manufacturer}

SERIAL
-------------------------
{disk.serial}

PARTICIONES
-------------------------
{disk.partitions}

SECTORES
-------------------------
{disk.sectors:,}

DEVICE ID
-------------------------
{disk.deviceid}
"""

        self.right_panel.info_box.setPlainText(texto)

        Logger.info(f"Dispositivo seleccionado: {disk.model}")
            # -------------------------------------------------
    # CREAR IMAGEN DEL DISCO
    # -------------------------------------------------

    def create_disk_image(self):

        if not self.disks:

            QMessageBox.warning(
                self,
                "Sin dispositivo",
                "Primero debe escanear y seleccionar un disco."
            )

            return

        index = self.left_panel.device_list.currentRow()

        if index < 0:

            QMessageBox.warning(
                self,
                "Sin selección",
                "Seleccione un dispositivo."
            )

            return

        disk = self.disks[index]

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar imagen",
            "backup.img",
            "Imagen (*.img)"
        )

        if not filename:
            return

        Logger.info(f"Creación de imagen iniciada: {disk.deviceid}")

        self.right_panel.progress.setValue(0)

        try:

            resultado = self.controller.create_image(
    disk,
    filename,
    self.right_panel.progress.setValue,
)

            self.right_panel.progress.setValue(100)

            Logger.info(f"Imagen creada correctamente: {filename}")

            QMessageBox.information(
    self,
    "Proceso finalizado",
    (
        "La imagen se creó correctamente.\n\n"
        f"SHA-256:\n{resultado['sha256']}"
    )
)

        except Exception as e:

            Logger.error(str(e))

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )