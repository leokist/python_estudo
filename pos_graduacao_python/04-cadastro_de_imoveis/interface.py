# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(621, 663)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(190, 10, 281, 21))
        self.label_17.setObjectName("label_17")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 591, 591))
        self.groupBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 300, 541, 241))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Preco = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_Preco.setMaxLength(11)
        self.lineEdit_Preco.setObjectName("lineEdit_Preco")
        self.gridLayout_2.addWidget(self.lineEdit_Preco, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.lineEdit_Obs = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_Obs.setObjectName("lineEdit_Obs")
        self.gridLayout_2.addWidget(self.lineEdit_Obs, 3, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.lineEdit_Cond = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_Cond.setObjectName("lineEdit_Cond")
        self.gridLayout_2.addWidget(self.lineEdit_Cond, 4, 1, 1, 2)
        self.textEdit_Caract = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_Caract.setObjectName("textEdit_Caract")
        self.gridLayout_2.addWidget(self.textEdit_Caract, 1, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.textEdit_Desc = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_Desc.setObjectName("textEdit_Desc")
        self.gridLayout_2.addWidget(self.textEdit_Desc, 0, 1, 1, 2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 100, 539, 182))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Bairro = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Bairro.setObjectName("lineEdit_Bairro")
        self.gridLayout.addWidget(self.lineEdit_Bairro, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 3, 1, 1)
        self.cb_TipoNeg = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cb_TipoNeg.setObjectName("cb_TipoNeg")
        self.gridLayout.addWidget(self.cb_TipoNeg, 0, 2, 1, 1)
        self.lineEdit_Comp = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Comp.setObjectName("lineEdit_Comp")
        self.gridLayout.addWidget(self.lineEdit_Comp, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.cb_TipoImovel = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cb_TipoImovel.setObjectName("cb_TipoImovel")
        self.gridLayout.addWidget(self.cb_TipoImovel, 5, 2, 1, 1)
        self.cb_Status = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cb_Status.setObjectName("cb_Status")
        self.gridLayout.addWidget(self.cb_Status, 0, 4, 1, 1)
        self.lineEdit_End = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_End.setObjectName("lineEdit_End")
        self.gridLayout.addWidget(self.lineEdit_End, 1, 2, 1, 3)
        self.lineEdit_Num = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Num.setMaxLength(5)
        self.lineEdit_Num.setObjectName("lineEdit_Num")
        self.gridLayout.addWidget(self.lineEdit_Num, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.lineEdit_Cidade = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Cidade.setObjectName("lineEdit_Cidade")
        self.gridLayout.addWidget(self.lineEdit_Cidade, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit_Cep = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Cep.setMaxLength(8)
        self.lineEdit_Cep.setObjectName("lineEdit_Cep")
        self.gridLayout.addWidget(self.lineEdit_Cep, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.lineEdit_Est = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Est.setObjectName("lineEdit_Est")
        self.gridLayout.addWidget(self.lineEdit_Est, 3, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 2)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 238, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.lineEdit_ID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.horizontalLayout.addWidget(self.lineEdit_ID)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 70, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.bt_Consultar = QtWidgets.QPushButton(self.groupBox)
        self.bt_Consultar.setGeometry(QtCore.QRect(270, 40, 80, 25))
        self.bt_Consultar.setObjectName("bt_Consultar")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 560, 168, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.lineEdit_ID, self.bt_Consultar)
        mainWindow.setTabOrder(self.bt_Consultar, self.cb_TipoNeg)
        mainWindow.setTabOrder(self.cb_TipoNeg, self.cb_Status)
        mainWindow.setTabOrder(self.cb_Status, self.lineEdit_End)
        mainWindow.setTabOrder(self.lineEdit_End, self.lineEdit_Num)
        mainWindow.setTabOrder(self.lineEdit_Num, self.lineEdit_Comp)
        mainWindow.setTabOrder(self.lineEdit_Comp, self.lineEdit_Cep)
        mainWindow.setTabOrder(self.lineEdit_Cep, self.lineEdit_Est)
        mainWindow.setTabOrder(self.lineEdit_Est, self.lineEdit_Cidade)
        mainWindow.setTabOrder(self.lineEdit_Cidade, self.lineEdit_Bairro)
        mainWindow.setTabOrder(self.lineEdit_Bairro, self.cb_TipoImovel)
        mainWindow.setTabOrder(self.cb_TipoImovel, self.textEdit_Desc)
        mainWindow.setTabOrder(self.textEdit_Desc, self.textEdit_Caract)
        mainWindow.setTabOrder(self.textEdit_Caract, self.lineEdit_Preco)
        mainWindow.setTabOrder(self.lineEdit_Preco, self.lineEdit_Obs)
        mainWindow.setTabOrder(self.lineEdit_Obs, self.lineEdit_Cond)
        mainWindow.setTabOrder(self.lineEdit_Cond, self.pushButton)
        mainWindow.setTabOrder(self.pushButton, self.pushButton_2)

        #self.cb_TipoNeg.clear()
        self.cb_TipoNeg.addItem("one")

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "PY ACESSORIA - CADASTRO DE IMÓVEIS"))
        self.label_17.setText(_translate("mainWindow", "PY ACESSORIA - CADASTRO DE IMÓVEL"))
        self.groupBox.setTitle(_translate("mainWindow", "Cadastro/Consulta"))
        self.label_14.setText(_translate("mainWindow", "Preço:"))
        self.label_15.setText(_translate("mainWindow", "Observações:"))
        self.label_16.setText(_translate("mainWindow", "Condições:"))
        self.label_19.setText(_translate("mainWindow", "Características:"))
        self.label_12.setText(_translate("mainWindow", "Descrição:"))
        self.label_7.setText(_translate("mainWindow", "Cidade:"))
        self.label_9.setText(_translate("mainWindow", "Estado:"))
        self.label_3.setText(_translate("mainWindow", "Endereço:"))
        self.label_8.setText(_translate("mainWindow", "Bairro:"))
        self.label_2.setText(_translate("mainWindow", "Status"))
        self.label.setText(_translate("mainWindow", "Tipo de Negociação"))
        self.label_5.setText(_translate("mainWindow", "Complemento:"))
        self.label_11.setText(_translate("mainWindow", "Tipo de Imóvel:"))
        self.label_4.setText(_translate("mainWindow", "Número:"))
        self.label_6.setText(_translate("mainWindow", "CEP:"))
        self.label_18.setText(_translate("mainWindow", "Identificação"))
        self.label_10.setText(_translate("mainWindow", "A identificação é cadastrada automáticamente!"))
        self.bt_Consultar.setText(_translate("mainWindow", "Consultar"))
        self.pushButton.setText(_translate("mainWindow", "Cadastrar"))
        self.pushButton_2.setText(_translate("mainWindow", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

