# pycalc.py 

"""A simple calculator app with qtpy"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
# view
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
# controller class
from functools import partial

__version__ = '0.1'
__author__ = "Rioba Ian"

class PyCalcUi(QMainWindow):
    """PyCalc's view GUI"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyCalc')
        self.setFixedSize(350,320)
        # set the central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # create the display widget
        self.display = QLineEdit()
        # set some display's properties 
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # add the display to the general layout 
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        # create the buttons
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # button text | position on the QGridLayout 
        buttons = {
            '7': (0,0),
            '8': (0,1),
            '9': (0,2),
            '/': (0,3),
            'C': (0,4),
            '4': (1,0),
            '5': (1,1),
            '6': (1,2),
            '*': (1,3),
            '(': (1,4),
            '1': (2,0),
            '2': (2,1),
            '3': (2,2),
            '-': (2,3),
            ')': (2,4),
            '0': (3,0),
            '00': (3,1),
            '.': (3,2),
            '+': (3,3),
            '=': (3,4),
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # add buttonslayout to the general layout 
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        # get the display text
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

def main():
    # create an instance of QApplication 
    pycalc = QApplication(sys.argv)
    # show the GUI
    view = PyCalcUi()
    view.show()
    # create instances of the modela dn the controller 
    model = evaluateExpression
    PyCalcCtrl(model=model,view=view)
    # execute the calculator's main loop
    sys.exit(pycalc.exec_())

ERROR_MSG = 'ERROR'

# create a model to handle the operations 
def evaluateExpression(expression):
    # evaluate an expression
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    
    return result
        

class PyCalcCtrl:
    """PyCalc controller class"""
    def __init__(self, model,view):
        # controller initializer
        self._view = view 
        self._evaluate = model
        # connect signals and slots 
        self._connectSignals()
    
    def _calculateResult(self):
        """Evaluate expressions"""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression"""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots """
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
            
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['='].clicked.connect(self._calculateResult)

if __name__ == '__main__':
    main()