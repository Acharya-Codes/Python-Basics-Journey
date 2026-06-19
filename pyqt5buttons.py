import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QPushButton,QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click this to get free 1000 diamonds💎 in FF😏!",self)
        self.button.setGeometry(25,200,450,100)
        self.button.setStyleSheet("font-size:20px;")
        
        self.button.clicked.connect(self.on_click)  # Connect the on_click function and the button!

    def on_click(self):
        print("Congrats u got scammed NOOB 😂")
        self.button.setText("NOOB😂")



def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
                            