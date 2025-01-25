from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

class Widget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("QImage Example")
        image_label = QLabel()
        image_label.setPixmap(QPixmap("start.jpg"))
        
        layout = QVBoxLayout()
        layout.addWidget(image_label)
        self.setLayout(layout)