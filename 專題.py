#左邊多設一個按鈕，link
#Loop 要有兩條線 (Ture , False)
#動態移動線 set widget
#setModule.getfile
#分割右上角格局

#Framework work
#Comilelist work

# =============================================================================
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure
# =============================================================================

import sys, os, random, cv2, matplotlib
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import Qt, QMimeData
import CompileList, SetModule, FrameworkDebugger
import Parameter


BasicClass = ['ExtremePointMode', 'originalMode', 'Decide', 'Loop']
 
AllFile = SetModule.getFile()

# =============================================================================
# for i in BasicClass:
#     print("BasicModule.%s"%i)
#     if "BasicModule.%s"%i in AllFile:
#         print("BasicModule%s"%i)
#         AllFile.remove("BasicModule%d"%i)
# =============================================================================
AllFile.remove('BasicModule.Decision')
AllFile.remove('BasicModule.ExtremePoint')
AllFile.remove('BasicModule.Loops')
AllFile.remove('BasicModule.Mode')
  

for i in AllFile:
    a = ['BasicModule.ExtremePointMode','BasicModule.originalMode',
         'BasicModule.Decide,BasicModule.Loop','BasicModule.Decision']
    exec('from '+ i + ' import*')

Type = ['BasicModule','TEST','UserdefinedClass']


i =0

script = []      #script
input =0
output = 0

button_number = -1 #button
button_name = []
buttonlist =[]

choice_button = 0

Decision_name = -1   #button_type
Mode_name = -1
Loop_name = -1
End_name = -1
Line_name = -1

can_draw = 0         #draw
start = 0
end = 0

button_pos = QPoint()


first_connect = 0
second_connect = 0

Line_now = ''


class add_Line(QLineF):
    
    name = 'Line'

    def __init__(self, title, parent=None):
        
        global Line_now
        global Line_name
        Line_name +=1
        
        super().__init__(title, parent)
        
        
        self.name = 'Line%s'%Line_name
        Line_now = 'Line%s'%Line_name
        print('HIHI: ',Line_now)


class Start_Button(QPushButton):
    
    global buttonlist
    global button_name
    global button_number
    global script


    dragable = 0

    position = QPoint()
    
    mode = 'process'
    string = 'Start'
    ExtremePoint = 0
    inputline = []  
    next_index = 'null'
    nodenum = 0
    TOF = ''
    name = 0
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        
        script.append([self.string,'ExtremePoint',self.inputline,self.next_index])
        
        self.name = self.string
        print(script)
    def showMenu(self):
        menu=QMenu()
        menu.addAction('編輯', self.Action1)
        menu.addAction('連接', self.Text)
        menu.addAction('刪除',self.deleteLater)
        menu.exec_(self.cursor().pos())
        
    
    def Text(self):
        
        global can_draw
        global start
        global end
        global first_connect
        global second_connect
        
        view = self.parent()

        can_draw +=1
        print(can_draw)
        if can_draw == 1:
            print("!!!!")
            
            start = QPointF(view.mapToScene(self.pos()))
            print("Start",start)
            print("THis Start",start)
            print("This End",end)
            print("Can Draw:" , can_draw)
            first_connect = self.string
            
        if can_draw == 2:
            print(can_draw,"!")
            end = QPointF(view.mapToScene(self.pos()))
            print(end)
            print("THis Start",start)
            print("This End",end)
            print("Can Draw:" , can_draw)
            can_draw -= 2
            print("Can Draw:" , can_draw)
            second_connect = self.string

            view.createLineItem(start,end,self.TOF)

       
        
    def Action1(self):

        print ('You selected Action 1')
        print(script)

        


        
    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return      
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()

            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        #super(DragButton, self).mouseMoveEvent(event)

    

    def mousePressEvent(self, event):
        global choice_button

        QPushButton.mousePressEvent(self, event)
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            

        if event.button() == Qt.RightButton:

            choice_button = self.objectName()

            
