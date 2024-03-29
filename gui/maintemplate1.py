# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maintemplate1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')
from my_poker_ai import traverse_actions #as traverse_actions
_translate = QtCore.QCoreApplication.translate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # setting up main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #setting up table
        self.table = QtWidgets.QLabel(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(90, 50, 601, 391))
        self.table.setText("")
        self.table.setPixmap(QtGui.QPixmap("../resources/table.png"))
        self.table.setScaledContents(True)
        self.table.setObjectName("table")
        #setting up player cards
        self.cards_p6_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p6_1.setGeometry(QtCore.QRect(130, 210, 61, 91))
        self.cards_p6_1.setText("")
        self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p6_1.setObjectName("cards_p6_1")
        self.cards_p6_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p6_2.setGeometry(QtCore.QRect(160, 210, 61, 91))
        self.cards_p6_2.setText("")
        self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p6_2.setObjectName("cards_p6_2")
        self.cards_p1_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p1_1.setGeometry(QtCore.QRect(240, 70, 61, 91))
        self.cards_p1_1.setText("")
        self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p1_1.setObjectName("cards_p1_1")
        self.cards_p1_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p1_2.setGeometry(QtCore.QRect(270, 70, 61, 91))
        self.cards_p1_2.setText("")
        self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p1_2.setObjectName("cards_p1_2")
        self.cards_p2_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p2_1.setGeometry(QtCore.QRect(440, 70, 61, 91))
        self.cards_p2_1.setText("")
        self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p2_1.setObjectName("cards_p2_1")
        self.cards_p2_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p2_2.setGeometry(QtCore.QRect(470, 70, 61, 91))
        self.cards_p2_2.setText("")
        self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p2_2.setObjectName("cards_p2_2")
        self.cards_p3_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p3_1.setGeometry(QtCore.QRect(570, 210, 61, 91))
        self.cards_p3_1.setText("")
        self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p3_1.setObjectName("cards_p3_1")
        self.cards_p3_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p3_2.setGeometry(QtCore.QRect(600, 210, 61, 91))
        self.cards_p3_2.setText("")
        self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p3_2.setObjectName("cards_p3_2")
        self.cards_p4_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p4_1.setGeometry(QtCore.QRect(440, 330, 61, 91))
        self.cards_p4_1.setText("")
        self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p4_1.setObjectName("cards_p4_1")
        self.cards_p4_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p4_2.setGeometry(QtCore.QRect(470, 330, 61, 91))
        self.cards_p4_2.setText("")
        self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p4_2.setObjectName("cards_p4_2")
        self.cards_p5_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p5_1.setGeometry(QtCore.QRect(260, 330, 61, 91))
        self.cards_p5_1.setText("")
        self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p5_1.setObjectName("cards_p5_1")
        self.cards_p5_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p5_2.setGeometry(QtCore.QRect(290, 330, 61, 91))
        self.cards_p5_2.setText("")
        self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/card_back.png"))
        self.cards_p5_2.setObjectName("cards_p5_2")
        #setting up players
        self.p1 = QtWidgets.QLabel(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(260, 10, 55, 16))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QLabel(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(460, 10, 55, 16))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QLabel(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(700, 230, 55, 16))
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QLabel(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(460, 450, 55, 16))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QLabel(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(280, 450, 55, 16))
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLabel(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(30, 230, 55, 16))
        self.p6.setObjectName("p6")
        #setting up text box to display number of chips
        self.p6_chips = QtWidgets.QLabel(self.centralwidget)
        self.p6_chips.setGeometry(QtCore.QRect(30, 250, 55, 16))
        self.p6_chips.setObjectName("p6_chips")
        self.p1_chips = QtWidgets.QLabel(self.centralwidget)
        self.p1_chips.setGeometry(QtCore.QRect(260, 30, 55, 16))
        self.p1_chips.setObjectName("p1_chips")
        self.p2_chips = QtWidgets.QLabel(self.centralwidget)
        self.p2_chips.setGeometry(QtCore.QRect(460, 30, 55, 16))
        self.p2_chips.setObjectName("p2_chips")
        self.p3_chips = QtWidgets.QLabel(self.centralwidget)
        self.p3_chips.setGeometry(QtCore.QRect(700, 250, 55, 16))
        self.p3_chips.setObjectName("p3_chips")
        self.p4_chips = QtWidgets.QLabel(self.centralwidget)
        self.p4_chips.setGeometry(QtCore.QRect(460, 470, 55, 16))
        self.p4_chips.setObjectName("p4_chips")
        self.p5_chips = QtWidgets.QLabel(self.centralwidget)
        self.p5_chips.setGeometry(QtCore.QRect(280, 470, 55, 16))
        self.p5_chips.setObjectName("p5_chips")
        #setting up start hand button
        self.startHand = QtWidgets.QPushButton(self.centralwidget)
        self.startHand.setGeometry(QtCore.QRect(340, 220, 121, 51))
        self.startHand.setObjectName("startHand")
        self.startHand.clicked.connect(self.funstartHand) ## function for start button
        #menu and status bars
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.p1.setText(_translate("MainWindow", "Player 1"))
        self.p2.setText(_translate("MainWindow", "Player 2"))
        self.p3.setText(_translate("MainWindow", "Player 3"))
        self.p4.setText(_translate("MainWindow", "Player 4"))
        self.p5.setText(_translate("MainWindow", "Player 5"))
        self.p6.setText(_translate("MainWindow", "Player 6"))
        self.p6_chips.setText(_translate("MainWindow", "Chips"))
        self.p1_chips.setText(_translate("MainWindow", "Chips"))
        self.p2_chips.setText(_translate("MainWindow", "Chips"))
        self.p3_chips.setText(_translate("MainWindow", "Chips"))
        self.p4_chips.setText(_translate("MainWindow", "Chips"))
        self.p5_chips.setText(_translate("MainWindow", "Chips"))
        self.startHand.setText(_translate("MainWindow", "Start Hand"))
    
    def funstartHand(self):
        self.startHand.hide()
        deck = traverse_actions.getshuffledDeck()
        rootNode = traverse_actions.Node(deck=deck)
        self.displaycurrentstate(rootNode)

    def displaycurrentstate(self,rootNode):
        self.p1_chips.setText(str(int(rootNode.pchips[0])))
        self.p2_chips.setText(str(int(rootNode.pchips[1])))
        self.p3_chips.setText(str(int(rootNode.pchips[2])))
        self.p4_chips.setText(str(int(rootNode.pchips[3])))
        self.p5_chips.setText(str(int(rootNode.pchips[4])))
        self.p6_chips.setText(str(int(rootNode.pchips[5])))

        #print("../resources/deck/"+rootNode.pCards[0][0]+".png")
        #rootNode.pFolded[0]=True
        if(rootNode.pFolded[0]):
            self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[0][0]+".png"))
            self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[0][1]+".png"))
        
        if(rootNode.pFolded[1]):
            self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[1][0]+".png"))
            self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[1][1]+".png"))
        
        if(rootNode.pFolded[2]):
            self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[2][0]+".png"))
            self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[2][1]+".png"))
        
        if(rootNode.pFolded[3]):
            self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[3][0]+".png"))
            self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[3][1]+".png"))
        
        if(rootNode.pFolded[4]):
            self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[4][0]+".png"))
            self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[4][1]+".png"))
        
        if(rootNode.pFolded[5]):
            self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[5][0]+".png"))
            self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/deck/"+rootNode.pCards[5][1]+".png"))

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
