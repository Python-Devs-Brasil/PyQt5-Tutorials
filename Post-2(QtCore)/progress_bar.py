from PyQt5.QtWidgets import QWidget, QProgressBar, QApplication
from PyQt5.QtCore import QBasicTimer
import sys


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__()
		self.set_settings()
		self.create_widgets()

	def set_settings(self):
		self.resize(350,200)

	def create_widgets(self):
		self.progress_bar = QProgressBar(self)
		self.progress_bar.setFixedWidth(300)
		self.progress_bar.move(50,80)
		#timer creating
		self.timer = QBasicTimer()
		self.step = 0
		self.timer.start(100, self)

	def timerEvent(self, e):
		if self.step >= 100:
			self.timer.stop()

		self.step += 1
		self.progress_bar.setValue(self.step)

root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())