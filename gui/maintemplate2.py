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
import my_poker_ai.main1 as traverse_actions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QLabel(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(90, 50, 801, 611))
        self.table.setText("")
        self.table.setPixmap(QtGui.QPixmap("../resources/table.png"))
        self.table.setScaledContents(True)
        self.table.setObjectName("table")
        self.cards_p6_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p6_1.setGeometry(QtCore.QRect(170, 310, 61, 91))
        self.cards_p6_1.setText("")
        self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p6_1.setObjectName("cards_p6_1")
        self.cards_p6_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p6_2.setGeometry(QtCore.QRect(200, 310, 61, 91))
        self.cards_p6_2.setText("")
        self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p6_2.setObjectName("cards_p6_2")
        self.cards_p1_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p1_1.setGeometry(QtCore.QRect(320, 110, 61, 91))
        self.cards_p1_1.setText("")
        self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p1_1.setObjectName("cards_p1_1")
        self.cards_p1_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p1_2.setGeometry(QtCore.QRect(350, 110, 61, 91))
        self.cards_p1_2.setText("")
        self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p1_2.setObjectName("cards_p1_2")
        self.cards_p2_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p2_1.setGeometry(QtCore.QRect(540, 110, 61, 91))
        self.cards_p2_1.setText("")
        self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p2_1.setObjectName("cards_p2_1")
        self.cards_p2_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p2_2.setGeometry(QtCore.QRect(570, 110, 61, 91))
        self.cards_p2_2.setText("")
        self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p2_2.setObjectName("cards_p2_2")
        self.cards_p3_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p3_1.setGeometry(QtCore.QRect(720, 300, 61, 91))
        self.cards_p3_1.setText("")
        self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p3_1.setObjectName("cards_p3_1")
        self.cards_p3_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p3_2.setGeometry(QtCore.QRect(750, 300, 61, 91))
        self.cards_p3_2.setText("")
        self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p3_2.setObjectName("cards_p3_2")
        self.cards_p4_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p4_1.setGeometry(QtCore.QRect(540, 480, 61, 91))
        self.cards_p4_1.setText("")
        self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p4_1.setObjectName("cards_p4_1")
        self.cards_p4_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p4_2.setGeometry(QtCore.QRect(570, 480, 61, 91))
        self.cards_p4_2.setText("")
        self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p4_2.setObjectName("cards_p4_2")
        self.cards_p5_1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p5_1.setGeometry(QtCore.QRect(330, 480, 61, 91))
        self.cards_p5_1.setText("")
        self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p5_1.setObjectName("cards_p5_1")
        self.cards_p5_2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_p5_2.setGeometry(QtCore.QRect(360, 480, 61, 91))
        self.cards_p5_2.setText("")
        self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_p5_2.setObjectName("cards_p5_2")
        self.p1 = QtWidgets.QLabel(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(330, 60, 55, 16))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QLabel(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(540, 60, 55, 16))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QLabel(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(820, 340, 55, 16))
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QLabel(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(550, 590, 55, 16))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QLabel(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(320, 590, 55, 16))
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLabel(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(120, 340, 55, 16))
        self.p6.setObjectName("p6")
        self.p6_chips = QtWidgets.QLabel(self.centralwidget)
        self.p6_chips.setGeometry(QtCore.QRect(120, 360, 55, 16))
        self.p6_chips.setObjectName("p6_chips")
        self.p1_chips = QtWidgets.QLabel(self.centralwidget)
        self.p1_chips.setGeometry(QtCore.QRect(330, 80, 55, 16))
        self.p1_chips.setObjectName("p1_chips")
        self.p2_chips = QtWidgets.QLabel(self.centralwidget)
        self.p2_chips.setGeometry(QtCore.QRect(540, 90, 55, 16))
        self.p2_chips.setObjectName("p2_chips")
        self.p3_chips = QtWidgets.QLabel(self.centralwidget)
        self.p3_chips.setGeometry(QtCore.QRect(820, 360, 55, 16))
        self.p3_chips.setObjectName("p3_chips")
        self.p4_chips = QtWidgets.QLabel(self.centralwidget)
        self.p4_chips.setGeometry(QtCore.QRect(560, 610, 55, 16))
        self.p4_chips.setObjectName("p4_chips")
        self.p5_chips = QtWidgets.QLabel(self.centralwidget)
        self.p5_chips.setGeometry(QtCore.QRect(330, 610, 55, 16))
        self.p5_chips.setObjectName("p5_chips")
        self.startHand = QtWidgets.QPushButton(self.centralwidget)
        self.startHand.setGeometry(QtCore.QRect(420, 310, 121, 51))
        self.startHand.setObjectName("startHand")
        self.p6_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p6_pBet.setGeometry(QtCore.QRect(260, 350, 55, 16))
        self.p6_pBet.setObjectName("p6_pBet")
        self.p1_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p1_pBet.setGeometry(QtCore.QRect(340, 210, 55, 16))
        self.p1_pBet.setObjectName("p1_pBet")
        self.p2_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p2_pBet.setGeometry(QtCore.QRect(560, 210, 55, 16))
        self.p2_pBet.setObjectName("p2_pBet")
        self.p3_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p3_pBet.setGeometry(QtCore.QRect(670, 340, 55, 16))
        self.p3_pBet.setObjectName("p3_pBet")
        self.p4_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p4_pBet.setGeometry(QtCore.QRect(570, 460, 55, 16))
        self.p4_pBet.setObjectName("p4_pBet")
        self.p5_pBet = QtWidgets.QLabel(self.centralwidget)
        self.p5_pBet.setGeometry(QtCore.QRect(350, 460, 55, 16))
        self.p5_pBet.setObjectName("p5_pBet")
        self.dealer = QtWidgets.QLabel(self.centralwidget)
        self.dealer.setGeometry(QtCore.QRect(140, 400, 21, 16))
        self.dealer.setText("")
        self.dealer.setPixmap(QtGui.QPixmap("../resources/dealer.png"))
        self.dealer.setScaledContents(True)
        self.dealer.setObjectName("dealer")
        self.turn_p1 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p1.setGeometry(QtCore.QRect(290, 180, 21, 16))
        self.turn_p1.setText("")
        self.turn_p1.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p1.setScaledContents(True)
        self.turn_p1.setObjectName("turn_p1")
        self.turn_p2 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p2.setGeometry(QtCore.QRect(510, 180, 21, 16))
        self.turn_p2.setText("")
        self.turn_p2.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p2.setScaledContents(True)
        self.turn_p2.setObjectName("turn_p2")
        self.turn_p3 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p3.setGeometry(QtCore.QRect(720, 280, 21, 16))
        self.turn_p3.setText("")
        self.turn_p3.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p3.setScaledContents(True)
        self.turn_p3.setObjectName("turn_p3")
        self.turn_p4 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p4.setGeometry(QtCore.QRect(640, 480, 21, 16))
        self.turn_p4.setText("")
        self.turn_p4.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p4.setScaledContents(True)
        self.turn_p4.setObjectName("turn_p4")
        self.turn_p5 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p5.setGeometry(QtCore.QRect(420, 480, 21, 16))
        self.turn_p5.setText("")
        self.turn_p5.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p5.setScaledContents(True)
        self.turn_p5.setObjectName("turn_p5")
        self.turn_p6 = QtWidgets.QLabel(self.centralwidget)
        self.turn_p6.setGeometry(QtCore.QRect(240, 400, 21, 16))
        self.turn_p6.setText("")
        self.turn_p6.setPixmap(QtGui.QPixmap("../resources/turn.png"))
        self.turn_p6.setScaledContents(True)
        self.turn_p6.setObjectName("turn_p6")
        self.cards_b1 = QtWidgets.QLabel(self.centralwidget)
        self.cards_b1.setGeometry(QtCore.QRect(340, 290, 61, 91))
        self.cards_b1.setText("")
        self.cards_b1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_b1.setObjectName("cards_b1")
        self.cards_b4 = QtWidgets.QLabel(self.centralwidget)
        self.cards_b4.setGeometry(QtCore.QRect(520, 290, 61, 91))
        self.cards_b4.setText("")
        self.cards_b4.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_b4.setObjectName("cards_b4")
        self.cards_b2 = QtWidgets.QLabel(self.centralwidget)
        self.cards_b2.setGeometry(QtCore.QRect(400, 290, 61, 91))
        self.cards_b2.setText("")
        self.cards_b2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_b2.setObjectName("cards_b2")
        self.cards_b3 = QtWidgets.QLabel(self.centralwidget)
        self.cards_b3.setGeometry(QtCore.QRect(460, 290, 61, 91))
        self.cards_b3.setText("")
        self.cards_b3.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_b3.setObjectName("cards_b3")
        self.cards_b5 = QtWidgets.QLabel(self.centralwidget)
        self.cards_b5.setGeometry(QtCore.QRect(580, 290, 61, 91))
        self.cards_b5.setText("")
        self.cards_b5.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        self.cards_b5.setObjectName("cards_b5")
        self.pot5 = QtWidgets.QLabel(self.centralwidget)
        self.pot5.setGeometry(QtCore.QRect(330, 390, 55, 16))
        self.pot5.setObjectName("pot5")
        self.pot3 = QtWidgets.QLabel(self.centralwidget)
        self.pot3.setGeometry(QtCore.QRect(400, 390, 55, 16))
        self.pot3.setObjectName("pot3")
        self.pot1 = QtWidgets.QLabel(self.centralwidget)
        self.pot1.setGeometry(QtCore.QRect(470, 390, 55, 16))
        self.pot1.setObjectName("pot1")
        self.pot2 = QtWidgets.QLabel(self.centralwidget)
        self.pot2.setGeometry(QtCore.QRect(540, 390, 55, 16))
        self.pot2.setObjectName("pot2")
        self.pot4 = QtWidgets.QLabel(self.centralwidget)
        self.pot4.setGeometry(QtCore.QRect(610, 390, 55, 16))
        self.pot4.setObjectName("pot4")
        self.allin_p1 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p1.setGeometry(QtCore.QRect(410, 110, 21, 16))
        self.allin_p1.setText("")
        self.allin_p1.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p1.setScaledContents(True)
        self.allin_p1.setObjectName("allin_p1")
        self.allin_p2 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p2.setGeometry(QtCore.QRect(630, 110, 21, 16))
        self.allin_p2.setText("")
        self.allin_p2.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p2.setScaledContents(True)
        self.allin_p2.setObjectName("allin_p2")
        self.allin_p4 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p4.setGeometry(QtCore.QRect(510, 550, 21, 16))
        self.allin_p4.setText("")
        self.allin_p4.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p4.setScaledContents(True)
        self.allin_p4.setObjectName("allin_p4")
        self.allin_p3 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p3.setGeometry(QtCore.QRect(790, 400, 21, 16))
        self.allin_p3.setText("")
        self.allin_p3.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p3.setScaledContents(True)
        self.allin_p3.setObjectName("allin_p3")
        self.allin_p5 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p5.setGeometry(QtCore.QRect(300, 550, 21, 16))
        self.allin_p5.setText("")
        self.allin_p5.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p5.setScaledContents(True)
        self.allin_p5.setObjectName("allin_p5")
        self.allin_p6 = QtWidgets.QLabel(self.centralwidget)
        self.allin_p6.setGeometry(QtCore.QRect(170, 290, 21, 16))
        self.allin_p6.setText("")
        self.allin_p6.setPixmap(QtGui.QPixmap("../resources/allin.png"))
        self.allin_p6.setScaledContents(True)
        self.allin_p6.setObjectName("allin_p6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 26))
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
        self.p6_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.p1_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.p2_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.p3_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.p4_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.p5_pBet.setText(_translate("MainWindow", "PbetCR"))
        self.pot5.setText(_translate("MainWindow", "Pot5: 0"))
        self.pot3.setText(_translate("MainWindow", "Pot3: 0"))
        self.pot1.setText(_translate("MainWindow", "Pot1: 0"))
        self.pot2.setText(_translate("MainWindow", "Pot2: 0"))
        self.pot4.setText(_translate("MainWindow", "Pot4: 0"))

        self.p6_pBet.setHidden(True)
        self.p1_pBet.setHidden(True)
        self.p2_pBet.setHidden(True)
        self.p3_pBet.setHidden(True)
        self.p4_pBet.setHidden(True)
        self.p5_pBet.setHidden(True)
        self.pot5.setHidden(True)
        self.pot3.setHidden(True)
        self.pot1.setHidden(True)
        self.pot2.setHidden(True)
        self.pot4.setHidden(True)

        self.allin_p1.setHidden(True)
        self.allin_p2.setHidden(True)
        self.allin_p4.setHidden(True)
        self.allin_p3.setHidden(True)
        self.allin_p5.setHidden(True)
        self.allin_p6.setHidden(True)

        self.cards_b1.setHidden(True)
        self.cards_b4.setHidden(True)
        self.cards_b2.setHidden(True)
        self.cards_b3.setHidden(True)
        self.cards_b5.setHidden(True)


        self.turn_p1.setHidden(True)
        self.turn_p2.setHidden(True)
        self.turn_p3.setHidden(True)
        self.turn_p4.setHidden(True)
        self.turn_p5.setHidden(True)
        self.turn_p6.setHidden(True)

        self.startHand.clicked.connect(self.funstartHand)

    def funstartHand(self):
        self.startHand.hide()
        deck = traverse_actions.getshuffledDeck()
        self.Node = traverse_actions.Node(deck=deck)
        self.displaycurrentstate(self.Node)
        #self.traversehand(self.Node)

    def displaycurrentstate(self,Node):
        ### Displaying player chips
        self.p1_chips.setText(str(int(Node.pchips[0])))
        self.p2_chips.setText(str(int(Node.pchips[1])))
        self.p3_chips.setText(str(int(Node.pchips[2])))
        self.p4_chips.setText(str(int(Node.pchips[3])))
        self.p5_chips.setText(str(int(Node.pchips[4])))
        self.p6_chips.setText(str(int(Node.pchips[5])))

        ## Displaying cards
        if(Node.pFolded[0]):
            self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p1_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[0][0]+".png"))
            self.cards_p1_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[0][1]+".png"))
        
        if(Node.pFolded[1]):
            self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p2_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[1][0]+".png"))
            self.cards_p2_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[1][1]+".png"))
        
        if(Node.pFolded[2]):
            self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p3_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[2][0]+".png"))
            self.cards_p3_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[2][1]+".png"))
        
        if(Node.pFolded[3]):
            self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p4_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[3][0]+".png"))
            self.cards_p4_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[3][1]+".png"))
        
        if(Node.pFolded[4]):
            self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p5_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[4][0]+".png"))
            self.cards_p5_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[4][1]+".png"))
        
        if(Node.pFolded[5]):
            self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
            self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/card_back_fold.png"))
        else:
            self.cards_p6_1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[5][0]+".png"))
            self.cards_p6_2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.pCards[5][1]+".png"))
        
        self.p6_pBet.setHidden(Node.pbetCurrentRound[5]==0)
        self.p1_pBet.setHidden(Node.pbetCurrentRound[0]==0)
        self.p2_pBet.setHidden(Node.pbetCurrentRound[1]==0)
        self.p3_pBet.setHidden(Node.pbetCurrentRound[2]==0)
        self.p4_pBet.setHidden(Node.pbetCurrentRound[3]==0)
        self.p5_pBet.setHidden(Node.pbetCurrentRound[4]==0)

        self.p6_pBet.setText(str(Node.pbetCurrentRound[5]))
        self.p1_pBet.setText(str(Node.pbetCurrentRound[0]))
        self.p2_pBet.setText(str(Node.pbetCurrentRound[1]))
        self.p3_pBet.setText(str(Node.pbetCurrentRound[2]))
        self.p4_pBet.setText(str(Node.pbetCurrentRound[3]))
        self.p5_pBet.setText(str(Node.pbetCurrentRound[4]))
        

        self.pot5.setHidden(True)
        self.pot3.setHidden(True)
        self.pot1.setHidden(True)
        self.pot2.setHidden(True)
        self.pot4.setHidden(True)

        if len(Node.chips)>0:  
            self.pot1.setHidden(False)
            self.pot1.setText("Pot1: "+str(int(Node.chips[0])))
        if len(Node.chips)>1:    
            self.pot2.setHidden(False)
            self.pot2.setText("Pot2: "+str(int(Node.chips[1])))
        if len(Node.chips)>2: 
            self.pot3.setHidden(False)
            self.pot3.setText("Pot3: "+str(int(Node.chips[2])))
        if len(Node.chips)>3: 
            self.pot4.setHidden(False)
            self.pot4.setText("Pot4: "+str(int(Node.chips[3])))
        if len(Node.chips)>4: 
            self.pot5.setHidden(False)
            self.pot5.setText("Pot5: "+str(int(Node.chips[4])))

        self.allin_p1.setHidden(not Node.pAllin[0])
        self.allin_p2.setHidden(not Node.pAllin[1])
        self.allin_p4.setHidden(not Node.pAllin[3])
        self.allin_p3.setHidden(not Node.pAllin[2])
        self.allin_p5.setHidden(not Node.pAllin[4])
        self.allin_p6.setHidden(not Node.pAllin[5])

        if Node.bettingRound==0:
            self.cards_b1.setHidden(True)
            self.cards_b2.setHidden(True)
            self.cards_b3.setHidden(True)
            self.cards_b4.setHidden(True)
            self.cards_b5.setHidden(True)
        elif Node.bettingRound==1:
            self.cards_b1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[0]+".png"))
            self.cards_b2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[1]+".png"))
            self.cards_b3.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[2]+".png"))
            self.cards_b1.setHidden(False)
            self.cards_b2.setHidden(False)
            self.cards_b3.setHidden(False)
            self.cards_b4.setHidden(True)
            self.cards_b5.setHidden(True)
        elif Node.bettingRound==2:
            self.cards_b1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[0]+".png"))
            self.cards_b2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[1]+".png"))
            self.cards_b3.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[2]+".png"))
            self.cards_b4.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[3]+".png"))
            self.cards_b1.setHidden(False)
            self.cards_b2.setHidden(False)
            self.cards_b3.setHidden(False)
            self.cards_b4.setHidden(False)
            self.cards_b5.setHidden(True)
        elif Node.bettingRound==3:
            self.cards_b1.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[0]+".png"))
            self.cards_b2.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[1]+".png"))
            self.cards_b3.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[2]+".png"))
            self.cards_b4.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[3]+".png"))
            self.cards_b5.setPixmap(QtGui.QPixmap("../resources/deck/"+Node.board[4]+".png"))
            self.cards_b1.setHidden(False)
            self.cards_b2.setHidden(False)
            self.cards_b3.setHidden(False)
            self.cards_b4.setHidden(False)
            self.cards_b5.setHidden(False)


        self.turn_p1.setHidden(True)
        self.turn_p2.setHidden(True)
        self.turn_p3.setHidden(True)
        self.turn_p4.setHidden(True)
        self.turn_p5.setHidden(True)
        self.turn_p6.setHidden(True)
        if(Node.currentPlayer==0):
            self.turn_p1.setHidden(False)
        if(Node.currentPlayer==1):
            self.turn_p2.setHidden(False)
        if(Node.currentPlayer==2):
            self.turn_p3.setHidden(False)
        if(Node.currentPlayer==3):
            self.turn_p4.setHidden(False)
        if(Node.currentPlayer==4):
            self.turn_p5.setHidden(False)
        if(Node.currentPlayer==5):
            self.turn_p6.setHidden(False)

    def chooseActionforTraversal(self,actions):
        #display info to user 
        #take input from user
        
        pass

    def traversehand(self,h):
        if traverse_actions.isTerminal(h):
            traverse_actions.showdown(h)
            self.displaycurrentstate(h)
            return
        elif traverse_actions.ischanceNode(h):
            traverse_actions.nextRound(h)
            self.displaycurrentstate(h)
            return 
        else:
            Ph = h.currentPlayer
            actions=traverse_actions.getActions(h)
            index = self.chooseActionforTraversal(actions)
            traverse_actions.doAction(h, actions[index])
            self.displaycurrentstate(h)
            return 

    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
