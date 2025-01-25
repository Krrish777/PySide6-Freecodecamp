#Importing the componets we need to create a window
from PySide6.QtWidgets import QApplication, QMainWindow

#sys responsible for the command line arguments
import sys

#Creating the application and a wrapper for the window
app = QApplication(sys.argv)

window = QMainWindow()
window.show()

#Start the event loop
app.exec()