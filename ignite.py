from PyQt5 import QtCore, QtGui, QtWidgets

word1 = ""
word2 = ""
check = ""
num_code = 1
result1 = ""
result2 = ""
status = "G"
ct1 = {"0":"9", "1":"8", "2":"7", "3":"6", "4":"5",\
    "5":"4", "6":"3", "7":"2", "8":"1", "9":"0"}
ct2 = {'A':'N', 'B':'V', 'C':'Q', 'D':'P', 'E':'U',\
    'F':'Z', 'G':'W', 'H':'R', 'I':'O', 'J':'T',\
    'K':'Y', 'L':'X', 'M':'S', 'N':'A', 'O':'I',\
    'P':'D', 'Q':'C', 'R':'H', 'S':'M', 'T':'J',\
    'U':'E', 'V':'B', 'W':'G', 'X':'L', 'Y':'K', 'Z':'F',\
    "0":"5", "1":"6", "2":"7", "3":"8", "4":"9",\
    "9":"4", "8":"3", "7":"2", "6":"1", "5":"0",}
ct3 = {'A':'K', 'B':'L', 'C':'M', 'D':'N', 'E':'O',\
    'F':'P', 'G':'Q', 'H':'R', 'I':'S', 'J':'T',\
    'K':'U', 'L':'V', 'M':'W', 'N':'X', 'O':'Y',\
    'P':'Z', 'Q':'G', 'R':'H','S':'I', 'T':'J',\
    'U':'A', 'V':'B', 'W':'C', 'X':'D', 'Y':'E', 'Z':'F',\
    "0":"2", "1":"3", "2":"4", "3":"5", "4":"6",\
    "5":"7", "6":"8", "7":"9", "8":"0", "9":"1",}
reverse_ct3 = {'A':'U', 'B':'V', 'C':'W', 'D':'X', 'E':'Y',\
           'F':'Z', 'G':'Q', 'H':'R', 'I':'S', 'J':'T',\
           'K':'A', 'L':'B', 'M':'C', 'N':'D', 'O':'E',\
           'P':'F', 'Q':'G', 'R':'H','S':'I', 'T':'J',\
           'U':'K', 'V':'L', 'W':'M', 'X':'N', 'Y':'O', 'Z':'P',\
            "0":"8", "1":"9", "2":"0", "3":"1", "4":"2",\
            "5":"3", "6":"4", "7":"5", "8":"6", "9":"7"}
ct4 = {'A':'ZB', 'B':'AC', 'C':'BD', 'D':'CE', 'E':'DF',\
           'F':'EG', 'G':'FH', 'H':'GI', 'I':'HJ', 'J':'IK',\
           'K':'JL', 'L':'KM', 'M':'LN', 'N':'MO', 'O':'NP',\
           'P':'OQ', 'Q':'PR', 'R':'QS','S':'RT', 'T':'SU',\
           'U':'TV', 'V':'UW', 'W':'VX', 'X':'WY', 'Y':'XZ', 'Z':'YA', ' ':'SP',\
            "0":"91", "1":"02", "2":"13", "3":"24", "4":"35",
            "5":"46", "6":"57", "7":"68", "8":"79", "9":"80"}
reverse_ct4 = {'ZB':'A', 'AC':'B', 'BD':'C', 'CE':'D', 'DF':'E',\
           'EG':'F', 'FH':'G', 'GI':'H', 'HJ':'I', 'IK':'J',\
           'JL':'K', 'KM':'L', 'LN':'M', 'MO':'N', 'NP':'O',\
           'OQ':'P', 'PR':'Q', 'QS':'R','RT':'S', 'SU':'T',\
           'TV':'U', 'UW':'V', 'VX':'W', 'WY':'X', 'XZ':'Y', 'YA':'Z', 'SP':' ',\
            "91":"0", "02":"1", "13":"2", "24":"3", "35":"4",
            "46":"5", "57":"6", "68":"7", "79":"8", "80":"9"}
