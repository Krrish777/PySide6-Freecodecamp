from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,  QPushButton, QListWidget, QAbstractItemView, QTabWidget, QLabel, QLineEdit, QSpacerItem

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        tab_widget = QTabWidget(self)
        
        widget_form = QWidget()
        label_full_name = QLabel("Full Name:")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)
        
        widget_buttons = QWidget()
        button_1 = QPushButton("Button 1")
        button_1.clicked.connect(self.on_button_1_clicked)
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_layout = QVBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        button_layout.addWidget(button_3)
        widget_buttons.setLayout(button_layout)
        
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")
        
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)
        
    def on_button_1_clicked(self):
        print("Button 1 was clicked.")