import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import audiototext
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button = QPushButton("Start Recording", self)
        self.button.clicked.connect(audiototext.start_recording) # connect the button to the function

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
