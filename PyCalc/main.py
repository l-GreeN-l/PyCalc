import PyQt5

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtGui

from Frames.frame import Ui_MainWindow
import sys

# app = QtWidgets.QApplication([])
# win = uic.loadUi("Frames/frame.ui")  # расположение вашего файла .ui
#
# win.show()
# sys.exit(app.exec())



def to_num(list=[]):
    list_num =[]
    for elem in list:
        list_num.append(int(elem))
    return list_num





class mywindow(QtWidgets.QMainWindow):

    str = ''
    result = 0.0

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon('Sourses/Py_Calc_icon.gif'))
        self.setWindowIcon(QIcon('Sourses/Py_Calc_icon.gif'))



        # Listeners buttons
        # Numerics buttons
        self.ui.one_btn.clicked.connect(self.one)
        self.ui.two_btn.clicked.connect(self.two)
        self.ui.three_btn.clicked.connect(self.three)
        self.ui.four_btn.clicked.connect(self.four)
        self.ui.five_btn.clicked.connect(self.five)
        self.ui.six_btn.clicked.connect(self.six)
        self.ui.seven_btn.clicked.connect(self.seven)
        self.ui.eight_btn.clicked.connect(self.eight)
        self.ui.nine_btn.clicked.connect(self.nine)
        self.ui.null_btn.clicked.connect(self.null)

        # Operation buttons
        self.ui.sum_btn.clicked.connect(self.sum)
        self.ui.sub_btn.clicked.connect(self.sub)
        self.ui.div_btn.clicked.connect(self.div)
        self.ui.mul_btn.clicked.connect(self.mul)

        #clear/ result
        self.ui.clear_btn.clicked.connect(self.clear)
        self.ui.result_btn.clicked.connect(self.result)
        pass


#-------------HMI buttons functions ------------------------------------------------------------------------------------


    # {----------Numeric-----------------------------------------}
    def one(self):
        # self.ui.TextBox.setText('1')

        self.str = self.str + '1'
        self.ui.TextBox.setText(self.str)
        pass

    def two(self):
        # self.ui.TextBox.setText('2')
        self.str = self.str + '2'
        self.ui.TextBox.setText(self.str)

        pass

    def three(self):
        # self.ui.TextBox.setText('3')
        self.str = self.str + '3'
        self.ui.TextBox.setText(self.str)

        pass

    def four(self):
        # self.ui.TextBox.setText('4')
        self.str = self.str + '4'
        self.ui.TextBox.setText(self.str)

        pass

    def five(self):
        # self.ui.TextBox.setText('5')
        self.str = self.str + '5'
        self.ui.TextBox.setText(self.str)

        pass

    def six(self):
        # self.ui.TextBox.setText('6')
        self.str = self.str + '6'
        self.ui.TextBox.setText(self.str)

        pass

    def seven(self):
        # self.ui.TextBox.setText('7')
        self.str = self.str + '7'
        self.ui.TextBox.setText(self.str)

        pass

    def eight(self):
        # self.ui.TextBox.setText('8')
        self.str = self.str + '8'
        self.ui.TextBox.setText(self.str)

        pass

    def nine(self):
        # self.ui.TextBox.setText('9')
        self.str = self.str + '9'
        self.ui.TextBox.setText(self.str)

        pass

    def null(self):
        # self.ui.TextBox.setText('0')
        self.str = self.str + '0'
        self.ui.TextBox.setText(self.str)

        pass




    # {------------------Operations---------------------------------------}


    def sum(self):
        # self.ui.TextBox.setText('sum')
        self.str = self.str + '+'
        self.ui.TextBox.setText(self.str)

        pass

    def sub(self):
        # self.ui.TextBox.setText('sub')
        self.str = self.str + '-'
        self.ui.TextBox.setText(self.str)

        pass

    def div(self):
        # self.ui.TextBox.setText('div')
        self.str = self.str + '/'
        self.ui.TextBox.setText(self.str)

        pass

    def mul(self):
        # self.ui.TextBox.setText('mul')
        self.str = self.str + '*'
        self.ui.TextBox.setText(self.str)

        pass


    # {--------------------Clear-----------------------------}

    def clear(self):
        # self.ui.TextBox.setText('clear')
        self.str = ''
        self.ui.TextBox.setText(self.str)

        pass






    # {---------------------Result button------------------------------------------------------}
    def result(self):
        # self.ui.TextBox.setText('result')

        if self.str != '':

            listNumeric =[]
            listOperation = []
            listPrioritets = []
            numeric =''

            # Parsing input stroke
            for elem in self.str:
                if elem == '+'  or elem == '-' :
                    listNumeric.append(numeric)
                    numeric=''
                    listOperation.append(elem)
                    listPrioritets.append(1)

                elif elem == '/' or elem == '*':
                    listNumeric.append(numeric)
                    numeric = ''
                    listOperation.append(elem)
                    listPrioritets.append(2)

                else: numeric = numeric+elem
                pass

            # last value append to array
            listNumeric.append(numeric)
            numeric = ''

            # transform string array to float
            listNumeric = to_num(listNumeric)






            # calculate result

            # First step operations = [*,/]

            operation = iter(listOperation)
            newlistNum=[]
            trigger = False
            for elem in range(1, len(listNumeric)):
                op = next(operation)

                if op =='/':
                    newlistNum.append(listNumeric[elem]/listNumeric[elem+1])
                    trigger = True


                elif op =='*':
                    newlistNum.append(listNumeric[elem]*listNumeric[elem+1])
                    trigger = True
                pass
            if trigger:
                listNumeric = newlistNum
                del newlistNum

            # del operation * / in array operation
            for elem in operation:
                if elem == '/' or elem == '*':
                    del elem
                pass


            # Second step operations = [+,-]
            self.result = listNumeric[0]
            operation = iter(listOperation)
            for elem in range(1,len(listNumeric)):
                op = next(operation)
                if op == '+':
                    self.result = self.result + listNumeric[elem]
                elif op =='-':
                    self.result = self.result - listNumeric[elem]


                pass

            print(listNumeric)
            print(listOperation)

            self.ui.TextBox.setText(str(self.result))

        else:
            self.ui.TextBox.setText('Введите выражение!')

        pass

# ----------------------------------------------------------------------------------------------------------------------

# End class

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

pass