import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() # Create a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load("form.ui", None)

def do_something():
    print(window.fullname_lineEdit.text(), "is a", window.occupation_lineEdit.text())
    
window.setWindowTitle("QDesigner Example")
window.submitbutton.clicked.connect(do_something)
window.show()
app.exec()