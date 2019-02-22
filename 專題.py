"""
Created on Thu Feb 14 21:15:03 2019

@author: Hank
"""

import sys, os, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QAction, QMenu, QLineEdit, QComboBox, QDialogButtonBox, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QCheckBox, QWidget, QApplication, QInputDialog, QVBoxLayout, QFormLayout, QHBoxLayout, QGraphicsLineItem, QStyleOptionGraphicsItem, QDialog

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData


        


class Process_Button(QPushButton):
    global buttonlist
    print("!!!!")
    inputline = []
    dragable = 0
    string = 'a'
    next_index = 'null'
    nodenum = 0
    position = QPoint()
    mode = 'process'
    ExtremePoint = 0
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
# =============================================================================
#     def mouseMoveEvent(self, e):
# 
#         if e.buttons() != Qt.RightButton:
#             return
# 
#         mimeData = QMimeData()
# 
#         drag = QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setHotSpot(e.pos() + self.rect().topLeft())
#         
#         dropAction = drag.exec_(Qt.MoveAction)
# 
#     def mousePressEvent(self, e):
#         global linemode
#         global paintarray
#         
#         if linemode == 1:
#             if e.buttons() == Qt.LeftButton:
#                 paintarray.append(self)
#             
#             #print(self.position)
#         else :
#             if e.buttons() == Qt.RightButton:
#                 for button in buttonlist:
#                     if button.dragable == 1:
#                         button.dragable = 0
#                 self.dragable = 1
#             
#             QPushButton.mousePressEvent(self, e)
# =============================================================================
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')


            
class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Demo: PyQt with matplotlib')
        self.setGeometry(400,100,1200,600)
        self.setAcceptDrops(True)
        self.create_menu()
        self.create_main_frame()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.leftwidget.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
       
        
        openfile_path = QFileDialog.getOpenFileName(self,'選擇文件','',"PNG (*.png)|*.png")
    
    
    def on_about(self):
        msg ="""
        
        *可以把開個照片，然後丟進來拉來拉去這樣。
        """
        QMessageBox.about(self, "簡介", msg.strip())


    def create_main_frame(self):
        self.main_frame = QWidget()

        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas2 = FigureCanvas(self.fig)


        hbox = QVBoxLayout()
        Button_box = QVBoxLayout()
        self.leftwidget = QWidget()
        

        
