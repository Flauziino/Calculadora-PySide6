from utils import util
from files import variables
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # Tamanho da fonte da "tela"
        self.setStyleSheet(f'font-size: {variables.BIG_FONT_SIZE}px;')
        # Tamnho da "tela" em si (*2 para ter um respiro)
        self.setMinimumHeight(variables.BIG_FONT_SIZE * 2)
        # Alinhamento a direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Margem do texto com list compreehnsion
        self.setTextMargins(*[variables.TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus,
            KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P
            ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Nao passar desse ponto se nao tiver txt
        if util.isEmpty(text):
            return event.ignore()

        if util.isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
