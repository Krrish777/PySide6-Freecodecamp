'''
#Version1 : Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton
def button_clicked():
    print("Button clicked")

app = QApplication()
button = QPushButton("Click me")

#clicked is a signal of QPushButton. It's emitted when the button is clicked.
#We can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)
button.show()
app.exec()
'''

'''
#Version2 : Signal sending values, capture values in slot
from PySide6.QtWidgets import QApplication, QPushButton
def button_clicked(value):
    print(f"Button clicked with value {value}")
    
app = QApplication()
button = QPushButton("Click me")
button.setCheckable(True)
#Makes the button checkable. It's unchecked by default.
#Further clicks will toggle between checked and unchecked states.

button.clicked.connect(button_clicked)
button.show()
app.exec()
'''

'''
'''

#Version3 : Captue value from a slider
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

def slider_moved(value):
    print(f"Slider moved to {value}")
    
app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
slider.setSingleStep(5)

slider.valueChanged.connect(slider_moved)
slider.show()
app.exec()