class End_Button(QPushButton):
    
    global buttonlist
    global button_name
    global button_number
    global script

    
    dragable = 0
    position = QPoint()
    
    inputline = []
    string = 'a'
    next_index = 'null'
    nodenum = 0
    mode = 'process'
    string = 'End'
    ExtremePoint = 0
    TOF = ''
    name = 0

       
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        script.append(['End%s' % End_name,'ExtremePoint',self.inputline,self.next_index])
        self.nodenum = End_name
        
        self.name = 'End%s' % End_name
        print(self.name)
        
        
    def showMenu(self):
        menu=QMenu()
        menu.addAction('編輯', self.Action1)
        menu.addAction('連接', self.Text)
        menu.addAction('刪除',self.deleteLater)
        menu.exec_(self.cursor().pos())
        
    def Text(self):
        
        global can_draw
        global start
        global end
        global first_connect
        global second_connect
        
        view = self.parent()

        can_draw +=1
        print(can_draw)
        if can_draw == 1:

            
            start = QPointF(view.mapToScene(self.pos()))

            first_connect = self.name
            
        if can_draw == 2:

            end = QPointF(view.mapToScene(self.pos()))

            can_draw -= 2

            second_connect = self.name
            view.createLineItem(start,end,self.TOF)

       
        
    def Action1(self):
        print(script)
        print ('You selected Action 1')


    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return      
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()

            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        #super(DragButton, self).mouseMoveEvent(event)

    

    def mousePressEvent(self, event):
        global choice_button

        QPushButton.mousePressEvent(self, event)
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            

        if event.button() == Qt.RightButton:

            choice_button = self.objectName()
            

class Process_Button(QPushButton):
    global buttonlist
    global button_name
    global button_number

    
    dragable = 0   
    position = QPoint() \
    
    inputline = []
    string = 'Mode'
    next_index = 'null'
    nodenum = 0
    mode = 'process'
    ExtremePoint = 0
    TOF = ''
    mode_choice = '可挑選'
    name = 0
       
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        script.append(['Mode%s' % Mode_name,self.mode_choice,self.inputline,[self.next_index]])
        
        self.nodenum = Mode_name
        self.name = 'Mode%s' % Mode_name
    
    def showMenu(self):
        menu=QMenu()
        menu.addAction('編輯', self.add_M)
        menu.addAction('連接', self.Text)
        menu.addAction('刪除',self.deleteLater)
        menu.exec_(self.cursor().pos())
    
    def add_M(self):

        dialog = Mode_Dialog(parent=self)
        
    def Text(self):
        
        global can_draw
        global start
        global end
        global first_connect
        global second_connect
            
        view = self.parent()

        can_draw +=1
        print(can_draw)
        if can_draw == 1:

            
            start = QPointF(view.mapToScene(self.pos()))

            first_connect = self.name
            
        if can_draw == 2:
            print(can_draw,"!")
            end = QPointF(view.mapToScene(self.pos()))

            can_draw -= 2

            second_connect = self.name
            view.createLineItem(start,end,self.TOF)

       
        
    def Action1(self):

        print ('You selected Action 1')
        
    def window_update(self,choice):

        self.mode_choice = choice
        self.setText(self.mode_choice)



    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return      
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()

            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        #super(DragButton, self).mouseMoveEvent(event)

    

    def mousePressEvent(self, event):
        global choice_button

        QPushButton.mousePressEvent(self, event)
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            

        if event.button() == Qt.RightButton:

            choice_button = self.objectName()
        
class Mode_Dialog(QDialog):
    global choice_button
    global button_name

    def __init__(self, parent=None):
            QDialog.__init__(self, parent)
            self.resize(200, 150)
            self.setWindowTitle('Loop')
            self.grid = QGridLayout()
            self.grid.setSpacing(10)

            self.mode_choice = QComboBox()
            for i in Type:
                self.mode_choice.addItem('%s'%i)

            self.grid.addWidget(QLabel('Mode Choice',self), 0, 0)
            self.grid.addWidget(self.mode_choice, 0, 1)
            self.symbol = QComboBox()
           
            self.printButton = QPushButton("OK")
            self.printButton.clicked.connect(self.sendback)
            
            self.buttonBox = QDialogButtonBox(parent=self)
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel) 


            self.buttonBox.rejected.connect(self.reject)
            self.hbox = QHBoxLayout()
            self.hbox.addWidget(self.printButton)
            self.hbox.addWidget(self.buttonBox)
            self.layout = QVBoxLayout()
            self.layout.addLayout(self.grid)
