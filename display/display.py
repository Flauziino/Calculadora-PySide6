from files import variables
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt


class Display(QLineEdit):
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
        # Margem do texto
        self.setTextMargins(*[variables.TEXT_MARGIN for _ in range(4)])
