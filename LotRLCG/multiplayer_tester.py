import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtTest import *
from JoinGameDialog import *
from HostGameDialog import *


hostGameDialog = None
joinGameDialogs = []


def startServer():
    global hostGameDialog
    hostGameDialog = HostGameDialog()
    hostGameDialog.move(0, 0)
    hostGameDialog.show()
    hostGameDialog.hostButton.click()
    QTest.keyPress(hostGameDialog.hostingLineEdit, Qt.Key_C, Qt.ControlModifier)
    QTest.keyRelease(hostGameDialog.hostingLineEdit, Qt.Key_C, Qt.ControlModifier)


def startClient():
    global hostGameDialog
    for i in range(2):
        joinGameDialog = JoinGameDialog()
        joinGameDialog.move(hostGameDialog.width() + i * joinGameDialog.width(), 0)
        joinGameDialog.show()
        QTest.keyPress(joinGameDialog.addressLineEdit, Qt.Key_V, Qt.ControlModifier)
        QTest.keyRelease(joinGameDialog.addressLineEdit, Qt.Key_V, Qt.ControlModifier)
        joinGameDialog.joinButton.click()
        global joinGameDialogs
        joinGameDialogs.append(joinGameDialog)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startServer()
    QTimer.singleShot(500, startClient)
    sys.exit(app.exec_())