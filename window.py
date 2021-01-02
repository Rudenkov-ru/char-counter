from PyQt5 import (QtCore, QtWidgets)
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 470)
        Dialog.setStyleSheet("")
        self.pushButton_choose = QtWidgets.QPushButton(Dialog)
        self.pushButton_choose.setGeometry(QtCore.QRect(290, 75, 25, 25))
        self.pushButton_choose.setStyleSheet("background-color: #F5E2E2;")
        self.pushButton_choose.setObjectName("pushButton_choose")

        self.label_choose = QtWidgets.QLabel(Dialog)
        self.label_choose.setGeometry(QtCore.QRect(180, 80, 210, 16))
        self.label_choose.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_choose.setObjectName("label_choose")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 390, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"Showcard Gothic\";\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 221, 21))
        self.label.setStyleSheet("font: 12pt \"Snap ITC\";\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_2.setStyleSheet("font: 9pt \"OCR A Extended\";")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(30, 400, 141, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 430, 145, 20))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(560, 440, 81, 20))
        self.label_3.setStyleSheet("font: 87 italic 8pt \"Segoe UI Black\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 80, 171, 16))
        self.label_4.setStyleSheet("color:green;font: 14pt \"OCR A Extended\";")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(33, 116, 581, 261))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Counter"))
        Dialog.setWindowIcon(QIcon("icon.png"))
        self.radioButton.setIcon(QIcon("Ok-icon.png"))
        self.radioButton_2.setIcon(QIcon("no-icon.png"))
        self.pushButton_choose.setIcon(QIcon("upload-icon.png"))
        self.pushButton.setText(_translate("Dialog", "Count!"))
        self.label.setText(_translate("Dialog", "Character counter"))
        self.label_2.setText(_translate("Dialog", "Input text:"))
        self.label_choose.setText(_translate("Dialog", "Upload(.txt)"))
        self.radioButton.setText(_translate("Dialog", "With spaces"))
        self.radioButton_2.setText(_translate("Dialog", "Without spaces"))
        self.label_3.setText(_translate("Dialog", "version 1.0"))
