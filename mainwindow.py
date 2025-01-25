from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("My App")
        
        
    # Working with menubar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_action)
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        
        help_menu = menu_bar.addMenu("Help")
        
        
    # Working with toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)
        
        action1 = QAction("Action 1", self)
        action1.setStatusTip("This is Action 1")
        action1.triggered.connect(self.action1_triggered)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon("start.jpg"),"Action 2", self)
        action2.setStatusTip("This is Action 2")
        action2.triggered.connect(self.action1_triggered)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Hello"))
        
        self.setStatusBar(QStatusBar(self))
        
        button = QPushButton("Button")
        button.clicked.connect(self.action1_triggered)
        self.setCentralWidget(button)
        
        
    def quit_action(self):
        self.app.quit()
        
    def action1_triggered(self):
        self.statusBar().showMessage("Action 1 triggered")