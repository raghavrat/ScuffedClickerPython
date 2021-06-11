import threading

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
import sys
import time
from threading import Timer



clickeramt = 0
counter = 0
grandmapog = 0
doggyamount = 0
monkeyamount = 0


def clickerfunc(c):
    global counter
    global clickeramt
    if counter >= 5:
        counter = counter - 5
        clickeramt += 1
        label.setText('clicks = ' + str(counter))
        print(clickeramt)

        clickers.move(100, 100)
        clickers.setText("clickers = " + str(clickeramt) + ', grandmas = ' + str(grandmapog) + ", doggies = " + str(doggyamount) + ", monkeys = " + str(monkeyamount))



def grandmafunc(c):
    global counter
    global grandmapog
    if counter >= 100:
        counter = counter - 100
        grandmapog += 1
        label.setText('clicks = ' + str(counter))
        print(grandmapog)

        clickers.move(100, 100)
        clickers.setText("clickers = " + str(clickeramt) + ', grandmas = ' + str(grandmapog) + ", doggies = " + str(doggyamount) + ", monkeys = " + str(monkeyamount))

def doggyfunc(c):
    global counter
    global doggyamount
    if counter >= 1000:
        counter = counter - 1000
        doggyamount += 1
        label.setText('clicks = ' + str(counter))
        print(doggyamount)

        clickers.move(100, 100)
        clickers.setText("clickers = " + str(clickeramt) + ', grandmas = ' + str(grandmapog) + ", doggies = " + str(doggyamount) + ", monkeys = " + str(monkeyamount))

def monkeyfunc(c):
    global counter
    global monkeyamount
    if counter >= 10000:
        counter = counter - 10000
        monkeyamount += 1
        label.setText('clicks = ' + str(counter))
        print(monkeyamount)

        clickers.move(100, 100)
        clickers.setText("clickers = " + str(clickeramt) + ', grandmas = ' + str(grandmapog) + ", doggies = " + str(doggyamount) + ", monkeys = " + str(monkeyamount))

def buttonClickedHandler(c):
    global counter
    counter += 1
    label.setText('clicks = ' + str(counter))


app = QApplication(sys.argv)

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("Scuffed Clicker")

layout = QGridLayout(window)


label = QLabel("clicks = 0")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label, 0, 0)

clickers = QLabel("clickers = 0")
layout.addWidget(clickers, 0, 1)
def click():
    threading.Timer(5, click).start()
    global counter
    global clickeramt
    counter += clickeramt
    label.setText('clicks = ' + str(counter))


click()

def grandmafunction():
    threading.Timer(1, grandmafunction).start()
    global counter
    global grandmapog
    counter += grandmapog
    label.setText('clicks = ' + str(counter))


grandmafunction()

def doggyfunction():
    threading.Timer(1, doggyfunction).start()
    global counter
    global doggyamount
    counter += doggyamount * 5
    label.setText('clicks = ' + str(counter))


doggyfunction()

def monkeyfunction():
    threading.Timer(1, monkeyfunction).start()
    global counter
    global monkeyamount
    counter += monkeyamount * 10
    label.setText('clicks = ' + str(counter))

monkeyfunction()

if counter > 100:
    label2 = QLabel("Achievement! 100+ clicks")
    layout.addWidget(label2)
    label2.move(0, 0)

clicker = QPushButton("Clicker, -5 clicks")
clicker.setToolTip("Clicks once every 5 seconds")
clicker.clicked.connect(clickerfunc)

grandmas = QPushButton("Grandma, -100 clicks")
grandmas.setToolTip("Clicks once every 1 seconds")
grandmas.clicked.connect(grandmafunc)

monkeys = QPushButton("Monkey, -10000 clicks")
monkeys.setToolTip("Clicks 10 times every 1 seconds")
monkeys.clicked.connect(monkeyfunc)

doggies = QPushButton("Doggy, -1000 clicks")
doggies.setToolTip("Clicks 5 times every 1 seconds")
doggies.clicked.connect(doggyfunc)

button = QPushButton("Click me")
button.setToolTip('CLICK ME!!!!!!!')

horLayout = QHBoxLayout()
horLayout.addStretch(1)
horLayout.addWidget(button)
horLayout.addWidget(clicker)
horLayout.addWidget(grandmas)
horLayout.addWidget(doggies)
horLayout.addWidget(monkeys)
horLayout.addStretch(1)
layout.addLayout(horLayout, 1, 0)

button.clicked.connect(buttonClickedHandler)



window.show()



sys.exit(app.exec_())