from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox, QRadioButton, QGroupBox, QButtonGroup

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox and QRadioButton")
        
        os = QGroupBox("Choose Operating Systems")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_toggled)
        
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_toggled)
        
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_toggled)
        
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)
        
        drink = QGroupBox("Choose Drinks")
        
        coffee = QCheckBox("Coffee")
        tea = QCheckBox("Tea")
        juice = QCheckBox("Juice")
        coffee.setChecked(True)
        
        exclusive_button = QButtonGroup(self)
        exclusive_button.addButton(coffee)
        exclusive_button.addButton(tea)
        exclusive_button.addButton(juice)
        exclusive_button.setExclusive(True)
        
        drink_layout = QVBoxLayout()
        drink_layout.addWidget(coffee)
        drink_layout.addWidget(tea)
        drink_layout.addWidget(juice)
        drink.setLayout(drink_layout)
        
        answers = QGroupBox("Choose Answers")
        answer1 = QRadioButton("Answer 1")
        answer2 = QRadioButton("Answer 2")
        answer3 = QRadioButton("Answer 3")
        answer1.setChecked(True)
        
        answer_layout = QVBoxLayout()
        answer_layout.addWidget(answer1)
        answer_layout.addWidget(answer2)
        answer_layout.addWidget(answer3)
        answers.setLayout(answer_layout)
        
        
        layout = QVBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drink)
        layout.addWidget(answers)
        self.setLayout(layout)
        
        
    def windows_toggled(self, checked):
        if(checked):
            print("Windows Checked")
        else:
            print("Windows Unchecked")
            
    def linux_toggled(self, checked):
        if(checked):
            print("Linux Checked")
        else:
            print("Linux Unchecked")
            
    def mac_toggled(self, checked):
        if(checked):
            print("Mac Checked")
        else:
            print("Mac Unchecked")