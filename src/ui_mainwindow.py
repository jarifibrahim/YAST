# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
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
        MainWindow.setMouseTracking(True)
        MainWindow.setDocumentMode(False)
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
        self.output_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.output_groupBox.setGeometry(QtCore.QRect(230, 90, 1081, 431))
        self.output_groupBox.setMinimumSize(QtCore.QSize(501, 0))
        self.output_groupBox.setMaximumSize(QtCore.QSize(16777215, 611))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.output_groupBox.setFont(font)
        self.output_groupBox.setFlat(False)
        self.output_groupBox.setCheckable(False)
        self.output_groupBox.setObjectName(_fromUtf8("output_groupBox"))
        self.output_plainTextEdit = QtGui.QPlainTextEdit(self.output_groupBox)
        self.output_plainTextEdit.setGeometry(QtCore.QRect(12, 25, 1061, 401))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.output_plainTextEdit.setFont(font)
        self.output_plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.output_plainTextEdit.setReadOnly(True)
        self.output_plainTextEdit.setPlainText(_fromUtf8(""))
        self.output_plainTextEdit.setBackgroundVisible(False)
        self.output_plainTextEdit.setCenterOnScroll(False)
        self.output_plainTextEdit.setObjectName(_fromUtf8("output_plainTextEdit"))
        self.choose_file_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.choose_file_groupBox.setGeometry(QtCore.QRect(10, 0, 1301, 61))
        self.choose_file_groupBox.setMinimumSize(QtCore.QSize(721, 0))
        self.choose_file_groupBox.setMaximumSize(QtCore.QSize(16777215, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.choose_file_groupBox.setFont(font)
        self.choose_file_groupBox.setTitle(_fromUtf8(""))
        self.choose_file_groupBox.setObjectName(_fromUtf8("choose_file_groupBox"))
        self.file_path_textEdit = QtGui.QLineEdit(self.choose_file_groupBox)
        self.file_path_textEdit.setEnabled(True)
        self.file_path_textEdit.setGeometry(QtCore.QRect(110, 20, 1181, 20))
        self.file_path_textEdit.setMinimumSize(QtCore.QSize(601, 0))
        self.file_path_textEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.file_path_textEdit.setFont(font)
        self.file_path_textEdit.setObjectName(_fromUtf8("file_path_textEdit"))
        self.B_choose_file = QtGui.QPushButton(self.choose_file_groupBox)
        self.B_choose_file.setGeometry(QtCore.QRect(20, 20, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.B_choose_file.setFont(font)
        self.B_choose_file.setObjectName(_fromUtf8("B_choose_file"))
        self.session_frame = QtGui.QFrame(self.centralwidget)
        self.session_frame.setEnabled(True)
        self.session_frame.setGeometry(QtCore.QRect(0, 430, 211, 161))
        self.session_frame.setMinimumSize(QtCore.QSize(201, 0))
        self.session_frame.setMaximumSize(QtCore.QSize(16777215, 181))
        self.session_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.session_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.session_frame.setObjectName(_fromUtf8("session_frame"))
        self.session_groupBox = QtGui.QGroupBox(self.session_frame)
        self.session_groupBox.setEnabled(True)
        self.session_groupBox.setGeometry(QtCore.QRect(10, 10, 191, 141))
        self.session_groupBox.setMinimumSize(QtCore.QSize(171, 0))
        self.session_groupBox.setMaximumSize(QtCore.QSize(16777215, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.session_groupBox.setFont(font)
        self.session_groupBox.setObjectName(_fromUtf8("session_groupBox"))
        self.session_time_label = QtGui.QLabel(self.session_groupBox)
        self.session_time_label.setEnabled(True)
        self.session_time_label.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.session_time_label.setFont(font)
        self.session_time_label.setObjectName(_fromUtf8("session_time_label"))
        self.time_spinBox = QtGui.QSpinBox(self.session_groupBox)
        self.time_spinBox.setGeometry(QtCore.QRect(40, 50, 71, 22))
        self.time_spinBox.setMinimumSize(QtCore.QSize(71, 0))
        self.time_spinBox.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.time_spinBox.setFont(font)
        self.time_spinBox.setObjectName(_fromUtf8("time_spinBox"))
        self.minute_label = QtGui.QLabel(self.session_groupBox)
        self.minute_label.setGeometry(QtCore.QRect(120, 50, 31, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.minute_label.setFont(font)
        self.minute_label.setObjectName(_fromUtf8("minute_label"))
        self.B_SStart = QtGui.QPushButton(self.session_groupBox)
        self.B_SStart.setEnabled(True)
        self.B_SStart.setGeometry(QtCore.QRect(60, 100, 75, 23))
        self.B_SStart.setMinimumSize(QtCore.QSize(75, 0))
        self.B_SStart.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.B_SStart.setFont(font)
        self.B_SStart.setObjectName(_fromUtf8("B_SStart"))
        self.line_seperator_2 = QtGui.QFrame(self.session_groupBox)
        self.line_seperator_2.setEnabled(False)
        self.line_seperator_2.setGeometry(QtCore.QRect(10, 80, 171, 20))
        self.line_seperator_2.setMinimumSize(QtCore.QSize(171, 0))
        self.line_seperator_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_seperator_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_seperator_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_seperator_2.setObjectName(_fromUtf8("line_seperator_2"))
        self.log_frame = QtGui.QFrame(self.centralwidget)
        self.log_frame.setGeometry(QtCore.QRect(0, 90, 211, 81))
        self.log_frame.setMinimumSize(QtCore.QSize(191, 0))
        self.log_frame.setMaximumSize(QtCore.QSize(16777215, 101))
        self.log_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.log_frame.setObjectName(_fromUtf8("log_frame"))
        self.groupBox_6 = QtGui.QGroupBox(self.log_frame)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 0, 191, 71))
        self.groupBox_6.setMinimumSize(QtCore.QSize(161, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.log_format_comboBox = QtGui.QComboBox(self.groupBox_6)
        self.log_format_comboBox.setGeometry(QtCore.QRect(10, 30, 151, 22))
        self.log_format_comboBox.setMinimumSize(QtCore.QSize(111, 0))
        self.log_format_comboBox.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.log_format_comboBox.setFont(font)
        self.log_format_comboBox.setObjectName(_fromUtf8("log_format_comboBox"))
        self.log_format_comboBox.addItem(_fromUtf8(""))
        self.log_format_comboBox.addItem(_fromUtf8(""))
        self.log_format_comboBox.addItem(_fromUtf8(""))
        self.token_frame = QtGui.QFrame(self.centralwidget)
        self.token_frame.setEnabled(True)
        self.token_frame.setGeometry(QtCore.QRect(0, 180, 211, 81))
        self.token_frame.setMinimumSize(QtCore.QSize(191, 0))
        self.token_frame.setMaximumSize(QtCore.QSize(16777215, 81))
        self.token_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.token_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.token_frame.setObjectName(_fromUtf8("token_frame"))
        self.token_groupBox = QtGui.QGroupBox(self.token_frame)
        self.token_groupBox.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.token_groupBox.setMinimumSize(QtCore.QSize(161, 0))
        self.token_groupBox.setMaximumSize(QtCore.QSize(16777215, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.token_groupBox.setFont(font)
        self.token_groupBox.setObjectName(_fromUtf8("token_groupBox"))
        self.B_TStart = QtGui.QPushButton(self.token_groupBox)
        self.B_TStart.setGeometry(QtCore.QRect(60, 30, 75, 23))
        self.B_TStart.setMinimumSize(QtCore.QSize(61, 0))
        self.B_TStart.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.B_TStart.setFont(font)
        self.B_TStart.setObjectName(_fromUtf8("B_TStart"))
        self.filter_frame = QtGui.QFrame(self.centralwidget)
        self.filter_frame.setEnabled(True)
        self.filter_frame.setGeometry(QtCore.QRect(0, 270, 211, 151))
        self.filter_frame.setMinimumSize(QtCore.QSize(191, 0))
        self.filter_frame.setMaximumSize(QtCore.QSize(16777215, 191))
        self.filter_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.filter_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.filter_frame.setObjectName(_fromUtf8("filter_frame"))
        self.filter_groupBox = QtGui.QGroupBox(self.filter_frame)
        self.filter_groupBox.setGeometry(QtCore.QRect(10, 0, 191, 151))
        self.filter_groupBox.setMinimumSize(QtCore.QSize(171, 0))
        self.filter_groupBox.setMaximumSize(QtCore.QSize(16777215, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.filter_groupBox.setFont(font)
        self.filter_groupBox.setObjectName(_fromUtf8("filter_groupBox"))
        self.ignore_ext_lineEdit = QtGui.QLineEdit(self.filter_groupBox)
        self.ignore_ext_lineEdit.setGeometry(QtCore.QRect(10, 60, 161, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ignore_ext_lineEdit.setFont(font)
        self.ignore_ext_lineEdit.setObjectName(_fromUtf8("ignore_ext_lineEdit"))
        self.ignore_ext_label = QtGui.QLabel(self.filter_groupBox)
        self.ignore_ext_label.setGeometry(QtCore.QRect(0, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ignore_ext_label.setFont(font)
        self.ignore_ext_label.setWordWrap(True)
        self.ignore_ext_label.setObjectName(_fromUtf8("ignore_ext_label"))
        self.line_seperator = QtGui.QFrame(self.filter_groupBox)
        self.line_seperator.setEnabled(False)
        self.line_seperator.setGeometry(QtCore.QRect(10, 90, 171, 20))
        self.line_seperator.setMinimumSize(QtCore.QSize(171, 0))
        self.line_seperator.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line_seperator.setFrameShape(QtGui.QFrame.HLine)
        self.line_seperator.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_seperator.setObjectName(_fromUtf8("line_seperator"))
        self.B_CStart = QtGui.QPushButton(self.filter_groupBox)
        self.B_CStart.setGeometry(QtCore.QRect(60, 110, 75, 23))
        self.B_CStart.setMinimumSize(QtCore.QSize(61, 0))
        self.B_CStart.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.B_CStart.setFont(font)
        self.B_CStart.setObjectName(_fromUtf8("B_CStart"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 221, 16))
        self.line_4.setMinimumSize(QtCore.QSize(221, 0))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 260, 221, 16))
        self.line_6.setMinimumSize(QtCore.QSize(221, 0))
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 420, 221, 16))
        self.line_7.setMinimumSize(QtCore.QSize(221, 0))
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.B_Close = QtGui.QPushButton(self.centralwidget)
        self.B_Close.setGeometry(QtCore.QRect(1180, 540, 90, 30))
        self.B_Close.setObjectName(_fromUtf8("B_Close"))
        self.B_Save = QtGui.QPushButton(self.centralwidget)
        self.B_Save.setGeometry(QtCore.QRect(1080, 540, 93, 30))
        self.B_Save.setObjectName(_fromUtf8("B_Save"))
        self.status_label = QtGui.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(230, 620, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.status_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.status_lineEdit.setEnabled(True)
        self.status_lineEdit.setGeometry(QtCore.QRect(300, 620, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.status_lineEdit.setFont(font)
        self.status_lineEdit.setReadOnly(True)
        self.status_lineEdit.setObjectName(_fromUtf8("status_lineEdit"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(300, 580, 981, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 580, 68, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.records_processed_value_label = QtGui.QLabel(self.centralwidget)
        self.records_processed_value_label.setGeometry(QtCore.QRect(240, 550, 131, 17))
        self.records_processed_value_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.records_processed_value_label.setObjectName(_fromUtf8("records_processed_value_label"))
        self.records_processed_label = QtGui.QLabel(self.centralwidget)
        self.records_processed_label.setGeometry(QtCore.QRect(380, 550, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.records_processed_label.setFont(font)
        self.records_processed_label.setObjectName(_fromUtf8("records_processed_label"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 620, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(0, 600, 221, 16))
        self.line_8.setMinimumSize(QtCore.QSize(221, 0))
        self.line_8.setMaximumSize(QtCore.QSize(16777215, 16))
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionYAST_Help = QtGui.QAction(MainWindow)
        self.actionYAST_Help.setObjectName(_fromUtf8("actionYAST_Help"))
        self.menuFile.addAction(self.actionReset)
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
        self.output_groupBox.setTitle(_translate("MainWindow", "Results", None))
        self.B_choose_file.setText(_translate("MainWindow", "Choose", None))
        self.session_groupBox.setTitle(_translate("MainWindow", "Sessionization", None))
        self.session_time_label.setText(_translate("MainWindow", "Enter Session Time:", None))
        self.minute_label.setText(_translate("MainWindow", "Min.", None))
        self.B_SStart.setText(_translate("MainWindow", "Start", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Log Format", None))
        self.log_format_comboBox.setItemText(0, _translate("MainWindow", "Apache Common", None))
        self.log_format_comboBox.setItemText(1, _translate("MainWindow", "Apache Combined", None))
        self.log_format_comboBox.setItemText(2, _translate("MainWindow", "Squid Proxy", None))
        self.token_groupBox.setTitle(_translate("MainWindow", "Tokenization", None))
        self.B_TStart.setText(_translate("MainWindow", "Start", None))
        self.filter_groupBox.setTitle(_translate("MainWindow", "Filter", None))
        self.ignore_ext_label.setText(_translate("MainWindow", "Discard requests to the following file extensions:", None))
        self.B_CStart.setText(_translate("MainWindow", "Start", None))
        self.B_Close.setText(_translate("MainWindow", "Close", None))
        self.B_Save.setText(_translate("MainWindow", "Save Result", None))
        self.status_label.setText(_translate("MainWindow", "Status ", None))
        self.label.setText(_translate("MainWindow", "Progress:", None))
        self.records_processed_value_label.setText(_translate("MainWindow", "0/0", None))
        self.records_processed_label.setText(_translate("MainWindow", "Records processed", None))
        self.label_6.setText(_translate("MainWindow", "YAST", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionYAST_Help.setText(_translate("MainWindow", "YAST Help", None))