class Ui_Ignite(object):
    def setupUi(self, Ignite):
        Ignite.setObjectName("Ignite")
        Ignite.resize(481, 566)
        self.centralwidget = QtWidgets.QWidget(Ignite)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 441, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setLineWidth(2)
        self.frame.setText("")
        self.frame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame.setObjectName("frame")
        self.codetype1 = QtWidgets.QLabel(self.centralwidget)
        self.codetype1.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.codetype1.setObjectName("codetype1")
        self.codetype2 = QtWidgets.QLabel(self.centralwidget)
        self.codetype2.setGeometry(QtCore.QRect(100, 20, 71, 16))
        self.codetype2.setObjectName("codetype2")
        self.codetype3 = QtWidgets.QLabel(self.centralwidget)
        self.codetype3.setGeometry(QtCore.QRect(170, 20, 71, 16))
        self.codetype3.setObjectName("codetype3")
        self.codetype4 = QtWidgets.QLabel(self.centralwidget)
        self.codetype4.setGeometry(QtCore.QRect(240, 20, 71, 16))
        self.codetype4.setObjectName("codetype4")
        self.translate_label = QtWidgets.QLabel(self.centralwidget)
        self.translate_label.setGeometry(QtCore.QRect(410, 10, 21, 31))
        self.translate_label.setObjectName("translate_label")
        self.generate_label = QtWidgets.QLabel(self.centralwidget)
        self.generate_label.setGeometry(QtCore.QRect(430, 10, 21, 31))
        self.generate_label.setObjectName("generate_label")
        self.upper_label = QtWidgets.QLabel(self.centralwidget)
        self.upper_label.setGeometry(QtCore.QRect(30, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upper_label.setFont(font)
        self.upper_label.setObjectName("upper_label")
        self.lower_label = QtWidgets.QLabel(self.centralwidget)
        self.lower_label.setGeometry(QtCore.QRect(30, 100, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lower_label.setFont(font)
        self.lower_label.setObjectName("lower_label")
        self.upper_label_input = QtWidgets.QLabel(self.centralwidget)
        self.upper_label_input.setGeometry(QtCore.QRect(50, 40, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upper_label_input.setFont(font)
        self.upper_label_input.setText("")
        self.upper_label_input.setObjectName("upper_label_input")
        self.lower_label_output = QtWidgets.QLabel(self.centralwidget)
        self.lower_label_output.setGeometry(QtCore.QRect(60, 100, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lower_label_output.setFont(font)
        self.lower_label_output.setText("")
        self.lower_label_output.setObjectName("lower_label_output")

        """--------------------------------------------alphabets--------------------------------------------------"""

        #A
        self.A_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("A"))
        self.A_button.setGeometry(QtCore.QRect(20, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.A_button.setFont(font)
        self.A_button.setObjectName("A_button")
        #B
        self.B_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("B"))
        self.B_button.setGeometry(QtCore.QRect(70, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.B_button.setFont(font)
        self.B_button.setObjectName("B_button")
        #C
        self.C_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("C"))
        self.C_button.setGeometry(QtCore.QRect(120, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.C_button.setFont(font)
        self.C_button.setObjectName("C_button")
        #D
        self.D_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("D"))
        self.D_button.setGeometry(QtCore.QRect(170, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.D_button.setFont(font)
        self.D_button.setObjectName("D_button")
        #E
        self.E_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("E"))
        self.E_button.setGeometry(QtCore.QRect(220, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.E_button.setFont(font)
        self.E_button.setObjectName("E_button")
        #F
        self.F_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("F"))
        self.F_button.setGeometry(QtCore.QRect(270, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.F_button.setFont(font)
        self.F_button.setObjectName("F_button")
        #G
        self.G_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("G"))
        self.G_button.setGeometry(QtCore.QRect(20, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.G_button.setFont(font)
        self.G_button.setObjectName("G_button")
        #H
        self.H_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("H"))
        self.H_button.setGeometry(QtCore.QRect(70, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.H_button.setFont(font)
        self.H_button.setObjectName("H_button")
        #I
        self.I_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("I"))
        self.I_button.setGeometry(QtCore.QRect(120, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.I_button.setFont(font)
        self.I_button.setObjectName("I_button")
        #J
        self.J_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("J"))
        self.J_button.setGeometry(QtCore.QRect(170, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.J_button.setFont(font)
        self.J_button.setObjectName("J_button")
        #K
        self.K_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("K"))
        self.K_button.setGeometry(QtCore.QRect(220, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.K_button.setFont(font)
        self.K_button.setObjectName("K_button")
        #L
        self.L_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("L"))
        self.L_button.setGeometry(QtCore.QRect(270, 270, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.L_button.setFont(font)
        self.L_button.setObjectName("L_button")
        #M
        self.M_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("M"))
        self.M_button.setGeometry(QtCore.QRect(20, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.M_button.setFont(font)
        self.M_button.setObjectName("M_button")
        #N
        self.N_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("N"))
        self.N_button.setGeometry(QtCore.QRect(70, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.N_button.setFont(font)
        self.N_button.setObjectName("N_button")
        #O
        self.O_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("O"))
        self.O_button.setGeometry(QtCore.QRect(120, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.O_button.setFont(font)
        self.O_button.setObjectName("O_button")
        #P
        self.P_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("P"))
        self.P_button.setGeometry(QtCore.QRect(170, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.P_button.setFont(font)
        self.P_button.setObjectName("P_button")
        #Q
        self.Q_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("Q"))
        self.Q_button.setGeometry(QtCore.QRect(220, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Q_button.setFont(font)
        self.Q_button.setObjectName("Q_button")
        #R
        self.R_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("R"))
        self.R_button.setGeometry(QtCore.QRect(270, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.R_button.setFont(font)
        self.R_button.setObjectName("R_button")
        #S
        self.S_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("S"))
        self.S_button.setGeometry(QtCore.QRect(20, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.S_button.setFont(font)
        self.S_button.setObjectName("S_button")
        #T
        self.T_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("T"))
        self.T_button.setGeometry(QtCore.QRect(70, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.T_button.setFont(font)
        self.T_button.setObjectName("T_button")
        #U
        self.U_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("U"))
        self.U_button.setGeometry(QtCore.QRect(120, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.U_button.setFont(font)
        self.U_button.setObjectName("U_button")
        #V
        self.V_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("V"))
        self.V_button.setGeometry(QtCore.QRect(170, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.V_button.setFont(font)
        self.V_button.setObjectName("V_button")
        #W
        self.W_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("W"))
        self.W_button.setGeometry(QtCore.QRect(220, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.W_button.setFont(font)
        self.W_button.setObjectName("W_button")
        #X
        self.X_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("X"))
        self.X_button.setGeometry(QtCore.QRect(270, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.X_button.setFont(font)
        self.X_button.setObjectName("X_button")
        #Y
        self.Y_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("Y"))
        self.Y_button.setGeometry(QtCore.QRect(20, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Y_button.setFont(font)
        self.Y_button.setObjectName("Y_button")
        #Z
        self.Z_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("Z"))
        self.Z_button.setGeometry(QtCore.QRect(70, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Z_button.setFont(font)
        self.Z_button.setObjectName("Z_button")

        """--------------------------------------------alphabets--------------------------------------------------"""

        """--------------------------------------------numbers----------------------------------------------------"""

        #0
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('0'))
        self.zero_button.setGeometry(QtCore.QRect(120, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        #1
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('1'))
        self.one_button.setGeometry(QtCore.QRect(170, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        #2
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('2'))
        self.two_button.setGeometry(QtCore.QRect(220, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        #3
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('3'))
        self.three_button.setGeometry(QtCore.QRect(270, 420, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        #4
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('4'))
        self.four_button.setGeometry(QtCore.QRect(20, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        #5
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('5'))
        self.five_button.setGeometry(QtCore.QRect(70, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        #6
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('6'))
        self.six_button.setGeometry(QtCore.QRect(120, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        #7
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('7'))
        self.seven_button.setGeometry(QtCore.QRect(170, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        #8
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('8'))
        self.eight_button.setGeometry(QtCore.QRect(220, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        #9
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet('9'))
        self.nine_button.setGeometry(QtCore.QRect(270, 470, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")

        """--------------------------------------------numbers----------------------------------------------------"""

        """-------------------------------------------code type---------------------------------------------------"""

        #push button code type 1
        self.ct1_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.codetype(1))
        self.ct1_button.setGeometry(QtCore.QRect(20, 190, 111, 23))
        self.ct1_button.setObjectName("ct1_button")
        #push button code type 2
        self.cd2_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.codetype(2))
        self.cd2_button.setGeometry(QtCore.QRect(130, 190, 111, 23))
        self.cd2_button.setObjectName("cd2_button")
        #push button code type 3
        self.cd3_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.codetype(3))
        self.cd3_button.setGeometry(QtCore.QRect(240, 190, 111, 23))
        self.cd3_button.setObjectName("cd3_button")
        #push button code type 4
        self.cd4_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.codetype(4))
        self.cd4_button.setGeometry(QtCore.QRect(350, 190, 111, 23))
        self.cd4_button.setObjectName("cd4_button")

        """-------------------------------------------code type---------------------------------------------------"""

        """-------------------------------------------commands----------------------------------------------------"""

        #GO BACK
        self.goback = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet("<<<"))
        self.goback.setGeometry(QtCore.QRect(320, 220, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        #SPACE
        self.space = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.alphabet(" "))
        self.space.setGeometry(QtCore.QRect(400, 220, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.space.setFont(font)
        self.space.setObjectName("space")
        #TRANSLATE MODE
        self.translate_mode = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.mode("T"))
        self.translate_mode.setGeometry(QtCore.QRect(320, 320, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.translate_mode.setFont(font)
        self.translate_mode.setObjectName("translate_mode")
        #GENERATE MODE
        self.generate_mode = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.mode("G"))
        self.generate_mode.setGeometry(QtCore.QRect(400, 320, 61, 91))
        self.generate_mode.setObjectName("generate_mode")
        #TRANSLATE
        self.translate = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.command("T"))
        self.translate.setGeometry(QtCore.QRect(320, 420, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.translate.setFont(font)
        self.translate.setObjectName("translate")
        #GENERATE
        self.generate = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.command("G"))
        self.generate.setGeometry(QtCore.QRect(400, 420, 61, 91))
        self.generate.setObjectName("generate")

        """-------------------------------------------commands----------------------------------------------------"""

        Ignite.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ignite)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        Ignite.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ignite)
        self.statusbar.setObjectName("statusbar")
        Ignite.setStatusBar(self.statusbar)

        self.retranslateUi(Ignite)
        QtCore.QMetaObject.connectSlotsByName(Ignite)

    def retranslateUi(self, Ignite):
        _translate = QtCore.QCoreApplication.translate
        Ignite.setWindowTitle(_translate("Ignite", "IGNITE"))
        self.codetype1.setText(_translate("Ignite", "CODE TYPE 1"))
        self.codetype2.setText(_translate("Ignite", " "))
        self.codetype3.setText(_translate("Ignite", " "))
        self.codetype4.setText(_translate("Ignite", " "))
        self.translate_label.setText(_translate("Ignite", " "))
        self.generate_label.setText(_translate("Ignite", "G"))
        self.upper_label.setText(_translate("Ignite", "S :"))
        self.lower_label.setText(_translate("Ignite", "C :"))
        self.A_button.setText(_translate("Ignite", "A"))
        self.B_button.setText(_translate("Ignite", "B"))
        self.D_button.setText(_translate("Ignite", "D"))
        self.C_button.setText(_translate("Ignite", "C"))
        self.F_button.setText(_translate("Ignite", "F"))
        self.E_button.setText(_translate("Ignite", "E"))
        self.H_button.setText(_translate("Ignite", "H"))
        self.L_button.setText(_translate("Ignite", "L"))
        self.G_button.setText(_translate("Ignite", "G"))
        self.I_button.setText(_translate("Ignite", "I"))
        self.J_button.setText(_translate("Ignite", "J"))
        self.K_button.setText(_translate("Ignite", "K"))
        self.N_button.setText(_translate("Ignite", "N"))
        self.R_button.setText(_translate("Ignite", "R"))
        self.M_button.setText(_translate("Ignite", "M"))
        self.O_button.setText(_translate("Ignite", "O"))
        self.P_button.setText(_translate("Ignite", "P"))
        self.Q_button.setText(_translate("Ignite", "Q"))
        self.T_button.setText(_translate("Ignite", "T"))
        self.X_button.setText(_translate("Ignite", "X"))
        self.S_button.setText(_translate("Ignite", "S"))
        self.U_button.setText(_translate("Ignite", "U"))
        self.V_button.setText(_translate("Ignite", "V"))
        self.W_button.setText(_translate("Ignite", "W"))
        self.Z_button.setText(_translate("Ignite", "Z"))
        self.three_button.setText(_translate("Ignite", "3"))
        self.Y_button.setText(_translate("Ignite", "Y"))
        self.zero_button.setText(_translate("Ignite", "0"))
        self.one_button.setText(_translate("Ignite", "1"))
        self.two_button.setText(_translate("Ignite", "2"))
        self.five_button.setText(_translate("Ignite", "5"))
        self.nine_button.setText(_translate("Ignite", "9"))
        self.four_button.setText(_translate("Ignite", "4"))
        self.six_button.setText(_translate("Ignite", "6"))
        self.seven_button.setText(_translate("Ignite", "7"))
        self.eight_button.setText(_translate("Ignite", "8"))
        self.ct1_button.setText(_translate("Ignite", "CODE TYPE 1"))
        self.cd2_button.setText(_translate("Ignite", "CODE TYPE 2"))
        self.cd3_button.setText(_translate("Ignite", "CODE TYPE 3"))
        self.cd4_button.setText(_translate("Ignite", "CODE TYPE 4"))
        self.goback.setText(_translate("Ignite", "<<<"))
        self.space.setText(_translate("Ignite", "SPACE"))
        self.translate_mode.setText(_translate("Ignite", "TRANSLATE\n"
"MODE"))
        self.generate_mode.setText(_translate("Ignite", "GENERATE\n"
"MODE"))
        self.translate.setText(_translate("Ignite", "TRANSLATE"))
        self.generate.setText(_translate("Ignite", "GENERATE"))

    def alphabet(self, cha):
        global word1
        global word2
        if num_code == 4 and status == "G":
            if cha == "<<<":
                if len(word1) == 22 and len(word2) > 0:
                    word2 = word2[:-1]
                    self.upper_label_input.setText(word1+"\n"+word2)
                elif len(word1) > 0 and len(word2) == 0:
                    word1 = word1[:-1]
                    self.upper_label_input.setText(word1)
            elif len(word1) < 22 and word2 == "":
                word1 += cha
                self.upper_label_input.setText(word1)
            elif len(word1) == 22 and len(word2) <= 22:
                word2 += cha
                self.upper_label_input.setText(word1+"\n"+word2)
        if num_code == 4 and status == "T":
            if cha == "<<<":
                if len(word1) == 44 and len(word2) > 0:
                    word2 = word2[:-1]
                    self.upper_label_input.setText(word1+"\n"+word2)
                elif len(word1) > 0 and len(word2) == 0:
                    word1 = word1[:-1]
                    self.upper_label_input.setText(word1)
            elif len(word1) < 44 and word2 == "":
                word1 += cha
                self.upper_label_input.setText(word1)
            elif len(word1) == 44 and len(word2) <= 44:
                word2 += cha
                self.upper_label_input.setText(word1+"\n"+word2)
        elif num_code != 4:
            if cha == "<<<":
                if len(word1) == 45 and len(word2) > 0:
                    word2 = word2[:-1]
                    self.upper_label_input.setText(word1+"\n"+word2)
                elif len(word1) > 0 and len(word2) == 0:
                    word1 = word1[:-1]
                    self.upper_label_input.setText(word1)
            elif len(word1) < 45 and word2 == "":
                word1 += cha
                self.upper_label_input.setText(word1)
            elif len(word1) == 45 and len(word2) <= 45:
                word2 += cha
                self.upper_label_input.setText(word1+"\n"+word2)

    def mode(self, mode_tg):
        global word1
        global word2
        global status
        if mode_tg == "T":
            word1 = ""
            word2 = ""
            status = "T"
            self.translate_label.setText("T")
            self.generate_label.setText(" ")
            self.upper_label.setText("C :")
            self.lower_label.setText("S :")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
        elif mode_tg == "G":
            word1 = ""
            word2 = ""
            status = "G"
            self.translate_label.setText(" ")
            self.generate_label.setText("G")
            self.upper_label.setText("S :")
            self.lower_label.setText("C :")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
    def codetype(self, ct):
        global word1
        global word2
        global num_code
        if ct == 1:
            num_code = 1
            word1 = ""
            word2 = ""
            self.codetype1.setText("CODE TYPE 1")
            self.codetype2.setText(" ")
            self.codetype3.setText(" ")
            self.codetype4.setText(" ")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
        elif ct == 2:
            num_code = 2
            word1 = ""
            word2 = ""
            self.codetype1.setText(" ")
            self.codetype2.setText("CODE TYPE 2")
            self.codetype3.setText(" ")
            self.codetype4.setText(" ")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
        elif ct == 3:
            num_code = 3
            word1 = ""
            word2 = ""
            self.codetype1.setText(" ")
            self.codetype2.setText(" ")
            self.codetype3.setText("CODE TYPE 3")
            self.codetype4.setText(" ")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
        elif ct == 4:
            num_code = 4
            word1 = ""
            word2 = ""
            self.codetype1.setText(" ")
            self.codetype2.setText(" ")
            self.codetype3.setText(" ")
            self.codetype4.setText("CODE TYPE 4")
            self.upper_label_input.setText(word1)
            self.lower_label_output.setText("")
    def command(self, com_tg):
        global result1
        global result2
        if com_tg == "T" and status == "T":
            if word1 == "" and word2 == "":
                result1 = ""
                result2 = ""
                self.lower_label_output.setText(result1)
            elif num_code == 1:
                for i in word1:
                    if i.isalpha():
                        result1 += chr(155-ord(i))
                    elif i.isnumeric():
                        result1 += ct1.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalpha():
                        result2 += chr(155-ord(i))
                    elif i.isnumeric():
                        result2 += ct1.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 2:
                for i in word1:
                    if i.isalnum():
                        result1 += ct2.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalnum():
                        result2 += ct2.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 3:
                for i in word1:
                    if i.isalnum():
                        result1 += reverse_ct3.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalnum():
                        result2 += reverse_ct3.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 4 and len(word1)%2 == 0 and len(word2)%2 == 0:
                try:
                    for i in range(0, len(word1)-1, 2):
                        result1 += reverse_ct4.get(word1[i]+word1[i+1])
                    for i in range(0, len(word2)-1, 2):
                        result2 += reverse_ct4.get(word2[i]+word2[i+1])
                    if len(result1) > 0 and len(result2) == 0:
                        self.lower_label_output.setText(result1)
                    elif len(result1) > 0 and len(result2) > 0:
                        self.lower_label_output.setText(result1+"\n"+result2)
                    result1 = ""
                    result2 = ""
                except TypeError:
                    self.lower_label_output.setText("Inappropriate code")
            elif num_code == 4 and (len(word1)%2 != 0 or len(word2)%2 != 0):
                self.lower_label_output.setText("Inappropriate code")
        elif com_tg == "G" and status == "G":
            if word1 == "" and word2 == "":
                result1 = ""
                result2 = ""
                self.lower_label_output.setText(result1)
            elif num_code == 1:
                for i in word1:
                    if i.isalpha():
                        result1 += chr(155-ord(i))
                    elif i.isnumeric():
                        result1 += ct1.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalpha():
                        result2 += chr(155-ord(i))
                    elif i.isnumeric():
                        result2 += ct1.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 2:
                for i in word1:
                    if i.isalnum():
                        result1 += ct2.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalnum():
                        result2 += ct2.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 3:
                for i in word1:
                    if i.isalnum():
                        result1 += ct3.get(i)
                    else:
                        result1 += i
                for i in word2:
                    if i.isalnum():
                        result2 += ct3.get(i)
                    else:
                        result2 += i
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""
            elif num_code == 4:
                for i in word1:
                    result1 += ct4.get(i)
                for i in word2:
                    result2 += ct4.get(i)
                if len(result1) > 0 and len(result2) == 0:
                    self.lower_label_output.setText(result1)
                elif len(result1) > 0 and len(result2) > 0:
                    self.lower_label_output.setText(result1+"\n"+result2)
                result1 = ""
                result2 = ""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ignite = QtWidgets.QMainWindow()
    ui = Ui_Ignite()
    ui.setupUi(Ignite)
    Ignite.show()
    sys.exit(app.exec_())
