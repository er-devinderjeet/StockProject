__author__ = 'Devinderjeet'

from PyQt4 import QtCore,QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

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


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class PrettyWidget(object):
    def __init__(self, parent=None):
        super(PrettyWidget,self).__init__()

    def setupUi(self,Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(321, 94)

        self.start = QtGui.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.start.setObjectName(_fromUtf8("start"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.start,QtCore.SIGNAL("clicked()"), ohlcGraph.main)
        #QtCore.QObject.connect(self)

    def retranslateUi(self,Form):
        self.start.setText(_translate("Form", "Start ", None))



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = PrettyWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

