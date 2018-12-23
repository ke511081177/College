# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, os, random
import pyautogui as pag
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel,QMainWindow,QApplication,QAction,QWidget,QHBoxLayout,QVBoxLayout,QFileDialog,QPushButton
from PyQt5.QtCore import QSize, Qt, QMimeData, QRect, QPoint, QPointF, QLineF, QLine
from PyQt5.QtGui import QPixmap, QDrag
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



class AppForm(QMainWindow,QLabel):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Put picture')
        self.create_menu()
        self.create_main_frame()

    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
       
        
        openfile_path = QFileDialog.getOpenFileName(self,'選擇文件','',"PNG (*.png)|*.png")
# =============================================================================
#         pixmap = QPixmap(openfile_path)
#         self.label.setPixmap(pixmap)
#         self.resize(pixmap.height(),pixmap.width())
# =============================================================================
# =============================================================================
#         self.label = QLabel(self)
#         self.label.setPixmap(pixmap)
#         self.label.resize(pixmap.width(), pixmap.height())
#         self.show()
#         #self.label.setPixmap(QPixmap(openfile_name))
# =============================================================================
        #self.label.setGeometry(60,50,800,400)
        


        print(pixmap)
        

# =============================================================================
#     
#     def mousePressEvent(self,e):
#         if e.buttons() != Qt.RightButton:
#             return
#         mimeData = QMimeData()
#         drag = QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setHotSpot(e.pos() - self.rect().topLeft())
#         drag.exec_(Qt.MoveAction)
# 
#     def mousePressEvent(self, e):
#         #self.label.mousePressEvent(self,e)
#         if e.button() == Qt.LeftButton:
#             print('press')
# 
#     def dragEnterEvent(self, e):
#         e.accept()
# 
#     def dropEvent(self, e):
#         position = e.pos()
#         self.label.move(position)
# 
#         e.setDropAction(Qt.MoveAction)
#         e.accept()
# 
# =============================================================================
        
    def mouseMoveEvent(self, event):
        print("On Hover") # event.pos().x(), event.pos().y()
        if event.buttons() != Qt.RightButton:
            self.label.pos = pag.position
            print(self.label.pos)
            #self.label.pos = event.pos
          
    def mousePressEvent(self, event):
        print(event)
        
    

  
    
    
    def on_about(self):
        msg ="""
        
        *可以把開個照片，然後丟進來拉來拉去這樣。
        """
        QMessageBox.about(self, "簡介", msg.strip())
    

    def create_main_frame(self):
        self.main_frame = QWidget()
        self.main_frame.resize(300,400)
        
        self.label = QLabel(self)
        self.label.setGeometry(40,40,800,600)
        self.label.setText('左')

         
        pixmap = QPixmap('image.png')
        self.label.setPixmap(pixmap)
        self.resize(1200,800)




# =============================================================================
#         self.canvas = FigureCanvas(self.fig)
#         self.canvas.setParent(self.main_frame)
# =============================================================================
       
        



        
        
 # =================================================================
#         self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
# =============================================================================
        


        hbox = QHBoxLayout()
        

        
        vbox = QVBoxLayout()
# =============================================================================
#         vbox.addWidget(self.mpl_toolbar)
#         vbox.addWidget(self.canvas)
# =============================================================================
        vbox.addLayout(hbox)
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
    
        
    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        load_file_action = self.create_action("&Open plot",
            shortcut="Ctrl+S", slot=self.save_plot, 
            tip="Open the plot")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        self.add_actions(self.file_menu, 
            (load_file_action, None, quit_action))
        
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
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
    main()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys, os, random
import pyautogui as pag
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel,QMainWindow,QApplication,QAction,QWidget,QHBoxLayout,QVBoxLayout,QFileDialog,QPushButton
from PyQt5.QtCore import QSize, Qt, QMimeData, QRect, QPoint, QPointF, QLineF, QLine
from PyQt5.QtGui import QPixmap, QDrag
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



class AppForm(QMainWindow,QLabel):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Put picture')
        self.create_menu()
        self.create_main_frame()

    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
       
        
        openfile_path = QFileDialog.getOpenFileName(self,'選擇文件','',"PNG (*.png)|*.png")
# =============================================================================
#         pixmap = QPixmap(openfile_path)
#         self.label.setPixmap(pixmap)
#         self.resize(pixmap.height(),pixmap.width())
# =============================================================================
# =============================================================================
#         self.label = QLabel(self)
#         self.label.setPixmap(pixmap)
#         self.label.resize(pixmap.width(), pixmap.height())
#         self.show()
#         #self.label.setPixmap(QPixmap(openfile_name))
# =============================================================================
        #self.label.setGeometry(60,50,800,400)
        


        print(pixmap)
        

# =============================================================================
#     
#     def mousePressEvent(self,e):
#         if e.buttons() != Qt.RightButton:
#             return
#         mimeData = QMimeData()
#         drag = QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setHotSpot(e.pos() - self.rect().topLeft())
#         drag.exec_(Qt.MoveAction)
# 
#     def mousePressEvent(self, e):
#         #self.label.mousePressEvent(self,e)
#         if e.button() == Qt.LeftButton:
#             print('press')
# 
#     def dragEnterEvent(self, e):
#         e.accept()
# 
#     def dropEvent(self, e):
#         position = e.pos()
#         self.label.move(position)
# 
#         e.setDropAction(Qt.MoveAction)
#         e.accept()
# 
# =============================================================================
        
    def mouseMoveEvent(self, event):
        print("On Hover") # event.pos().x(), event.pos().y()
        if event.buttons() != Qt.RightButton:
            self.label.pos = pag.position
            print(self.label.pos)
            #self.label.pos = event.pos
          
    def mousePressEvent(self, event):
        print(event)
        
    

  
    
    
    def on_about(self):
        msg ="""
        
        *可以把開個照片，然後丟進來拉來拉去這樣。
        """
        QMessageBox.about(self, "簡介", msg.strip())
    

    def create_main_frame(self):
        self.main_frame = QWidget()
        self.main_frame.resize(300,400)
        
        self.label = QLabel(self)
        self.label.setGeometry(40,40,800,600)
        self.label.setText('左')

         
        pixmap = QPixmap('image.png')
        self.label.setPixmap(pixmap)
        self.resize(1200,800)




# =============================================================================
#         self.canvas = FigureCanvas(self.fig)
#         self.canvas.setParent(self.main_frame)
# =============================================================================
       
        



        
        
 # =================================================================
#         self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
# =============================================================================
        


        hbox = QHBoxLayout()
        

        
        vbox = QVBoxLayout()
# =============================================================================
#         vbox.addWidget(self.mpl_toolbar)
#         vbox.addWidget(self.canvas)
# =============================================================================
        vbox.addLayout(hbox)
        
        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)
    
        
    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        load_file_action = self.create_action("&Open plot",
            shortcut="Ctrl+S", slot=self.save_plot, 
            tip="Open the plot")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        self.add_actions(self.file_menu, 
            (load_file_action, None, quit_action))
        
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
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
