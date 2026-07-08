"""
MERIDIAN-JB Alpha 0.1

Buried Worlds Research Lab
Initial application shell.
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)
from PySide6.QtCore import Qt


class MeridianWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MERIDIAN-JB Alpha 0.1")
        self.resize(1200, 800)

        title = QLabel(self)

        title.setText(
            "BURIED WORLDS RESEARCH LAB\n\n"
            "MERIDIAN-JB Alpha 0.1\n\n"
            "Archaeology • Geography • Exploration"
        )

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #c8a45d;
                background-color: #151515;
            }
        """)

        self.setCentralWidget(title)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #151515;
            }
        """)


def main():
    app = QApplication(sys.argv)

    window = MeridianWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
