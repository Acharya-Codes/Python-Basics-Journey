import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(0,0,500,500) # (x-coords,y-coords,width,height)
        self.setWindowIcon(QIcon("random.jpg"))

        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:red;background-color:black;font-weight:bold;font-style:italic;text-decoration:underline;")
        #label.setAlignment(Qt.AlignTop) # Vertically Top
        #label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter) # Vertically Center
        #label.setAlignment(Qt.AlignRight) # Hozirontally Right
        #label.setAlignment(Qt.AlignLeft) # Hozirontally Left
        #label.setAlignment(Qt.AlignHCenter) # Horizontally Center

        #label.setAlignment(Qt.AlignHCenter | Qt.Top) Center and Top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) Center and Bottom
        #label.setAlignment(Qt.AlignCenter) Center and Center

        label1 = QLabel(self)
        pixmap = QPixmap("random.jpg")
        label1.setPixmap(pixmap)
        label1.setScaledContents(True) # Fit to size
        label1.setGeometry(0,0,250,250)
        label.setGeometry((self.width() - label1.width())//2,(self.height()-label1.height())//2,label1.width(),label1.height())
        # Basically we can modify the line 35 and position the image!!


def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    