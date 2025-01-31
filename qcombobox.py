from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,  QPushButton, QListWidget, QAbstractItemView, QTabWidget, QLabel, QLineEdit, QSpacerItem, QComboBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Example")
        
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venues")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Jupiter")
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Uranus")
        self.combo_box.addItem("Neptune")
        
        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.get_current_value)
        button_current_text = QPushButton("Set Value")
        button_current_text.clicked.connect(self.set_current_text)
        button_get_values = QPushButton("Get Values")
        button_get_values.clicked.connect(self.get_values)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_current_text)
        v_layout.addWidget(button_get_values)
        
        self.setLayout(v_layout)
        
    def get_current_value(self):
        print("Current Value:", self.combo_box.currentText(), "Index:", self.combo_box.currentIndex())
        
    def set_current_text(self):
        self.combo_box.setCurrentIndex(2)
        
    def get_values(self):
        for i in range(self.combo_box.count()):
            print("Index:", i, "Value:", self.combo_box.itemText(i))