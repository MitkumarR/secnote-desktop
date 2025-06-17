import os
from PyQt5.QtWidgets import (
    QDialog, QPushButton, QLabel, QPlainTextEdit
)
from PyQt5 import QtCore, QtWidgets

from core.key_utils import generate_key, is_valid_fernet_key
from core.file_utils import encrypt_file, decrypt_file, lock_file

class EncryptionBox(QDialog):
    def __init__(self, path):
        super().__init__()

        self.key_str = None
        self.file = path

        if not self.file:
            QtWidgets.QMessageBox.warning(self, "Error", "Please save current file or open file")
            raise ValueError("No file selected")  # Abort creation

        self.key = None
        self.title = os.path.basename(self.file)
        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(380, 290)
        self.setWindowTitle("Encryption - Secnote")

        # --------- Widgets ---------

        # Generate Key Button
        self.generateKeyButton = QtWidgets.QPushButton(self)
        self.generateKeyButton.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.generateKeyButton.setObjectName("generateKeyButton")
        self.generateKeyButton.setText("Generate Key")
        self.generateKeyButton.clicked.connect(self.generate_key)

        # Copy Button
        self.copyKeyButton = QtWidgets.QPushButton(self)
        self.copyKeyButton.setGeometry(QtCore.QRect(280, 60, 81, 31))
        self.copyKeyButton.setObjectName("copyKeyButton")
        self.copyKeyButton.setText("Copy")
        self.copyKeyButton.clicked.connect(self.copy_key)

        # Clear Button
        self.clearKeyButton = QtWidgets.QPushButton(self)
        self.clearKeyButton.setGeometry(QtCore.QRect(210, 60, 71, 31))
        self.clearKeyButton.setObjectName("clearKeyButton")
        self.clearKeyButton.setText("Clear")
        self.clearKeyButton.clicked.connect(self.clear_key)

        # Key Output Area
        self.generatedKeyOutput = QtWidgets.QPlainTextEdit(self)
        self.generatedKeyOutput.setGeometry(QtCore.QRect(20, 100, 341, 131))
        self.generatedKeyOutput.setObjectName("generatedKeyOutput")
        self.generatedKeyOutput.setPlainText("")
        self.generatedKeyOutput.setReadOnly(True)

        # Encrypt Button
        self.encryptButton = QtWidgets.QPushButton(self)
        self.encryptButton.setGeometry(QtCore.QRect(80, 240, 111, 31))
        self.encryptButton.setObjectName("encryptButton")
        self.encryptButton.setText("Encrypt")
        self.encryptButton.clicked.connect(self.encrypt)

        # Cancel Button
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setGeometry(QtCore.QRect(200, 240, 111, 31))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.reject)

        # File Name Label
        self.fileNameLabel = QtWidgets.QLabel(self)
        self.fileNameLabel.setGeometry(QtCore.QRect(20, 30, 200, 21))
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.fileNameLabel.setText(self.title)

        QtCore.QMetaObject.connectSlotsByName(self)

        # --------- Actions ---------

    def generate_key(self):
        self.key = generate_key()
        self.key_str = self.key.decode()
        self.generatedKeyOutput.setPlainText(self.key_str)

    def copy_key(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.generatedKeyOutput.toPlainText())

    def clear_key(self):
        self.generatedKeyOutput.clear()
        self.key = ""

    def encrypt(self):
        if self.key:
            self.file = encrypt_file(self.file, self.key)
            lock_file(self.file)
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Please generate a key first.")

class DecryptionBox(QDialog):
    def __init__(self, path):
        super().__init__()

        self.file = path
        self.key_str = ""
        self.key = None

        if not self.file or not self.file.endswith(".enc"):
            QtWidgets.QMessageBox.warning(self, "Error", "Please open an encrypted (.enc) file.")
            raise ValueError("Invalid file selected")

        self.title = os.path.basename(self.file)
        self.initUI()

    def initUI(self):
        self.setObjectName("DecryptionDialog")
        self.resize(380, 290)
        self.setWindowTitle("Decryption - Secnote")

        # File Name Label
        self.fileNameLabel = QtWidgets.QLabel(self)
        self.fileNameLabel.setGeometry(QtCore.QRect(20, 60, 300, 21))
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.fileNameLabel.setText(self.title)

        # Key Input Area
        self.keyInput = QtWidgets.QPlainTextEdit(self)
        self.keyInput.setGeometry(QtCore.QRect(20, 100, 341, 131))
        self.keyInput.setObjectName("keyInput")
        self.keyInput.setPlaceholderText("Paste your encryption key here...")

        # Paste Button
        self.pasteKeyButton = QtWidgets.QPushButton(self)
        self.pasteKeyButton.setGeometry(QtCore.QRect(280, 60, 71, 31))
        self.pasteKeyButton.setObjectName("pasteKeyButton")
        self.pasteKeyButton.setText("Paste")
        self.pasteKeyButton.clicked.connect(self.paste_key)

        # Clear Button
        self.clearKeyButton = QtWidgets.QPushButton(self)
        self.clearKeyButton.setGeometry(QtCore.QRect(210, 60, 71, 31))
        self.clearKeyButton.setObjectName("clearKeyButton")
        self.clearKeyButton.setText("Clear")
        self.clearKeyButton.clicked.connect(self.clear_key)

        # Decrypt Button
        self.decryptButton = QtWidgets.QPushButton(self)
        self.decryptButton.setGeometry(QtCore.QRect(80, 240, 111, 31))
        self.decryptButton.setObjectName("decryptButton")
        self.decryptButton.setText("Decrypt")
        self.decryptButton.clicked.connect(self.decrypt)

        # Cancel Button
        self.cancelButton = QtWidgets.QPushButton(self)
        self.cancelButton.setGeometry(QtCore.QRect(200, 240, 111, 31))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(self)

    def paste_key(self):
        clipboard = QtWidgets.QApplication.clipboard()
        self.keyInput.setPlainText(clipboard.text())

    def clear_key(self):
        self.keyInput.clear()

    def decrypt(self):
        self.key_str = self.keyInput.toPlainText().strip()

        if not self.key_str:
            QtWidgets.QMessageBox.warning(self, "Error", "Please paste a key first.")
            return

        if not is_valid_fernet_key(self.key_str):
            QtWidgets.QMessageBox.warning(self, "Invalid Key", "The key must be a valid 32-byte Fernet key.")
            return

        self.key = self.key_str.encode()

        try:
            decrypt_file(self.file, self.key)
            self.accept()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Failed", f"Decryption Failed: {e}")

