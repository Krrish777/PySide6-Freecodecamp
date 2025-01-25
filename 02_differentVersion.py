'''
#Version 1 : Setting everything up in the global scope
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First App")

button = QPushButton("Click me")
window.setCentralWidget(button)

window.show()
app.exec()
'''

'''
#Version 2 : Setting everything up in the class
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First App")
        button = QPushButton("Click me")
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
'''

#Version 3 : Move the class to a separate file
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
