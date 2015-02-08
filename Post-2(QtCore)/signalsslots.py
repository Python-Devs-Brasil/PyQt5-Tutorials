from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                            QHBoxLayout, QMessageBox, QRadioButton,
                            QGroupBox, QVBoxLayout)
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        # first widgets
        self.button = QPushButton("Exibir mensagem")
        self.button.setAcceptDrops(True)
        self.button.clicked.connect(self.exibir)
        self.line_edit = QLineEdit()
        # group box of widgets
        self.groupbox = QGroupBox("Opções de Diálogo")
        # options
        self.option_information = QRadioButton("Information")
        self.option_information.setChecked(True)
        self.option_warning = QRadioButton("Warning")
        self.option_critical = QRadioButton("Critical")
        # layout of items of group box
        self.layout_options = QVBoxLayout()
        self.layout_options.addWidget(self.option_information)
        self.layout_options.addWidget(self.option_critical)
        self.layout_options.addWidget(self.option_warning)
        self.groupbox.setLayout(self.layout_options)
        # layout of QPushButton e QLineEdit
        self.layout_first_widgets = QHBoxLayout()
        self.layout_first_widgets.addWidget(self.line_edit)
        self.layout_first_widgets.addWidget(self.button)
        # main layout
        self.layout_master = QVBoxLayout()
        self.layout_master.addLayout(self.layout_first_widgets)
        self.layout_master.addWidget(self.groupbox)
        self.setLayout(self.layout_master)

    def exibir(self):
        self.text = self.line_edit.text()
        if self.option_information.isChecked():
            self.messsage_box = QMessageBox.information(self,"Exemplo 1", 
                                                       self.text)
        elif self.option_warning.isChecked():
            self.messsage_box = QMessageBox.warning(self,"Exemplo 1", 
                                                    self.text)
        else:
            self.messsage_box = QMessageBox.critical(self,"Exemplo 1", 
                                                    self.text)

    def closeEvent(self, e):
        e.ignore()
        question_close = QMessageBox.question(self, "Fechamento",
                                        "Deseja realmente fechar a aplicação?",
                                        QMessageBox.Yes, QMessageBox.No)
        if question_close == QMessageBox.Yes:
            exit(0)

if __name__ == "__main__":
    root = QApplication([])
    app = Window()
    app.show()
    sys.exit(root.exec_())