# =============================================================================
#             self.layout.addWidget(self.printButton)
# =============================================================================
            self.layout.addLayout(self.hbox)
            self.setLayout(self.layout)
            
            self.show()
            
    def sendback(self):
        global Loop_name
        button = self.parent()
        Loop_name += 1
        a = int(choice_button)
        
        
        
        button.window_update(self.mode_choice.currentText())
            

        self.close()

                    

            

            
class Decision_Button(QPushButton):
    global buttonlist
    global button_name
    global button_number
    global first_connect
    global second_connect
    
    dragable = 0   
    position = QPoint() 
    
    
    inputline = []
    true_index = ''
    false_index =''
    string = 'Decision'
    next_index = 'null'
    nodenum = 0
    mode = 'Decision'
    ExtremePoint = 0
    compare_num = 0.0
    compare_stuff = " "
    compare_symbol = " "
    parameter = []
    TOF = ''
    name = 0
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
        
        script.append(['Decision%s' % Decision_name,self.mode,self.inputline,[self.true_index,self.false_index],
                           [self.compare_stuff,self.compare_num
                           ,self.compare_symbol]])
        self.nodenum = Decision_name
        self.name = 'Decision%s' % Decision_name
    
    def showMenu(self):
        menu=QMenu()
        menu2=QMenu()
        menu2.addAction('True',self.T_Line)
        menu2.addAction('Flase',self.F_Line)
        menu.addAction('編輯', self.add_D)
        
        menu.addMenu(menu2)
        menu.addAction('刪除',self.deleteLater)
        menu.exec_(self.cursor().pos())
    def T_Line(self):
        self.TOF = True
        self.Text()
        
    def F_Line(self):
        self.TOF= False
        self.Text()
        
    def Text(self):
        
        global can_draw
        global start
        global end
        global first_connect
        global second_connect
        
        view = self.parent()

        can_draw +=1

        if can_draw == 1:

            
            start = QPointF(view.mapToScene(self.pos()))
            first_connect = self.name
            
        if can_draw == 2:

            end = QPointF(view.mapToScene(self.pos()))
            
            second_connect = self.name
            
            can_draw -= 2

            
            view.createLineItem(start,end,self.TOF)

       
        
    def Action1(self):

        print ('You selected Action 1')
    
    def window_update(self,varible,value,symbol):

        self.compare_stuff = varible
        self.compare_num = value
        self.compare_symbol = symbol

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return      
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()

            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        #super(DragButton, self).mouseMoveEvent(event)

    

    def mousePressEvent(self, event):
        global choice_button

        QPushButton.mousePressEvent(self, event)
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            

        if event.button() == Qt.RightButton:

            choice_button = self.objectName()
            
    def add_D(self):

        dialog = Decision_Dialog(parent=self)
    
    

            
class Loop_Button(QPushButton):
    global buttonlist
    global button_name
    global button_number

   
 
    inputline = []
    cont_index = 'null'
    break_index = 'null'
    dragable = 0
    string = 'Loop'
    nodenum = 0
    position = QPoint()
    mode = 'Loop'
    ExtremePoint = 0
    compare_num = None
    compare_stuff = None
    compare_symbol = None
    loop_time = 10
       
    name = 0
    
    TOF = ''
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)

        script.append(['Loop%s' % Loop_name,self.mode,self.inputline,[self.cont_index,self.break_index]
                           ,[self.compare_stuff,self.compare_num
                           ,self.compare_symbol],self.loop_time])
        self.nodenum = Loop_name
        self.name = 'Loop%s' % Loop_name
        
    def showMenu(self):
        menu=QMenu()
        menu2=QMenu()
        menu2.addAction('Continue',self.T_Line)
        menu2.addAction('End',self.F_Line)
        menu.addAction('編輯', self.add_L)
        
        menu.addMenu(menu2)
        menu.addAction('刪除',self.deleteLater)
        menu.exec_(self.cursor().pos())
    def T_Line(self):
        self.TOF = True
        self.Text()
        
    def F_Line(self):
        self.TOF= False
        self.Text()
        
    def Text(self):
        
        global can_draw
        global start
        global end
        global first_connect
        global second_connect 
        
        view = self.parent()

        can_draw +=1

        if can_draw == 1:

            
            start = QPointF(view.mapToScene(self.pos()))
            first_connect = self.name
                        
        if can_draw == 2:

            end = QPointF(view.mapToScene(self.pos()))
            second_connect = self.name
                        
            can_draw -= 2

            
            view.createLineItem(start,end,self.TOF)
            
    
    def window_update(self,varible,value,symbol):


        self.compare_stuff = varible
    
        self.compare_num = value
        self.compare_symbol = symbol
        
      
    def add_L(self):

        dialog = Loop_Dialog(parent=self)
       
        

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return      
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()

            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        #super(DragButton, self).mouseMoveEvent(event)

    

    def mousePressEvent(self, event):
        global choice_button

        QPushButton.mousePressEvent(self, event)
        
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            

        if event.button() == Qt.RightButton:

            choice_button = self.objectName()
    
    
        
   

            
