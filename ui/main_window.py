from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSplitter,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    APP_NAME = "Juan Lopez Recovery Pro"

    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.APP_NAME)
        self.resize(1400, 850)

        self._create_menu()
        self._create_toolbar()
        self._create_statusbar()
        self._create_ui()

    # ----------------------------------------------------
    # MENU
    # ----------------------------------------------------

    def _create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("&Archivo")
        recovery_menu = menu.addMenu("&Recuperación")
        tools_menu = menu.addMenu("&Herramientas")
        help_menu = menu.addMenu("&Ayuda")

        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

    # ----------------------------------------------------
    # TOOLBAR
    # ----------------------------------------------------

    def _create_toolbar(self):

        toolbar = QToolBar()

        toolbar.setMovable(False)

        self.addToolBar(toolbar)

        toolbar.addAction("Escanear")

        toolbar.addAction("Crear Imagen")

        toolbar.addAction("Recuperar JPG")

        toolbar.addAction("Recuperar Todo")

    # ----------------------------------------------------
    # STATUSBAR
    # ----------------------------------------------------

    def _create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Listo")

        self.setStatusBar(status)

    # ----------------------------------------------------
    # UI
    # ----------------------------------------------------

    def _create_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        root = QVBoxLayout()

        central.setLayout(root)

        splitter = QSplitter()

        splitter.setOrientation(Qt.Horizontal)

        root.addWidget(splitter)

        splitter.addWidget(self._left_panel())

        splitter.addWidget(self._right_panel())

        splitter.setSizes([320, 1000])

    # ----------------------------------------------------
    # LEFT PANEL
    # ----------------------------------------------------

    def _left_panel(self):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        title = QLabel("Dispositivos encontrados")

        title.setStyleSheet("font-size:18px;font-weight:bold;")

        layout.addWidget(title)

        self.device_list = QListWidget()

        layout.addWidget(self.device_list)

        self.device_list.addItem("No se ha realizado ningún escaneo.")

        self.scan_button = QPushButton("Escanear dispositivos")

        layout.addWidget(self.scan_button)

        layout.addStretch()

        return widget

    # ----------------------------------------------------
    # RIGHT PANEL
    # ----------------------------------------------------

    def _right_panel(self):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        logo = QLabel("Juan Lopez Recovery Pro")

        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet(
            """
            font-size:28px;
            font-weight:bold;
            padding:20px;
            """
        )

        layout.addWidget(logo)

        info_group = QGroupBox("Información del dispositivo")

        info_layout = QVBoxLayout()

        self.info_box = QTextEdit()

        self.info_box.setReadOnly(True)

        self.info_box.setPlainText(
            """Esperando escaneo...

Seleccione un dispositivo para visualizar la información.
"""
        )

        info_layout.addWidget(self.info_box)

        info_group.setLayout(info_layout)

        layout.addWidget(info_group)

        progress_group = QGroupBox("Progreso")

        progress_layout = QVBoxLayout()

        self.progress = QProgressBar()

        self.progress.setValue(0)

        progress_layout.addWidget(self.progress)

        progress_group.setLayout(progress_layout)

        layout.addWidget(progress_group)

        buttons = QHBoxLayout()

        self.btn_image = QPushButton("Crear Imagen")

        self.btn_jpg = QPushButton("Recuperar JPG")

        self.btn_all = QPushButton("Recuperar Todo")

        buttons.addWidget(self.btn_image)

        buttons.addWidget(self.btn_jpg)

        buttons.addWidget(self.btn_all)

        layout.addLayout(buttons)

        layout.addStretch()

        return widget