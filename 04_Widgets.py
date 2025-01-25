from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RockWidget
import sys
app = QApplication(sys.argv)
rock_widget = RockWidget()
rock_widget.show()

app.exec()