from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)

    def mousePressEvent(self, e):
        img, re = QFileDialog.getOpenFileName(self,"Selecionar Arquivo",
                                            filter="All(*.png *.jpg)")
        if re:
            self.setPixmap(QPixmap(img).scaled(250,150,
                            Qt.KeepAspectRatio))

    def mouseMoveEvent(self, e):
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self, e):
        QApplication.setOverrideCursor(Qt.ArrowCursor)

class HandlerWindow(QWidget):
    def __init__(self, parent=None):
        super(HandlerWindow, self).__init__()
        self.resize(300,350)
        self.label = CustomLabel(self)
        self.label.setPixmap(QPixmap("imgs/default-user.png").scaled(250,150,
                            Qt.KeepAspectRatio))

if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = HandlerWindow()
    app.show()
    sys.exit(root.exec_())