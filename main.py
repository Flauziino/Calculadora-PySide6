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
    info.setText('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Cria display
    display = display.Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = buttons.ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Button
    # buttonsGrid.addWidget(buttons.Button('0'), 0, 0)
    # buttonsGrid.addWidget(buttons.Button('1'), 0, 1)
    # buttonsGrid.addWidget(buttons.Button('2'), 0, 2)
    # buttonsGrid.addWidget(buttons.Button('3'), 0, 3)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
