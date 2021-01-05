# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 509)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_left = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_left.setGeometry(QtCore.QRect(10, 20, 341, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)


        self.groupBox_left.setFont(font)
        self.groupBox_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_left.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_left.setObjectName("groupBox_left")


        self.Frame = QtWidgets.QFrame(self.groupBox_left)
        self.Frame.setGeometry(QtCore.QRect(10, 20, 321, 421))
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setObjectName("Frame")



        self.frame_3D = QtWidgets.QFrame(self.Frame)
        self.frame_3D.setGeometry(QtCore.QRect(10, 10, 301, 401))
        self.frame_3D.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3D.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3D.setObjectName("frame_3D")
        self.groupBox_right = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_right.setGeometry(QtCore.QRect(370, 20, 401, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)


        self.groupBox_right.setFont(font)
        self.groupBox_right.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_right.setObjectName("groupBox_right")
        self.groupBox_query = QtWidgets.QGroupBox(self.groupBox_right)
        self.groupBox_query.setGeometry(QtCore.QRect(9, 370, 381, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_query.setFont(font)
        self.groupBox_query.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_query.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_query.setObjectName("groupBox_query")


        self.send_pushButton = QtWidgets.QPushButton(self.groupBox_query)
        self.send_pushButton.setGeometry(QtCore.QRect(320, 30, 51, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.send_pushButton.setObjectName("send_pushButton")

        self.send_lineEdit = QtWidgets.QLineEdit(self.groupBox_query)
        self.send_lineEdit.setGeometry(QtCore.QRect(10, 30, 301, 20))
        self.send_lineEdit.setObjectName("send_lineEdit")


        self.room_textEdit = QtWidgets.QTextEdit(self.groupBox_right)
        self.room_textEdit.setGeometry(QtCore.QRect(10, 20, 381, 351))
        self.room_textEdit.setObjectName("room_textEdit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")

        self.menuFace = QtWidgets.QMenu(self.menubar)
        self.menuFace.setObjectName("menuFace")

        self.menuPose_Gesture = QtWidgets.QMenu(self.menubar)
        self.menuPose_Gesture.setObjectName("menuPose_Gesture")

        self.menuFingerprint = QtWidgets.QMenu(self.menubar)
        self.menuFingerprint.setObjectName("menuFingerprint")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFace.menuAction())
        self.menubar.addAction(self.menuPose_Gesture.menuAction())
        self.menubar.addAction(self.menuFingerprint.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Assistant"))
        self.groupBox_left.setTitle(_translate("MainWindow", "Virtual Assistance"))
        self.groupBox_right.setTitle(_translate("MainWindow", "CHATBOT"))
        self.groupBox_query.setTitle(_translate("MainWindow", "Query"))
        self.send_pushButton.setText(_translate("MainWindow", "Send"))
        self.menuFace.setTitle(_translate("MainWindow", "Face"))
        self.menuPose_Gesture.setTitle(_translate("MainWindow", "Pose/Gesture"))
        self.menuFingerprint.setTitle(_translate("MainWindow", "Fingerprint"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
