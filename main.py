import sys

from PySide6.QtWidgets import QApplication, QLabel
from main_window import main_widow


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = main_widow.MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window.v_layout.addWidget(label1)
    window.adjustFixedSize()

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