# =============================================================================
#         self.Start_Button = QPushButton("Start")   
#         self.Start_Button.setCheckable(True)
#         self.End_Button = QPushButton("End")
#         self.End_Button.setBackgroundRole
#         self.End_Button.setCheckable(True)
#         self.Process_Button = QPushButton("Process")
#         self.Process_Button.setCheckable(True)
#         self.Loop_Button = QPushButton("Loop")
#         self.Loop_Button.setCheckable(True)
#         self.Decision_Button = QPushButton("Decision")
#         self.Decision_Button.setCheckable(True)
#         
#         for w in [  self.Start_Button, self.End_Button, self.Loop_Button,
#                     self.Decision_Button]:
#             hbox.addWidget(w)
#             hbox.setAlignment(w, Qt.AlignVCenter)
# =============================================================================
        
        toolbarBox = QtWidgets.QToolBar(self)
        toolbarBox.setFixedWidth(180)
        toolbarBox.setMovable(False)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)
        self.Start_Action = toolbarBox.addAction('Start')
        self.Start_Action.triggered.connect(self.add_Start)
        self.Start_Action.setCheckable(True)
        self.End_Action = toolbarBox.addAction('End')
        self.End_Action.triggered.connect(self.add_End)
        self.End_Action.setCheckable(True)
        self.Decision_Action = toolbarBox.addAction('Decision')
        self.Decision_Action.triggered.connect(self.add_Decision)
        self.Decision_Action.setCheckable(True)
        self.Loop_Action = toolbarBox.addAction('Loop')
        self.Loop_Action.triggered.connect(self.add_Loop)
        self.Loop_Action.setCheckable(True)
        self.Process_Action = toolbarBox.addAction('Process')
        self.Process_Action.triggered.connect(self.add_Process)
        self.Process_Action.setCheckable(True)
       
        Hbox = QHBoxLayout()
        #vbox.addWidget(Button_box)
        #Hbox.addLayout(hbox)

        Hbox.addWidget(self.leftwidget)
        Hbox.addWidget(self.canvas2)
        Hbox.addWidget(self.canvas)
    
        self.main_frame.setLayout(Hbox)
        self.setCentralWidget(self.main_frame)
    
    def add_Start(self):
        self.Start_Action.setCheckable(True)
        self.End_Action.setCheckable(False)
        self.Decision_Action.setCheckable(False)
        self.Loop_Action.setCheckable(False)
        self.Process_Action.setCheckable(False)
        print("1234")
        self.leftwidget.button = Process_Button('Start', self)
        self.leftwidget.button.setStyleSheet("background-color: Gray")
        self.leftwidget.button.string = 'Start'
        self.leftwidget.button.ExtremePoint = 1
        self.leftwidget.button.setGeometry(240, 30, 210, 30)
        self.leftwidget.button.position.setX(240)
        self.leftwidget.button.position.setY(30)
        
        self.leftwidget.button.show()
        
    def add_End(self):
        self.End_Action.setCheckable(True)
        self.Start_Action.setCheckable(False)
        self.Decision_Action.setCheckable(False)
        self.Loop_Action.setCheckable(False)
        self.Process_Action.setCheckable(False)

        self.leftwidget.button = Process_Button('End', self)
        self.leftwidget.button.setStyleSheet("background-color: Gray")
        self.leftwidget.button.string = 'Start'
        self.leftwidget.button.ExtremePoint = 1
        self.leftwidget.button.setGeometry(240, 30, 210, 30)
        self.leftwidget.button.position.setX(240)
        self.leftwidget.button.position.setY(30)
        
        self.leftwidget.button.show()
    
    def add_Process(self, name):
        self.Process_Action.setCheckable(True)
        self.Start_Action.setCheckable(False)
        self.End_Action.setCheckable(False)
        self.Decision_Action.setCheckable(False)
        self.Loop_Action.setCheckable(False)
        print("1234")
        self.leftwidget.button = Process_Button('Process', self)
        self.leftwidget.button.setStyleSheet("background-color: Red")
        self.leftwidget.button.string = 'Start'
        self.leftwidget.button.ExtremePoint = 1
        self.leftwidget.button.setGeometry(240, 30, 210, 30)
        self.leftwidget.button.position.setX(240)
        self.leftwidget.button.position.setY(30)

        self.leftwidget.button.show()
    
    def add_Decision(self):
        self.Decision_Action.setCheckable(True)
        self.Start_Action.setCheckable(False)
        self.End_Action.setCheckable(False)
        self.Loop_Action.setCheckable(False)
        self.Process_Action.setCheckable(False)
        print("1234")
        self.leftwidget.button = Process_Button('Decision', self)
        self.leftwidget.button.setStyleSheet("background-color: Pink")
        self.leftwidget.button.string = 'Start'
        self.leftwidget.button.ExtremePoint = 1
        self.leftwidget.button.setGeometry(240, 30, 210, 30)
        self.leftwidget.button.position.setX(240)
        self.leftwidget.button.position.setY(30)
        
        self.leftwidget.button.show()

    def add_Loop(self):
        self.Loop_Action.setCheckable(True)
        self.Start_Action.setCheckable(False)
        self.End_Action.setCheckable(False)
        self.Decision_Action.setCheckable(False)
        self.Process_Action.setCheckable(False)
        print("1234")
        self.leftwidget.button = Process_Button('Loop', self)
        self.leftwidget.button.setStyleSheet("background-color: DodgerBlue")
        self.leftwidget.button.string = 'Start'
        self.leftwidget.button.ExtremePoint = 1
        self.leftwidget.button.setGeometry(240, 30, 210, 30)
        self.leftwidget.button.position.setX(240)
        self.leftwidget.button.position.setY(30)
        
        self.leftwidget.button.show()
        
    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        load_file_action = self.create_action("&Save plot",
            shortcut="Ctrl+S", slot=self.save_plot, 
            tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        self.add_menuactions(self.file_menu, 
            (load_file_action, None, quit_action))
        
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_menuactions(self.help_menu, (about_action,))



    def add_menuactions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
