# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import qdarktheme
from files import variables


# Utilizando 2 chaves para o Fstring entender que
# nao é para ler a chave dupla e sim apenas a que esta sozinha
qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {variables.PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {variables.DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {variables.DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{variables.PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{variables.PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
