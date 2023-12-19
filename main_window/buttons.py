from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from files import variables
from utils import util
from display import display
from infos import info
from . import main_widow
import math


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(variables.MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
            self,
            display: display.Display,
            info: info.MyInfo, window: main_widow.MainWindow,
            *args, **kwargs
            ):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.window = window
        self.info = info
        self.display = display
        self._equation = ''
        self._initialEquation = 'Sua conta'
        self._left = None
        self._right = None
        self._operator = None
        self._makeGrid()

        self.equation = self._initialEquation

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._equal)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not util.isNumOrDot(
                    buttonText
                    ) and not util.isEmpty(
                        buttonText
                        ):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(
                    self._insertToDisplay,
                    buttonText,
                )
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text))

        if text == '=':
            self._connectButtonClicked(button, self._equal)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not util.isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._initialEquation
        self.display.clear()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # numero (self._left)
        self.display.clear()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not util.isValidNumber(displayText) and self._left is None:
            self._showError('Voce nao digitou nada')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._operator = text
        self.equation = f'{self._left} {self._operator} ?'

    @Slot()
    def _equal(self):
        displayText = self.display.text()

        if not util.isValidNumber(displayText):
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation:
                result = math.pow(self._left, self._right)

            else:
                result = eval(self.equation)

        except ZeroDivisionError:
            self._showError('Zero Division Error')

        except OverflowError:
            self._showError('Numero muito grande')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok |
            msgBox.StandardButton.Cancel
        )
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok |
            msgBox.StandardButton.Cancel
        )
        msgBox.exec()
