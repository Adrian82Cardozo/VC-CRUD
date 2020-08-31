from PyQt5 import QtWidgets
from main import Ui_MainWindow  # importing our generated file
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setText("hola!!!")

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())