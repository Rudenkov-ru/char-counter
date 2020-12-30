import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from window import Ui_Dialog

# Create app
app = QtWidgets.QApplication(sys.argv)

# Init
Dialog = QtWidgets.QDialog()
Error = QtWidgets.QErrorMessage()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# Hook logic
def get_length():
    text = ui.textEdit.toPlainText()
    if ui.radioButton.isChecked():
        result_1 = len(text)
        ui.label_4.setText(f'Result:{result_1}')
    elif ui.radioButton_2.isChecked():
        result_2 = len(text.replace(" ", ""))
        ui.label_4.setText(f'Result:{result_2}')
    else:
        Error.showMessage("Choose way!")


ui.textEdit.setAcceptRichText(False)
ui.pushButton.clicked.connect(get_length)

# Main loop
sys.exit(app.exec_())
