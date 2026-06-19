import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QCheckBox)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.checkbox = QCheckBox("Do you like Pokemon?",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,700,100)
        self.checkbox.setStyleSheet("font-size:30px;font-family:Arial;")
        self.checkbox.stateChanged.connect(self.checkbox_state)

    def checkbox_state(self,state):
        if state == 0:
            print("Why dont you like pokemon😭")
        elif state == 2:
            print("Yay!You like pokemon😁")

def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()