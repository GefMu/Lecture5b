import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lecture 5b")
        self.setMinimumWidth(300)
        self.counter = 0
        max_range = 255
        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, max_range)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("QSpinBox { background-color: #d3d3d3; }")

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0, max_range)
        self.slider.valueChanged.connect(self.on_slide_value_changed)

        self.slider_spin_box = QSpinBox()
        self.slider_spin_box.setRange(0, max_range)
        self.slider_spin_box.setReadOnly(True)
        self.slider_spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.slider_spin_box.setStyleSheet(
            "QSpinBox { background-color: #d3d3d3; }"
        )

        self.color_box = QLabel()
        self.color_box.setMinimumWidth(100)
        self.color_box.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        self.color_box.setStyleSheet('background-color:lightgray')

        self.toggle_button = QPushButton("Start")
        self.toggle_button.toggled.connect(self.on_button_toggle)
        self.toggle_button.setCheckable(True)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_method)
        self.timer.start(1_000)

        controls_layout = QVBoxLayout()
        controls_layout.addWidget(self.spin_box)
        controls_layout.addWidget(self.toggle_button)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.slider_spin_box)

        layout = QHBoxLayout()
        layout.addLayout(controls_layout)
        layout.addLayout(slider_layout)
        layout.addWidget(self.color_box, 1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_toggle(self, started: bool) -> None:
        self.toggle_button.setText("Stop" if started else "Start")
        if started:
            self.counter = 0
            self.timer.start(10)
        else:
            self.timer.stop()


    def on_timer_method(self):
        self.spin_box.setValue(self.counter)
        self.counter += 1

    def on_slide_value_changed(self):
        self.slider_spin_box.setValue(self.slider.value())

def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()