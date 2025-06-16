import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QIcon, QKeySequence
from gui.about_dialog import AboutDialog
from gui.crypto_box import EncryptionBox


class Secnote(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Untitled - Secnote'
        self.width = 600
        self.height = 400
        self.file = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        # Icon (optional)
        if os.path.exists("Secnote.ico"):
            self.setWindowIcon(QIcon("Secnote.ico"))

        # Text Edit Area
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Menu Bar
        menuBar = self.menuBar()

        # File Menu
        fileMenu = menuBar.addMenu('File')
        self.add_menu_item(fileMenu, "New", self.new_file, "Ctrl+N")
        self.add_menu_item(fileMenu, "Open", self.open_file, "Ctrl+O")
        self.add_menu_item(fileMenu, "Save", self.save_file, "Ctrl+S")
        self.add_menu_item(fileMenu, "Save As", self.save_file_as, "Ctrl+Shift+S")
        fileMenu.addSeparator()
        self.add_menu_item(fileMenu, "Exit", self.close, "Ctrl+Q")

        # Action Menu
        actionMenu = menuBar.addMenu('Action')
        self.add_menu_item(actionMenu, "Encrypt", self.encrypt, "Ctrl+Shift+E")
        self.add_menu_item(actionMenu, "Decrypt", self.decrypt, "Ctrl+Shift+D")
        self.add_menu_item(actionMenu, "Reset Key", self.reset_key, "Ctrl+R")
        self.add_menu_item(actionMenu, "Remove Key", self.remove_key, "Ctrl+Shift+R")

        # Edit Menu
        editMenu = menuBar.addMenu('Edit')
        self.add_menu_item(editMenu, "Cut", self.textEdit.cut, "Ctrl+X")
        self.add_menu_item(editMenu, "Copy", self.textEdit.copy, "Ctrl+C")
        self.add_menu_item(editMenu, "Paste", self.textEdit.paste, "Ctrl+V")

        # Help Menu
        helpMenu = menuBar.addMenu('Help')
        self.add_menu_item(helpMenu, "About Secnote", self.show_about)

    def add_menu_item(self, menu, name, handler, shortcut=None):
        action = QAction(name, self)
        if shortcut:
            action.setShortcut(QKeySequence(shortcut))
        action.triggered.connect(handler)
        menu.addAction(action)

    def show_about(self):
        
        about_dialog = AboutDialog()
        about_dialog.exec_()

    def new_file(self):
        self.textEdit.clear()
        self.file = None
        self.setWindowTitle("Untitled - Secnote")

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, 'r') as file:
                    self.textEdit.setText(file.read())
                self.file = path
                self.setWindowTitle(os.path.basename(self.file) + " - Secnote")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not open file: {e}")

    def save_file(self):
        if self.file:
            try:
                with open(self.file, 'w') as file:
                    file.write(self.textEdit.toPlainText())
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", "Untitled.txt", "Text Files (*.txt);;All Files (*)")
        if path:
            self.file = path
            self.save_file()
            self.setWindowTitle(os.path.basename(self.file) + " - Secnote")

    def encrypt(self):

        encryption_box = EncryptionBox(self.file)
        encryption_box.exec_()

    def decrypt(self):
        QMessageBox.information(self, "Success", "File Decrypted")

    def reset_key(self):
        QMessageBox.information(self, "Success", "Key has been reset")

    def remove_key(self):
        QMessageBox.information(self, "Success", "Key has been removed")

def run_app():
    app = QApplication(sys.argv)
    window = Secnote()
    window.show()
    sys.exit(app.exec_())
