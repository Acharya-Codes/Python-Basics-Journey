import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QPushButton,QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.button = QPushButton("Click this to get free 1000 diamonds💎 in FF😏!",self)
        self.label = QLabel("Hello Surviver",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(25,200,450,100)
        self.button.setStyleSheet("font-size:20px;")
        self.button.clicked.connect(self.on_click)  # Connect the on_click function and the button!
        self.label.setGeometry(10,100,400,100)
        self.label.setStyleSheet("font-size:50px;")

    def on_click(self):
        self.label.setText("Byebye")
        print("Congrats u got scammed NOOB 😂")
        self.button.setText("NOOB😂")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
                            