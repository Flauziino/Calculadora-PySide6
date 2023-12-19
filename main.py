import sys

from infos import info
from display import display
from styles import qss_style
from main_window import main_widow, buttons
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = main_widow.MainWindow()

    qss_style.setupTheme()

    # Info
    info = info.MyInfo()
    info.setText('HARO')
    window.addWidgetToVLayout(info)

    # Cria display
    display = display.Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = buttons.ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
