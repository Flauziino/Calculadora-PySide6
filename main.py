import sys

from infos import info
from display import display
from main_window import main_widow
from PySide6.QtWidgets import QApplication
from styles import qss_style


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = main_widow.MainWindow()

    qss_style.setupTheme()

    # Info
    info = info.MyInfo()
    info.setText('2.0 ^ 10.0 = 1024')
    window.addToLayout(info)

    # Cria display
    display = display.Display()
    window.addToLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
