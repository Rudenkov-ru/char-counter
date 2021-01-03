import sys
import glob, os
from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtGui import (QIcon, QFileOpenEvent, QShortcutEvent)
from PyQt5.QtWidgets import (QFileDialog, QKeySequenceEdit)
from window import Ui_Dialog

# Create app
app = QtWidgets.QApplication(sys.argv)

# Init
Dialog = QtWidgets.QDialog()
Information = QtWidgets.QErrorMessage()
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
        Information.showMessage("Choose way!")
        print("Error Message")


def showDialog():
    filedialog = QFileDialog()
    # filedialog.exec()
    filename = filedialog.getOpenFileName(filedialog, "C:\\", "", "Text files (*.txt)")

    path = filename[0]

    print("file path: " + path)
    if path == "":
        print("file not selected")
    else:

        with open(path, "r", encoding="utf-8") as f:
            text = f.readlines()
            ui.textEdit.setText(str(text))
            print("Text has been inserted")
            Information.showMessage("Text has been inserted!")


ui.pushButton_choose.setToolTip('Use <b>Ctrl+O</b> for open file')

ui.textEdit.setAcceptRichText(False)
ui.pushButton.clicked.connect(get_length)
ui.pushButton_choose.clicked.connect(showDialog)

# Main loop
sys.exit(app.exec_())
