import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt

class PyColorMini(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.generate_palette()  # Auto-generate palette upon opening

    def init_ui(self):
        self.setWindowTitle("PyColor Mini")
        
        # Apply dark theme
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.generate_button = QPushButton("Generate Palette")
        self.generate_button.setStyleSheet("background-color: #444; color: white; font-size: 14px; padding: 5px;")
        self.generate_button.clicked.connect(self.generate_palette)
        self.main_layout.addWidget(self.generate_button)

        self.color_panel = QVBoxLayout()
        self.main_layout.addLayout(self.color_panel)

        self.adjustSize()  # Resize to fit content

    def generate_palette(self):
        # Clear previous palette
        for i in reversed(range(self.color_panel.count())):
            widget = self.color_panel.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Generate and display new palette
        for _ in range(5):
            color = self.random_color()
            
            color_label = QLabel()
            color_label.setAutoFillBackground(True)
            
            # Explicitly set the color background using a palette
            palette = QPalette()
            palette.setColor(QPalette.Window, color)
            color_label.setPalette(palette)
            color_label.setStyleSheet(f"background-color: {color.name()}; font-size: 14px; font-weight: bold; padding: 5px;")
            color_label.setFixedHeight(50)

            hex_code = color.name()
            color_label.setText(f"  {hex_code}")
            color_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

            color_label.mousePressEvent = lambda event, hex_code=hex_code: self.copy_to_clipboard(hex_code)

            self.color_panel.addWidget(color_label)

        self.adjustSize()  # Adjust window size after generating palette

    def random_color(self):
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def copy_to_clipboard(self, hex_code):
        clipboard = QApplication.clipboard()
        clipboard.setText(hex_code)
        print(f"Copied {hex_code} to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyColorMini()
    window.show()
    sys.exit(app.exec_())
