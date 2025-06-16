import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QMessageBox
from core.key_utils import generate_key
from core.file_utils import encrypt_file, decrypt_file

class EncryptionBox(QDialog):
    def __init__(self, path):
        super().__init__()
        self.title = 'Untitled - Secnote'
        self.width = 600
        self.height = 400
        self.file = path
        self.key = None
        self.initUI()

    def initUI(self):
        # ----- Components -----
        self.setGeometry(200, 200, self.width, self.height)  # x, y, width, height

        # Label
        self.label = QLabel(os.path.basename(self.file))

        # Button
        self.btn = QPushButton("Generate Key", self)
        self.btn.clicked.connect(self.on_button_click)

        # Output Area (read-only)
        self.outputText = QLineEdit(self.key)
        self.outputText.setReadOnly(True)

        # ----- Layout -----
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.addWidget(self.outputText)

        self.setLayout(layout)

    def on_button_click(self):
        self.key = generate_key()

    def encryption(self):
        encrypt_file(self.file, self.key)

class DecryptionBox(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secnote")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        label = QLabel("Decryption Box")
        layout.addWidget(label)

        self.setLayout(layout)
