import sys

from display import display
from PySide6.QtWidgets import QApplication, QLabel
from main_window import main_widow


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = main_widow.MainWindow()

    # Cria display
    display = display.Display()
    window.addToLayout(display)

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window.addToLayout(label1)
    window.adjustFixedSize()

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
