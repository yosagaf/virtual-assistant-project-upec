import os, sys, math, subprocess, pdb, datetime
import dialogflow
import time
from google.api_core.exceptions import InvalidArgument
from extract_emotion import text2speech, extractEmotion, speech2text

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'upec-bot-olvv.json'

DIALOGFLOW_PROJECT_ID = 'upec-bot-olvv'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

# import PyQt related module
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
    print("You need OpenGL !" + "\n" + "run: pip install pyOpenGL")
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

# Import the class "Ui_MainWindow" from the GUI file "GUI.py" - The extension ".py" should never be added
from GUI import Ui_MainWindow as Ui_MainWindow_0

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
query = ""
result = ""
maflag = False

#################################################################
#                   The Main Window (GUI)
#################################################################

class MainWindow_0(QMainWindow, Ui_MainWindow_0):
    def __init__(self, parent=None):
        global InputModel, InputModelLoaded, InputTextureLoaded
        super(MainWindow_0, self).__init__(parent)
        QMainWindow.__init__(self)

        # All the elements from our GUI are added in "ui"
        self.ui = Ui_MainWindow_0()
        self.ui.setupUi(self)

        self.ui.send_pushButton.clicked.connect(self.querySent)
        self.ui.mic_push_button.clicked.connect(self.record)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui.room_textEdit.setFont(font)

    # To be called when the "send" button is pressed 
    def querySent(self):
        global query
        global maflag
        
        if maflag == True:
            query = speech2text()
            print("My query is :", query)
            maflag = False
        else :
            query = self.ui.send_lineEdit.text()
            #emotion2 = extractEmotion(query)

        # Grab text and display it in the main chat if there is a message
        if query != "":
            self.ui.room_textEdit.setTextColor(QColor(0, 0, 255))
            self.ui.room_textEdit.append("User: " + query)

            # Clear out the input box so we can type something else
            self.ui.send_lineEdit.clear()

            # Put the focus back into the input box so we can type again
            self.ui.send_lineEdit.setFocus()

            self.ui.room_textEdit.setTextColor(QColor(255, 0, 255))
            self.ui.room_textEdit.append("Assistant: " + self.getResponse())
        
        # Classify the emotion from the text TAQ for the answer and perform speech to text
        extractEmotion(result)
        text2speech(result)

    # function to be called the MIC button is pressed to process speech recogniton
    def record(self):
        global maflag
        maflag = True
        self.querySent()
    
    # Get the query and the answer and display it on the text room
    def getResponse(self):
        global result
        text_to_be_analyzed = query

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise

        result = response.query_result.fulfillment_text
        
        print("Query text:", response.query_result.query_text)
        print("Detected intent:", response.query_result.intent.display_name)
        print("Detected intent confidence:", response.query_result.intent_detection_confidence)
        print("Fulfillment text:", result)
        
        return result

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow_0()
    window.show()
    sys.exit(app.exec_())