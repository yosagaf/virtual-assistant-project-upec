import os, sys, math, subprocess, pdb, datetime


import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'virtual-assistant.json'

DIALOGFLOW_PROJECT_ID = 'virtual-assistant-yojl'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import *
    from PyQt5.QtCore import Qt, QEvent, QObject, pyqtSignal, pyqtProperty, pyqtSlot, QPoint, QSize, QThread, \
        QThreadPool
    from PyQt5.QtOpenGL import QGL, QGLWidget
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, qApp, QFileDialog, QHBoxLayout, QOpenGLWidget, \
        QSlider, QWidget, QMessageBox, QLineEdit
    from PyQt5.QtGui import QColor, QIcon, QTextCursor, QFont
except ImportError:
    print("You need PyQt5!" + "\n" + "run: pip install PyQt5")
    sys.exit()

# OpenGL libraries
try:
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    import OpenGL.GL as gl
except ImportError:
    print("You need OpenGL!" + "\n" + "run: pip install pyOpenGL")
    sys.exit()

# PIL libraries
try:
    import PIL
    from PIL import Image
    from PIL import ImageChops
except ImportError:
    print("You need PIL!" + "\n" + "run: pip install Pillow")
    sys.exit()

# numpy libraries
try:
    import numpy
    from numpy import eye
    import numpy as np
except ImportError:
    print(
        "You need numpy!" + "\n" + "run: pip install numpy" + "Or you can download the version numpy+mkl (faster version) there: https://www.lfd.uci.edu/~gohlke/pythonlibs/")
    sys.exit()

# Import the class "Ui_MainWindow" from the GUI file "GUI_Final.py" - The extension ".py" should never be added
from GUI import Ui_MainWindow as Ui_MainWindow_0

from df_chatbot import *

InputTexturePath = "Virtual_assistant.png"
InputModelPath = "Virtual_assistant.obj"
InputModel = []
InputModelLoaded = InputTextureLoaded = InputListCreated = False
Tx = Ty = 0
Tz = 1
LeftXRot = LeftYRot = 0
b_Ready = False
Updated = False
curDir = os.getcwd()
b_MainWindowON = True
b_ChildWindowON = False
bot_name = ""


####################################################################################################
##              The Main Window (GUI)
####################################################################################################

class MainWindow_0(QMainWindow, Ui_MainWindow_0):
    #msg=''
    def __init__(self, parent=None):
        global InputModel, InputModelLoaded, InputTextureLoaded
        super(MainWindow_0, self).__init__(parent)
        QMainWindow.__init__(self)

        # All the elements from our GUI are added in "ui"
        self.ui = Ui_MainWindow_0()
        self.ui.setupUi(self)

        self.ui.send_pushButton.clicked.connect(self.querySent)
        self.ui.room_textEdit.textChanged.connect(self.get_gResponse)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui.room_textEdit.setFont(font)


    def querySent(self):
        msg = self.ui.send_lineEdit.text()
        
        # Grab text and display it in the main chat if there is a message
        if msg != "":
            msg = self.ui.send_lineEdit.text()
            self.ui.room_textEdit.setTextColor(QColor(0, 0, 255))
            self.ui.room_textEdit.append("User: " + msg)

            # Clear out the input box so we can type something else
            self.ui.send_lineEdit.clear()

            # Put the focus back into the input box so we can type again
            self.ui.send_lineEdit.setFocus()

    def get_gResponse(self):
        text_to_be_analyzed = "Hello"

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise

        result = response.query_result.fulfillment_text

        #self.ui.room_textEdit.setTextColor(QColor(0, 0, 255))
        #self.ui.room_textEdit.append("Boot:" + result)


        print("Query text:", response.query_result.query_text)
        print("Detected intent:", response.query_result.intent.display_name)
        print("Detected intent confidence:", response.query_result.intent_detection_confidence)
        print("Fulfillment text:", result)

        return result


'''
    def chatbotCommands(self):
        global bot_name
        # Extract last line of the chat
        chat = self.ui.room_textEdit.textCursor()

        self.ui.room_textEdit.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
        self.ui.room_textEdit.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
        self.ui.room_textEdit.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        lastmsg = self.ui.room_textEdit.textCursor().selectedText()

        self.ui.room_textEdit.setTextCursor(chat)
'''


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow_0()
    window.show()
    sys.exit(app.exec_())