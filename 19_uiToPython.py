#pyside6-uic form.ui > ui_form.py
import sys
from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication(sys.argv)

widget = Widget()
widget.show()

app.exec()