class Loop_Dialog(QDialog):
    global choice_button
    global button_name

    def __init__(self, parent=None):
            QDialog.__init__(self, parent)
            self.resize(200, 150)
            self.setWindowTitle('Loop')
            self.grid = QGridLayout()
            self.grid.setSpacing(10)

            self.varible = QComboBox()
            self.varible.addItem('A')
            self.varible.addItem('B')
            self.grid.addWidget(QLabel('變數',self), 0, 0)
            self.grid.addWidget(self.varible, 0, 1)
            self.symbol = QComboBox()
            
            for i in ['>','<','=']:
                self.symbol.addItem(i)
                
            self.grid.addWidget(QLabel('運算子',self), 1, 0)
            self.grid.addWidget(self.symbol, 1, 1)
            
            self.counter = QLineEdit()
            self.grid.addWidget(QLabel('數值',self),2,0)
            self.grid.addWidget(self.counter,2,1)
            self.printButton = QPushButton("print")
            self.printButton.clicked.connect(self.sendback)
            
            self.buttonBox = QDialogButtonBox(parent=self)
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel
                                         |QDialogButtonBox.Ok) 

            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

            self.layout = QVBoxLayout()
            self.layout.addLayout(self.grid)
            self.layout.addWidget(self.printButton)
            self.layout.addWidget(self.buttonBox)
            self.setLayout(self.layout)
            
            self.show()
            
    def sendback(self):
        global Loop_name
        button = self.parent()
        Loop_name += 1
        a = int(choice_button)
        
        
        if a in range(len(script)):
            script[a]=['Loop%s' % Loop_name,'Loop',[input],[output],
                           [self.varible.currentText()
                           ,self.counter.text()],self.symbol.currentText(),10]            
        
        button.window_update(self.varible.currentText(),self.counter.text(),self.symbol.currentText())
            

        self.close()

            

class Decision_Dialog(QDialog):
    
    global choice_button
    global button_name
  
    def __init__(self, parent=None):
            QDialog.__init__(self, parent)
            self.resize(200, 150)
            self.setWindowTitle('Decision')
            self.grid = QGridLayout()
            self.grid.setSpacing(10)


            self.varible = QComboBox()
            self.varible.addItem('A')
            self.varible.addItem('B')
            self.grid.addWidget(QLabel('變數',self), 0, 0)
            self.grid.addWidget(self.varible, 0, 1)
            self.symbol = QComboBox()
            
            for i in ['>','<','=']:
                self.symbol.addItem(i)
                
            self.grid.addWidget(QLabel('運算子',self), 1, 0)
            self.grid.addWidget(self.symbol, 1, 1)
            
            self.counter = QLineEdit()
            self.grid.addWidget(QLabel('數值',self),2,0)
            self.grid.addWidget(self.counter,2,1)
            
            self.printButton = QPushButton("print")
            self.printButton.clicked.connect(self.sendback)
            
            self.buttonBox = QDialogButtonBox(parent=self)
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel
                                         |QDialogButtonBox.Ok)
            self.buttonBox.rejected.connect(self.reject)
            self.buttonBox.accepted.connect(self.accepted)


            self.layout = QVBoxLayout()
            self.layout.addLayout(self.grid)
            self.layout.addWidget(self.printButton)
            self.layout.addWidget(self.buttonBox)

            self.setLayout(self.layout)

            self.show()


    def sendback(self):
        global Decision_name
        button = self.parent()
        Decision_name += 1
        
        
        a = int(choice_button)
        

        if a in range(len(script)):
            script[a]=['Decision%s' % Decision_name,'Decision',[input],[output],
                           [self.varible.currentText()
                           ,self.counter.text()],self.symbol.currentText(),10]            
        button.window_update(self.varible.currentText(),self.counter.text(),
                             self.symbol.currentText())
            


        self.close()
        

