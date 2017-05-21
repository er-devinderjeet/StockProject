# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ohlcGraph
import basicGraph
import daysGraph

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(305, 200)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.ohlcButton = QtGui.QPushButton(Form)
        self.ohlcButton.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.ohlcButton.setFixedWidth(100)
        self.ohlcButton.setObjectName(_fromUtf8("ohlcButton"))

        #dates Graph button
        self.daysBasicButton = QtGui.QPushButton(Form)
        self.daysBasicButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.daysBasicButton.setFixedWidth(150)
        self.daysBasicButton.setObjectName(_fromUtf8("daysBasicButton"))

        '''
        #Label Statistic
        '''
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 110, 16))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")), basicGraph.forever)

        QtCore.QObject.connect(self.ohlcButton,QtCore.SIGNAL(_fromUtf8("clicked()")), ohlcGraph.main)
        #button click simple days
        QtCore.QObject.connect(self.daysBasicButton,QtCore.SIGNAL(_fromUtf8("clicked()")), daysGraph.forever)




    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Basic Graph", None))
        self.ohlcButton.setText(_translate("Form", "Candle Stick Graph", None))
        self.daysBasicButton.setText(_translate("Form", "Basic Daily Chart", None))
        self.daysBasicButton.setText(_translate("Form", "Basic Daily Chart", None))
        self.label.setText(_translate("Form", "Statistic Analysis", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

