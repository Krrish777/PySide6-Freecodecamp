from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout
class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        
        # layout = QHBoxLayout() #Horizontal layout
        layout = QVBoxLayout() #Vertical layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)
    
    def button1_clicked(self):
        print("Button1 clicked")
    
    def button2_clicked(self):
        print("Button2 clicked")