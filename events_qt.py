import sys  


from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel

from main_windows import Window

def greeting():
    """slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)


layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())