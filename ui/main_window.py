from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QTextEdit,
    QProgressBar,
    QGroupBox,
    QSplitter,
    QStatusBar,
    QToolBar,
)

from core.disk_scanner import DiskScanner
from core.image_creator import ImageCreator


class MainWindow(QMainWindow):

    APP_NAME = "Juan Lopez Recovery Pro"

    def __init__(self):
        super().__init__()

        self.disks = []

        self.setWindowTitle(self.APP_NAME)
        self.resize(1400, 850)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()
        self.create_ui()

        self.scan_button.clicked.connect(self.scan_disks)
        self.device_list.itemClicked.connect(self.show_disk_info)
        self.btn_image.clicked.connect(self.create_disk_image)

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
    # STATUSBAR
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

        splitter.addWidget(self.left_panel())
        splitter.addWidget(self.right_panel())

        splitter.setSizes([320, 1000])

        layout.addWidget(splitter)
            # -------------------------------------------------
    # PANEL IZQUIERDO
    # -------------------------------------------------

    def left_panel(self):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        titulo = QLabel("Dispositivos encontrados")
        titulo.setStyleSheet(
            "font-size:18px;font-weight:bold;"
        )

        layout.addWidget(titulo)

        self.device_list = QListWidget()
        layout.addWidget(self.device_list)

        self.device_list.addItem(
            "Pulse 'Escanear dispositivos' para comenzar."
        )

        self.scan_button = QPushButton(
            "Escanear dispositivos"
        )

        layout.addWidget(self.scan_button)

        layout.addStretch()

        return widget

    # -------------------------------------------------
    # PANEL DERECHO
    # -------------------------------------------------

    def right_panel(self):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        titulo = QLabel(self.APP_NAME)

        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:15px;
        """)

        layout.addWidget(titulo)

        info_group = QGroupBox("Información del dispositivo")

        info_layout = QVBoxLayout()

        self.info_box = QTextEdit()

        self.info_box.setReadOnly(True)

        self.info_box.setPlainText(
            "Esperando escaneo..."
        )

        info_layout.addWidget(self.info_box)

        info_group.setLayout(info_layout)

        layout.addWidget(info_group)

        progreso = QGroupBox("Progreso")

        progreso_layout = QVBoxLayout()

        self.progress = QProgressBar()

        self.progress.setValue(0)

        progreso_layout.addWidget(self.progress)

        progreso.setLayout(progreso_layout)

        layout.addWidget(progreso)

        botones = QHBoxLayout()

        self.btn_image = QPushButton("Crear Imagen")
        self.btn_jpg = QPushButton("Recuperar JPG")
        self.btn_all = QPushButton("Recuperar Todo")

        botones.addWidget(self.btn_image)
        botones.addWidget(self.btn_jpg)
        botones.addWidget(self.btn_all)

        layout.addLayout(botones)

        layout.addStretch()

        return widget
            # -------------------------------------------------
    # ESCANEAR DISPOSITIVOS
    # -------------------------------------------------

    def scan_disks(self):

        self.device_list.clear()
        self.progress.setValue(0)

        try:
            scanner = DiskScanner()

            self.disks = scanner.scan()

            if not self.disks:
                self.device_list.addItem("No se encontraron dispositivos.")
                self.info_box.setPlainText(
                    "No se encontraron dispositivos."
                )
                return

            for disk in self.disks:

                size_gb = disk["size"] / (1024 ** 3)

                self.device_list.addItem(
                    f'{disk["model"]} ({size_gb:.2f} GB)'
                )

            self.progress.setValue(100)

            self.info_box.setPlainText(
                f"Se encontraron {len(self.disks)} dispositivo(s).\n\n"
                "Seleccione uno para visualizar la información."
            )

            self.statusBar().showMessage("Escaneo finalizado")

        except Exception as e:

            self.info_box.setPlainText(str(e))

            self.statusBar().showMessage("Error durante el escaneo")

    # -------------------------------------------------
    # MOSTRAR INFORMACIÓN DEL DISCO
    # -------------------------------------------------

    def show_disk_info(self, item):

        index = self.device_list.currentRow()

        if index < 0:
            return

        if index >= len(self.disks):
            return

        disk = self.disks[index]

        texto = f"""
        def create_disk_image(self):

    if not self.disks:
        QMessageBox.warning(
            self,
            "Sin dispositivo",
            "Primero debe escanear y seleccionar un disco."
        )
        return

    filename, _ = QFileDialog.getSaveFileName(
        self,
        "Guardar imagen",
        "backup.img",
        "Imagen (*.img)"
    )

    if not filename:
        return

    QMessageBox.information(
        self,
        "En desarrollo",
        (
            "La interfaz ya está lista.\n\n"
            "En el siguiente paso conectaremos el motor "
            "de creación de imágenes."
        )
    )
MODELO
-------------------------
{disk.get("model", "")}

CAPACIDAD
-------------------------
{disk.get("size", 0) / (1024 ** 3):.2f} GB

INTERFAZ
-------------------------
{disk.get("interface", "")}

FABRICANTE
-------------------------
{disk.get("manufacturer", "")}

SERIAL
-------------------------
{disk.get("serial", "")}

PARTICIONES
-------------------------
{disk.get("partitions", "")}

SECTORES
-------------------------
{disk.get("sectors", ""):,}

DEVICE ID
-------------------------
{disk.get("deviceid", "")}
"""

        self.info_box.setPlainText(texto)