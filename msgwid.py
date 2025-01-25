from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box Example")
        
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.show_hard_message)
        
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.show_critical_message)
        
        button_information = QPushButton("Information")
        button_information.clicked.connect(self.show_information_message)
        
        button_question = QPushButton("Question")
        button_question.clicked.connect(self.show_question_message)
        
        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.show_warning_message)
        
        button_about = QPushButton("About")
        button_about.clicked.connect(self.show_about_message)
        
        
        #Set layout
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_information)
        layout.addWidget(button_question)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)
    
    def show_hard_message(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message: Hard")
        message.setText("This is a hard message")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")
    
    def show_critical_message(self):
        ret = QMessageBox.critical(self, "Critical", "This is a critical message", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")
        
    def show_information_message(self):
        QMessageBox.information(self, "Information", "This is an information message")
        
    def show_question_message(self):
        QMessageBox.question(self, "Question", "This is a question message")
        
    def show_warning_message(self):
        QMessageBox.warning(self, "Warning", "This is a warning message")
    
    def show_about_message(self):
        QMessageBox.about(self, "About", "This is an about message")