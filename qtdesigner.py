from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() # Create a loader object

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.window = loader.load("form.ui", None)
        self.window.setWindowTitle("QDesigner Example")
        self.window.submitbutton.clicked.connect(self.do_something)
        
    def show(self):
        self.window.show()
    
    def do_something(self):
        print(self.window.fullname_lineEdit.text(), "is a", self.window.occupation_lineEdit.text())