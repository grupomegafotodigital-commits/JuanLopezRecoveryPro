from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QProgressBar,
    QPushButton,
    QGroupBox,
)


class RightPanel(QWidget):

    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Juan Lopez Recovery Pro")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            padding:15px;
        """)

        layout.addWidget(title)

        info_group = QGroupBox("Información del dispositivo")
        info_layout = QVBoxLayout()

        self.info_box = QTextEdit()
        self.info_box.setReadOnly(True)
        self.info_box.setPlainText("Esperando escaneo...")

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