class View(QGraphicsView):
    
    
    
    def add_Start(self):
        
        global buttonlist
        global button_number
        button_number += 1
        
        self.button = Start_Button('Start', self)
        self.button.setStyleSheet("background-color: black")
        self.button.string = 'Start'
        self.button.ExtremePoint = 1
        self.button.setGeometry(230, 80, 100, 30)
        self.button.position.setX(240)
        self.button.position.setY(30)
        self.button.setObjectName('%d' % button_number)
        button_name.append(self.button.objectName())
        buttonlist.append(self.button)


 
        
        


        
        self.button.show()
        
    def add_End(self):
        global buttonlist
        global button_number
        global End_name
        
        End_name += 1
        button_number += 1
        
        self.button = End_Button('End', self)
        self.button.setStyleSheet("background-color: black")
        self.button.string = 'End'
        self.button.ExtremePoint = 1
        self.button.setGeometry(230, 80, 100, 30)
        self.button.position.setX(240)
        self.button.position.setY(30)
        self.button.setObjectName('%d' % button_number)
        button_name.append(self.button.objectName())
        buttonlist.append(self.button)

        

        self.button.show()

    
    def add_Process(self):
        global buttonlist
        global button_number
        global Mode_name
        button_number += 1
        Mode_name +=1        
        
        self.button = Process_Button('Process', self)
        self.button.setStyleSheet("background-color: black")
        self.button.string = 'Process'
        self.button.ExtremePoint = 1
        self.button.setGeometry(230, 80, 100, 30)
        self.button.position.setX(240)
        self.button.position.setY(30)
        self.button.setObjectName('%d' % button_number)
        button_name.append(self.button.objectName())
        buttonlist.append(self.button)


        
        self.button.show()
    
    def add_Decision(self,):
        global buttonlist
        global button_number
        global Decision_name
        Decision_name +=1
        button_number += 1
        
        self.button = Decision_Button('Decision', self)
        self.button.setStyleSheet("background-color: black")
        self.button.string = 'Decision'
        self.button.ExtremePoint = 1
        self.button.setGeometry(230, 80, 100, 30)
        self.button.position.setX(240)
        self.button.position.setY(30)
        self.button.setObjectName('%d' % button_number)
        
        button_name.append(self.button.objectName())
        buttonlist.append(self.button)
              

        self.button.show()       
    def add_Loop(self):

        global button_number
        global Loop_name
        Loop_name +=1
        button_number += 1
        
        self.button = Loop_Button('Loop', self)
        self.button.setStyleSheet("background-color: black")
        self.button.string = 'Loop'
        self.button.ExtremePoint = 1
        self.button.setGeometry(230, 80, 100, 30)
        self.button.position.setX(240)
        self.button.position.setY(30)
        self.button.setObjectName('%d' % button_number)
        button_name.append(self.button.objectName())
        buttonlist.append(self.button)


        self.button.show() 
    
    
    def createLineItem(self,start,end,TOF):
        global i
        global first_connect
        global second_connect
        i +=1
        self.line = QGraphicsLineItem(add_Line(start, end))
        self.scene().addItem(self.line)
        self.update(TOF)
        
    def update(self,TOF):
        global buttonlist
        global first_connect
        global second_connect
        global Line_now
        
        print(first_connect)
        print(second_connect)
        for i in buttonlist:

            
            if i.name == first_connect:

                if i.TOF == True:
                    if i.mode == 'Loop':
                        i.cont_index = Line_now
                    else:
                        i.true_index = Line_now

                elif i.TOF == False:
                    if i.mode =='Loop':
                        i.break_index = Line_now
                    else:
                        i.false_index = Line_now
                        print(i.false_index)

                else:  
                    i.next_index = Line_now
                


                
            elif i.name == second_connect:
                i.inputline.append(Line_now)

 
    
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setScene(QGraphicsScene(self))
        self.setSceneRect(QRectF(self.viewport().rect()))
        

    def mousePressEvent(self, event):
        if can_draw == 1 :
            self._start = event.pos()


    def mouseReleaseEvent(self, event):
        if can_draw == 1:
            start = QPointF(self.mapToScene(self._start))
            
            end = self.mapToScene(event.pos())

            self.scene().addItem(
                QGraphicsLineItem(QLineF(start, end)))
            
            for point in (start, end):
                text = self.scene().addSimpleText(
                    '(%d, %d)' % (point.x(), point.y()))
                
                
                text.setBrush(Qt.blue)
                text.setPos(point)
                
    def dragEnterEvent(self, e):

        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):

        e.accept()

    def draw(self,start,end):
        
        

        self.scene().addItem(
                QGraphicsLineItem(QLineF(start, end)))



            
