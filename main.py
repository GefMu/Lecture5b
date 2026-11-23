import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lecture 5b")
        self.setMinimumWidth(300)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10_000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("QSpinBox { background-color: #d3d3d3; }")

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.on_button_toggle)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_toggle(self, started: bool) -> None:
        self.toggle_button.setText("Stop" if started else "Start")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()