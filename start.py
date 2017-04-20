# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4w
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import TA2
import ohlcGraph

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
        Form.resize(321, 94)

        self.start = QtGui.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.start.setObjectName(_fromUtf8("start"))

        self.stop = QtGui.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.stop.setObjectName(_fromUtf8("stop"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.start, QtCore.SIGNAL(_fromUtf8("clicked()")), TA2.forever)
        QtCore.QObject.connect(self.stop, QtCore.SIGNAL(_fromUtf8("clicked()")), ohlcGraph.main)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Fetching Data", None))
        self.start.setText(_translate("Form", "Start ", None))
        self.stop.setText(_translate("Form", "Stop", None))
        self.label.setText(_translate("Form", "Current Status", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_1 = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form_1)
    Form_1.show()
    sys.exit(app.exec_())

    app_2 = QtGui.QApplication(sys.argv)
    widget_2 = QtGui.QWidget()
    ui_2 = Ui_Form()
    ui_2.setupUi(widget_2)
    widget_2.show()
    sys.exit(app_2.exec_())
