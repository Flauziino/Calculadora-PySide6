from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from files import variables
from utils import util
from display import display
from infos import info


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
            self, display: display.Display, info: info.MyInfo,
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
                    self._insertButtonTextToDisplay,
                    button,
                )
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text

        if not util.isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)

    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._initialEquation
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # operadores (+-/*)
        displayText = self.display.text()  # numero (self._left)
        self.display.clear()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not util.isValidNumber(displayText) and self._left is None:
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._operator = buttonText
        self.equation = f'{self._left} {self._operator} ?'
