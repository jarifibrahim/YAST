# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\YAST\yast_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1350, 686)
        MainWindow.setMinimumSize(QtCore.QSize(1350, 686))
        MainWindow.setMaximumSize(QtCore.QSize(1350, 686))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 70, 1461, 20))
        self.line.setMinimumSize(QtCore.QSize(751, 0))
        self.line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(210, 80, 20, 631))
        self.line_2.setMinimumSize(QtCore.QSize(20, 0))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 631))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(5)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(220, 520, 1381, 20))
        self.line_3.setMinimumSize(QtCore.QSize(781, 0))
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(230, 90, 1081, 431))
        self.groupBox.setMinimumSize(QtCore.QSize(501, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 611))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 1061, 401))
        self.scrollArea.setMinimumSize(QtCore.QSize(481, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1059, 399))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 1301, 61))
        self.groupBox_2.setMinimumSize(QtCore.QSize(721, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 1181, 20))
        self.lineEdit.setMinimumSize(QtCore.QSize(601, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.B_choose_file = QtGui.QPushButton(self.groupBox_2)
        self.B_choose_file.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.B_choose_file.setObjectName(_fromUtf8("B_choose_file"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QtCore.QRect(10, 460, 201, 171))
        self.frame_3.setMinimumSize(QtCore.QSize(201, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 181))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.frame_3)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 171, 151))
        self.groupBox_5.setMinimumSize(QtCore.QSize(171, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.B_SStop = QtGui.QPushButton(self.groupBox_5)
        self.B_SStop.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.B_SStop.setMinimumSize(QtCore.QSize(75, 0))
        self.B_SStop.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_SStop.setObjectName(_fromUtf8("B_SStop"))
        self.B_SStart = QtGui.QPushButton(self.groupBox_5)
        self.B_SStart.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.B_SStart.setMinimumSize(QtCore.QSize(75, 0))
        self.B_SStart.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_SStart.setObjectName(_fromUtf8("B_SStart"))
        self.line_5 = QtGui.QFrame(self.groupBox_5)
        self.line_5.setGeometry(QtCore.QRect(0, 50, 171, 20))
        self.line_5.setMinimumSize(QtCore.QSize(171, 0))
        self.line_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox.setGeometry(QtCore.QRect(20, 100, 71, 22))
        self.spinBox.setMinimumSize(QtCore.QSize(71, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(100, 100, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(10, 90, 191, 81))
        self.frame_4.setMinimumSize(QtCore.QSize(191, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 101))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.frame_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 0, 171, 71))
        self.groupBox_6.setMinimumSize(QtCore.QSize(161, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.comboBox = QtGui.QComboBox(self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 141, 22))
        self.comboBox.setMinimumSize(QtCore.QSize(111, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 180, 191, 81))
        self.frame.setMinimumSize(QtCore.QSize(191, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 81))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.groupBox_3 = QtGui.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.groupBox_3.setMinimumSize(QtCore.QSize(161, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.B_TStart = QtGui.QPushButton(self.groupBox_3)
        self.B_TStart.setGeometry(QtCore.QRect(10, 30, 71, 23))
        self.B_TStart.setMinimumSize(QtCore.QSize(71, 0))
        self.B_TStart.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_TStart.setObjectName(_fromUtf8("B_TStart"))
        self.B_TStop = QtGui.QPushButton(self.groupBox_3)
        self.B_TStop.setGeometry(QtCore.QRect(90, 30, 71, 23))
        self.B_TStop.setMinimumSize(QtCore.QSize(71, 0))
        self.B_TStop.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_TStop.setObjectName(_fromUtf8("B_TStop"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setMinimumSize(QtCore.QSize(2, 0))
        self.layoutWidget.setMaximumSize(QtCore.QSize(16777215, 2))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setMinimumSize(QtCore.QSize(2, 0))
        self.layoutWidget1.setMaximumSize(QtCore.QSize(16777215, 2))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setEnabled(False)
        self.frame_2.setGeometry(QtCore.QRect(10, 280, 191, 171))
        self.frame_2.setMinimumSize(QtCore.QSize(191, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 191))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 171, 161))
        self.groupBox_4.setMinimumSize(QtCore.QSize(171, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.B_CStart = QtGui.QPushButton(self.groupBox_4)
        self.B_CStart.setEnabled(False)
        self.B_CStart.setGeometry(QtCore.QRect(10, 20, 61, 23))
        self.B_CStart.setMinimumSize(QtCore.QSize(61, 0))
        self.B_CStart.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_CStart.setObjectName(_fromUtf8("B_CStart"))
        self.B_CStop = QtGui.QPushButton(self.groupBox_4)
        self.B_CStop.setEnabled(False)
        self.B_CStop.setGeometry(QtCore.QRect(80, 20, 71, 23))
        self.B_CStop.setMinimumSize(QtCore.QSize(61, 0))
        self.B_CStop.setMaximumSize(QtCore.QSize(16777215, 23))
        self.B_CStop.setObjectName(_fromUtf8("B_CStop"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 90, 121, 51))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 221, 16))
        self.line_4.setMinimumSize(QtCore.QSize(221, 0))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 260, 221, 16))
        self.line_6.setMinimumSize(QtCore.QSize(221, 0))
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 450, 221, 16))
        self.line_7.setMinimumSize(QtCore.QSize(221, 0))
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.B_Close = QtGui.QPushButton(self.centralwidget)
        self.B_Close.setGeometry(QtCore.QRect(1180, 540, 75, 23))
        self.B_Close.setObjectName(_fromUtf8("B_Close"))
        self.B_Save = QtGui.QPushButton(self.centralwidget)
        self.B_Save.setGeometry(QtCore.QRect(1100, 540, 75, 23))
        self.B_Save.setObjectName(_fromUtf8("B_Save"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 580, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 610, 1041, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionYAST_Help = QtGui.QAction(MainWindow)
        self.actionYAST_Help.setObjectName(_fromUtf8("actionYAST_Help"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionYAST_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "YAST", None))
        self.groupBox.setTitle(_translate("MainWindow", "Output", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filter", None))
        self.B_choose_file.setText(_translate("MainWindow", "Choose", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sessionization", None))
        self.B_SStop.setText(_translate("MainWindow", "Stop", None))
        self.B_SStart.setText(_translate("MainWindow", "Start", None))
        self.label_3.setText(_translate("MainWindow", "Session Time:", None))
        self.label.setText(_translate("MainWindow", "Min.", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Log Format", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Proxy Log File", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Web Log File", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Squid Log File", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tokenization", None))
        self.B_TStart.setText(_translate("MainWindow", "Start", None))
        self.B_TStop.setText(_translate("MainWindow", "Stop", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Clean", None))
        self.B_CStart.setText(_translate("MainWindow", "Start", None))
        self.B_CStop.setText(_translate("MainWindow", "Stop", None))
        self.label_2.setText(_translate("MainWindow", "To Be Exclude:", None))
        self.B_Close.setText(_translate("MainWindow", "Close", None))
        self.B_Save.setText(_translate("MainWindow", "Save", None))
        self.label_4.setText(_translate("MainWindow", "Status :", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionYAST_Help.setText(_translate("MainWindow", "YAST Help", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

