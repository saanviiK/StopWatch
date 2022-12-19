# importing libraries
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle('Python Stop Watch')

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):

            # counter
            self.count = 0

            # creating a flag
            self.flag = False

            # creating a label to show the time
            self.label = QLabel(self)

            # setting the geometry of the label
            self.label.setGeometry(75, 100, 250, 70)

            # adding border to the label
            self.label.setStyleSheet("border :  4px solid black")

            # setting text inside the label
            self.label.setText(str(self.count))

            # setting font to the label
            self.label.setFont(QFont('Arial', 25))

            # setting alignment to the text of the label
            self.label.setAlignment(Qt.AlignCenter)

            # creating the start button
            start = QPushButton("start", self)
            
            # creating the stop button
            pause = QPushButton("pause", self)

            # creating the reset button
            reset = QPushButton("reset", self)

            # setting the geometry of the start button
            start.setGeometry(125, 250, 150, 40)

            # setting the geometry of the stop button
            pause.setGeometry(125, 300, 150, 40)

            # setting the geometry of the reset button
            reset.setGeometry(125, 350, 150, 40)

            # add action to the method
            start.pressed.connect(self.start)

            # add action to the method
            pause.pressed.connect(self.pause)
            
            # add action to the method
            reset.pressed.connect(self.reset)

            # creating the timer object
            timer = QTimer(self)

            # adding action to the timer
            timer.timeout.connect(self.showTime)

            # update the timer every tenth second
            timer.start(100)
        
        # method called by timer
    def showTime(self):
        # checking if the flag is true
        if self.flag:

            # incrementing the counter
            self.count += 1

        # getting the text from count
        text = str(self.count / 10)

        # showing text
        self.label.setText(text)
    
    def start(self):

        # setting flag to true
        self.flag = True
    
    def pause(self):
        
        # setting flag to false
        self.flag = False
    
    def reset(self):

        # setting flag to false
        self.flag = False

        # setting timer to 0
        self.count = 0

        # showing the text
        self.label.setText(str(self.count))


# creating pyqt5 app
App = QApplication(sys.argv)

# creating the instance of our window
window = Window()

# start the app
sys.exit(App.exec())