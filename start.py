# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4w
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import TA2
import ohlcGraph
import indices
import one_day_fetch
import one_day_indices



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
        Form.resize(521, 94)


        self.stock = QtGui.QPushButton(Form)
        self.stock.setGeometry(QtCore.QRect(40, 20, 75, 23))
        self.stock.setObjectName(_fromUtf8("stock"))


        self.indices = QtGui.QPushButton(Form)
        self.indices.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.indices.setObjectName(_fromUtf8("indices"))

        self.one_day_fetch = QtGui.QPushButton(Form)
        self.one_day_fetch.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.one_day_fetch.setObjectName(_fromUtf8("one_day_fetch"))

        self.one_day_indices = QtGui.QPushButton(Form)
        self.one_day_indices.setGeometry(QtCore.QRect(180, 60, 75, 23))
        self.one_day_indices.setObjectName(_fromUtf8("one_day_indices"))

        self.stop = QtGui.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.stop.setObjectName(_fromUtf8("stop"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        #QtCore.QObject.connect(self.start, QtCore.SIGNAL(_fromUtf8("clicked()")), TA2.forever)
        QtCore.QObject.connect(self.indices, QtCore.SIGNAL(_fromUtf8("clicked()")), indices.forever)
        QtCore.QObject.connect(self.stock, QtCore.SIGNAL(_fromUtf8("clicked()")), TA2.forever)
        QtCore.QObject.connect(self.one_day_fetch, QtCore.SIGNAL(_fromUtf8("clicked()")), one_day_fetch.forever)
        QtCore.QObject.connect(self.one_day_indices, QtCore.SIGNAL(_fromUtf8("clicked()")), one_day_indices.forever)


        QtCore.QObject.connect(self.stop, QtCore.SIGNAL(_fromUtf8("clicked()")), ohlcGraph.main)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Fetching Data", None))
        self.indices.setText(_translate("Form", "Indices ", None))
        self.stock.setText(_translate("Form", "Stock ", None))
        self.one_day_fetch.setText(_translate("Form", "1 day ", None))
        self.one_day_indices.setText(_translate("Form", "day indices", None))

        self.stop.setText(_translate("Form", "Stop", None))
        self.label.setText(_translate("Form", "Stock Data", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form_1 = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form_1)
    Form_1.show()
    sys.exit(app.exec_())
