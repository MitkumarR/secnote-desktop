from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Secnote")
        self.setFixedSize(400, 250)
        self.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout()

        about_text = (
            "<h3>Secnote</h3>"
            "<p>A lightweight and secure desktop note editor built using Python. </p>"
            "<b>Features:</b><br>"
            "- File encryption/decryption<br>"
            "- Custom key management<br>"
            "- Local storage security<br><br>"
            "<i>Developed by: Mit Softwares</i>"
        )

        label = QLabel(about_text)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        layout.addWidget(label)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn, alignment=Qt.AlignRight)

        self.setLayout(layout)