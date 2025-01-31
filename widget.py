from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_form import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.submitbutton.clicked.connect(self.submit)
    
    def submit(self):
        print(f"Full Name: {self.fullname_lineEdit.text()} \nOccupation: {self.occupation_lineEdit.text()}")