class AppForm(QMainWindow):
    

    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('專題')
        qss_file = open('black_style.qss').read()
        self.setStyleSheet(qss_file)
        
        self.setGeometry(200,100,1000,600)
        self.setAcceptDrops(True)
        self.create_menu()
        self.create_main_frame()
        
        self.cwd = os.getcwd()
        
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):


        e.setDropAction(Qt.MoveAction)
        e.accept()
        


    def save_File(self):
        global buttonlist

       
        
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "存檔",
                                    "./",
                                    "Text Files (*.txt)")

        f = open(fileName_choose,'w')

        a=0
        for i in buttonlist:

            if i.mode == 'process':

                if i.string == 'Mode':                                         #write 'Mode_' + i.string + str(i.nodenum), i.string, i.inputline, [i.next_index]
                    f.write('Mode_' + i.string + str(i.nodenum) + ' ')
                    f.write(i.string+' ')
                    f.write('[')
                    for j in i.inputline:
                        f.write(j+',')
                    f.write('] ')
                    f.write('[' + i.next_index + ']')
                else:
                    if i.string == 'End':                                       #write i.string+str(i.nodenum), 'ExtremePointMode', i.inputline, []
                        f.write(i.string + str(i.nodenum) + ' ')
                        f.write('ExtremePointMode ')
                        f.write('[')
                        for j in i.inputline:
                           f.write(j+',')
                        f.write('] ')
                        f.write('[]')
                    else:                                                       #write i.string, 'ExtremePointMode', i.inputline, [i.next_index]
                        f.write(i.string + ' ')
                        f.write('ExtremePointMode ')
                        f.write('[')
                        for j in i.inputline:
                           f.write(j+', ')
                        f.write('] ')
                        f.write('[')
                        f.write(i.next_index)
                        f.write(']')

            elif i.mode == 'Decision':                                          #write i.string+str(i.nodenum), 'Decide', i.inputline, [i.true_index, i.false_index], [i.compare_stuff, i.compare_num, i.compare_symbol]
                f.write(i.string + str(i.nodenum) + ' ')
                f.write('Decide ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write('] ')
                f.write('[' + i.true_index + ',' + i.false_index + '] ')
                if i.compare_stuff != None and i.compare_num != None and i.compare_symbol != None:
                    f.write('[' + i.compare_stuff + ',' + str(i.compare_num) +',' + i.compare_symbol + '] ')
                else:
                    f.write('[None,None,None] ')
                
            elif i.mode == 'Loop':                                              #write i.string+str(i.nodenum), i.string, i.inputline, [i.cont_index, i.break_index], [0, i.loop_time]
                f.write(i.string + str(i.nodenum) + ' ')
                f.write(i.string + ' ')
                f.write('[')
                for j in i.inputline:
                    f.write(j+',')
                f.write('] ')
                f.write('[' + i.cont_index + ',' + i.break_index + '] ')
                if i.compare_stuff != None and i.compare_num != None and i.compare_symbol != None:
                    f.write('[' + i.compare_stuff + ',' + str(i.compare_num) +',' + i.compare_symbol + '] ')
                else:
                    f.write('[None,None,None] ')
                f.write(str(i.loop_time))
            f.write('\n')
        f.close()
        
        
        if fileName_choose == "":
            self.console.setText("取消存檔")
            print("\n取消存檔")
            return
        a = str(fileName_choose)
        self.console.setText("存檔成功\n")
        print(fileName_choose)
        print("檔案類型:" ,filetype)


        
   
        
    def on_about(self):
        msg ="""
        
        *專題，加油。
        """
        QMessageBox.about(self, "簡介", msg.strip())
    
    def create_main_frame(self):
        self.main_frame = QWidget()

        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)


        hbox = QHBoxLayout()
        Button_box = QVBoxLayout()
        self.leftwidget = QWidget()
        self.view = View(self)

        
        self.Start_Button = QPushButton("Start")   
        self.Start_Button.setCheckable(True)
        self.Start_Button.clicked.connect(self.view.add_Start)
        self.End_Button = QPushButton("End")
        self.End_Button.setCheckable(True)
        self.End_Button.clicked.connect(self.view.add_End)
        self.Process_Button = QPushButton("Process")
        self.Process_Button.setCheckable(True)

        self.Process_Button.clicked.connect(self.view.add_Process)
        self.Loop_Button = QPushButton("Loop")
        self.Loop_Button.setCheckable(True)
        self.Loop_Button.clicked.connect(self.view.add_Loop)
        self.Decision_Button = QPushButton("Decision")
        self.Decision_Button.setCheckable(True)
        self.Decision_Button.clicked.connect(self.view.add_Decision)

        
        for w in [  self.Start_Button, self.End_Button, self.Loop_Button,
                    self.Decision_Button, self.Process_Button]:
            Button_box.addWidget(w)
            Button_box.setAlignment(w, Qt.AlignVCenter)
        

        self.console =QTextEdit()
        
        hbox.addLayout(Button_box)
        Hbox = QHBoxLayout()
        second_vbox = QVBoxLayout()
        
        self.S_Label = QLabel('Canvas')
        self.S_Label.setFixedHeight(15)
        second_vbox.addWidget(self.S_Label)
        second_vbox.addWidget(self.view)
        third_vbox = QVBoxLayout()
        self.Result_Label = QLabel('Result')
        third_vbox.addWidget(self.Result_Label)
        third_vbox.addWidget(self.canvas)
        third_vbox.addWidget(QLabel('Console',self))
        third_vbox.addWidget(self.console)

