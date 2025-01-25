from PySide6.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        
        label = QLabel("Hello World!")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter your text here")
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        
        button = QPushButton("Click me!")
        button.clicked.connect(self.button_clicked)
        self.text_holder = QLabel("I AM HERE")
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder)
        
        self.setLayout(v_layout)
        
    def button_clicked(self):
        self.text_holder.setText(self.line_edit.text())
            
    def text_changed(self, text):
        self.text_holder.setText(self.line_edit.text())
        
    def cursor_position_changed(self,old_pos, new_pos):
        print(f"Old position: {old_pos}, New position: {new_pos}")
        
    def editing_finished(self):
        print("Editing finished")
        
    def return_pressed(self):
        print("Return pressed")