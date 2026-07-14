from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
)


class LeftPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Dispositivos encontrados")
        title.setStyleSheet(
            "font-size:18px;font-weight:bold;"
        )

        layout.addWidget(title)

        self.device_list = QListWidget()

        self.device_list.addItem(
            "Pulse 'Escanear dispositivos' para comenzar."
        )

        layout.addWidget(self.device_list)

        self.scan_button = QPushButton(
            "Escanear dispositivos"
        )

        layout.addWidget(self.scan_button)

        layout.addStretch()