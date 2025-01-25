from PySide6.QtWidgets import QWidget,QSizePolicy,QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        
        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_4 = QPushButton("Button 4")
        button_5 = QPushButton("Button 5")
        button_6 = QPushButton("Button 6")
        button_7 = QPushButton("Button 7")
        
        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0, 0)
        grid_layout.addWidget(button_2, 0, 1,1,2)
        grid_layout.addWidget(button_3, 1, 0,2,1)
        grid_layout.addWidget(button_4, 1, 1)
        grid_layout.addWidget(button_5, 1, 2)
        grid_layout.addWidget(button_6, 2, 1)
        grid_layout.addWidget(button_7, 2, 2)
        
        self.setLayout(grid_layout)