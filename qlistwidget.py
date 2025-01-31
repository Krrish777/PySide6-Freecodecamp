from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox, QListWidget, QRadioButton, QGroupBox, QButtonGroup, QAbstractItemView

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")
        
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two", "Three", "Four"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)
        
        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(lambda: self.list_widget.addItem("New Item"))
        
        button_remove_item = QPushButton("Remove Item")
        button_remove_item.clicked.connect(lambda: self.list_widget.takeItem(self.list_widget.currentRow()))
        
        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(lambda: print(f"Item count: {self.list_widget.count()}"))
        
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(button_add_item)
        layout.addWidget(button_remove_item)
        layout.addWidget(button_item_count)
        self.setLayout(layout)
        
    def current_item_changed(self, item):
        print(f"Current item: {item.text()}")
        
    def current_text_changed(self, text):
        print(f"Current text: {text}")