# =============================================================================
#         Hbox.addWidget(self.leftwidget)
# =============================================================================
        Hbox.addLayout(hbox)
        

# =============================================================================
#         Hbox.addLayout(second_vbox)
# =============================================================================
        Hbox.addLayout(second_vbox)
        Hbox.addLayout(third_vbox)
    
        self.main_frame.setLayout(Hbox)
        self.setCentralWidget(self.main_frame)
    
    def drawline(self):
        
        global can_draw
        global start
        global end
        
        self.view=View(self)
        can_draw +=1

        if can_draw == 1:

            start = QPointF(theview.mapToScene(self.pos()))

        if can_draw == 2:

            end = QPointF(theview.mapToScene(self.pos()))

            can_draw -= 2

            for point in (start, end):

                text = theview.scene().addSimpleText(
                    '(%d, %d)' % (point.x(), point.y()))
                
                
                text.setBrush(Qt.blue)
                text.setPos(point)
            theview.scene().addItem(QGraphicsLineItem(QLineF(start, end)))
            



        
        
        
    def Action1(self):

        self.view.hi(self)
        
        self.view.draw(start,end)


    def run_file(self):
        list=[
                ['Start', 'ExtremePointMode', [], ['line_0']],
        ['Loop1', 'Loop', ['line_1'], ['line_A', 'line_2'],[None, None, None], 15],
        ['Mode_A', 'testMode', ['line_0', 'line_2'], ['line_1']],
        ['End0', 'ExtremePointMode', ['line_A'], []],
        ]
        
        errormsg = FrameworkDebugger.TestErrorRaise(list)
        
        if errormsg  != '':
            errorlabel.setText(errormsg)
        else:
            CompileList.execBlockChart(list)
        
    def create_menu(self):        
        menu = self.menuBar().addMenu('File')
        read_action = menu.addAction('Export')
        read_action.triggered.connect(self.save_File)

        
        add_draw_action = self.menuBar().addAction('run')
        add_draw_action.triggered.connect(self.run_file)


def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
