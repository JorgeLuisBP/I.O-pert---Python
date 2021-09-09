# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(1183, 652)
        Principal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1183, 652))
        self.stackedWidget.setStyleSheet("background-color: rgb(43, 49, 61);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagePerl = QtWidgets.QWidget()
        self.pagePerl.setObjectName("pagePerl")
        self.tabla = QtWidgets.QTableWidget(self.pagePerl)
        self.tabla.setGeometry(QtCore.QRect(20, 140, 361, 391))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tabla.setFont(font)
        self.tabla.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"text-align: center;")
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(6)
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, item)
        self.tablaView = QtWidgets.QTableWidget(self.pagePerl)
        self.tablaView.setGeometry(QtCore.QRect(380, 140, 781, 391))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tablaView.setFont(font)
        self.tablaView.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);")
        self.tablaView.setObjectName("tablaView")
        self.tablaView.setColumnCount(12)
        self.tablaView.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaView.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.tablaView.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tablaView.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tablaView.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tablaView.setHorizontalHeaderItem(11, item)
        self.canVariable = QtWidgets.QSpinBox(self.pagePerl)
        self.canVariable.setGeometry(QtCore.QRect(260, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.canVariable.setFont(font)
        self.canVariable.setStyleSheet("color: rgb(255, 255, 255);")
        self.canVariable.setObjectName("canVariable")
        self.label_2 = QtWidgets.QLabel(self.pagePerl)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.btnGenera = QtWidgets.QPushButton(self.pagePerl)
        self.btnGenera.setGeometry(QtCore.QRect(360, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenera.setFont(font)
        self.btnGenera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenera.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 137, 191);")
        self.btnGenera.setObjectName("btnGenera")
        self.btnNuevo = QtWidgets.QPushButton(self.pagePerl)
        self.btnNuevo.setGeometry(QtCore.QRect(920, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnNuevo.setFont(font)
        self.btnNuevo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNuevo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 137, 191);")
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnCalcular = QtWidgets.QPushButton(self.pagePerl)
        self.btnCalcular.setGeometry(QtCore.QRect(780, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalcular.setFont(font)
        self.btnCalcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalcular.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 129, 120);\n"
"alternate-background-color: rgb(203, 209, 185);\n"
"background-color: rgb(46, 137, 191);")
        self.btnCalcular.setObjectName("btnCalcular")
        self.label_7 = QtWidgets.QLabel(self.pagePerl)
        self.label_7.setGeometry(QtCore.QRect(510, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.pagePerl)
        self.label_9.setGeometry(QtCore.QRect(0, 580, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.pagePerl)
        self.pageSimplex = QtWidgets.QWidget()
        self.pageSimplex.setObjectName("pageSimplex")
        self.label_5 = QtWidgets.QLabel(self.pageSimplex)
        self.label_5.setGeometry(QtCore.QRect(0, 580, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.btnGenerar = QtWidgets.QPushButton(self.pageSimplex)
        self.btnGenerar.setGeometry(QtCore.QRect(390, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerar.setStyleSheet("background-color: rgb(70, 151, 231);\n"
"color: rgb(255, 255, 255);")
        self.btnGenerar.setObjectName("btnGenerar")
        self.tablaRestri = QtWidgets.QTableWidget(self.pageSimplex)
        self.tablaRestri.setGeometry(QtCore.QRect(570, 110, 441, 241))
        self.tablaRestri.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.tablaRestri.setObjectName("tablaRestri")
        self.tablaRestri.setColumnCount(0)
        self.tablaRestri.setRowCount(0)
        self.label = QtWidgets.QLabel(self.pageSimplex)
        self.label.setGeometry(QtCore.QRect(40, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.tablaVaria = QtWidgets.QTableWidget(self.pageSimplex)
        self.tablaVaria.setGeometry(QtCore.QRect(40, 280, 461, 71))
        self.tablaVaria.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.tablaVaria.setObjectName("tablaVaria")
        self.tablaVaria.setColumnCount(0)
        self.tablaVaria.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVaria.setVerticalHeaderItem(0, item)
        self.btnNuevo_2 = QtWidgets.QPushButton(self.pageSimplex)
        self.btnNuevo_2.setGeometry(QtCore.QRect(580, 480, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnNuevo_2.setFont(font)
        self.btnNuevo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNuevo_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnNuevo_2.setAutoFillBackground(False)
        self.btnNuevo_2.setStyleSheet("background-color: rgb(70, 151, 231);\n"
"color: rgb(255, 255, 255);")
        self.btnNuevo_2.setObjectName("btnNuevo_2")
        self.canVariable_2 = QtWidgets.QSpinBox(self.pageSimplex)
        self.canVariable_2.setGeometry(QtCore.QRect(240, 90, 101, 31))
        self.canVariable_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.canVariable_2.setObjectName("canVariable_2")
        self.tablaIgual = QtWidgets.QTableWidget(self.pageSimplex)
        self.tablaIgual.setGeometry(QtCore.QRect(1010, 110, 111, 241))
        self.tablaIgual.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);")
        self.tablaIgual.setObjectName("tablaIgual")
        self.tablaIgual.setColumnCount(0)
        self.tablaIgual.setRowCount(0)
        self.btnResultado = QtWidgets.QPushButton(self.pageSimplex)
        self.btnResultado.setGeometry(QtCore.QRect(390, 480, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnResultado.setFont(font)
        self.btnResultado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnResultado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnResultado.setAutoFillBackground(False)
        self.btnResultado.setStyleSheet("background-color: rgb(70, 151, 231);\n"
"color: rgb(255, 255, 255);")
        self.btnResultado.setObjectName("btnResultado")
        self.canRestri = QtWidgets.QSpinBox(self.pageSimplex)
        self.canRestri.setGeometry(QtCore.QRect(240, 140, 101, 31))
        self.canRestri.setStyleSheet("color: rgb(255, 255, 255);")
        self.canRestri.setObjectName("canRestri")
        self.label_4 = QtWidgets.QLabel(self.pageSimplex)
        self.label_4.setGeometry(QtCore.QRect(570, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.pageSimplex)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.pageSimplex)
        self.label_6.setGeometry(QtCore.QRect(40, 250, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.pageSimplex)
        self.label_8.setGeometry(QtCore.QRect(500, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.pageSimplex)
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 21))
        self.menubar.setObjectName("menubar")
        self.menuMETODOS = QtWidgets.QMenu(self.menubar)
        self.menuMETODOS.setObjectName("menuMETODOS")
        Principal.setMenuBar(self.menubar)
        self.actionSimplex = QtWidgets.QAction(Principal)
        self.actionSimplex.setObjectName("actionSimplex")
        self.actionPerl = QtWidgets.QAction(Principal)
        self.actionPerl.setObjectName("actionPerl")
        self.menuMETODOS.addAction(self.actionSimplex)
        self.menuMETODOS.addSeparator()
        self.menuMETODOS.addAction(self.actionPerl)
        self.menubar.addAction(self.menuMETODOS.menuAction())

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Invesigación de operaciones"))
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Actividad"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Detalle"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Depende de"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "To"))
        item = self.tabla.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Tn"))
        item = self.tabla.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "Tp"))
        item = self.tablaView.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "D i,j"))
        item = self.tablaView.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "O i,j"))
        item = self.tablaView.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Ti0"))
        item = self.tablaView.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "Ti1"))
        item = self.tablaView.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Tj0"))
        item = self.tablaView.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "Tj1"))
        item = self.tablaView.horizontalHeaderItem(6)
        item.setText(_translate("Principal", "MT i,j"))
        item = self.tablaView.horizontalHeaderItem(7)
        item.setText(_translate("Principal", "Ml i,j"))
        item = self.tablaView.horizontalHeaderItem(8)
        item.setText(_translate("Principal", "Fecha inicio temprano"))
        item = self.tablaView.horizontalHeaderItem(9)
        item.setText(_translate("Principal", "Fecha inicio tardio"))
        item = self.tablaView.horizontalHeaderItem(10)
        item.setText(_translate("Principal", "Fecha final temprano"))
        item = self.tablaView.horizontalHeaderItem(11)
        item.setText(_translate("Principal", "Fecha final tardio"))
        self.label_2.setText(_translate("Principal", "Número de Actividades: "))
        self.btnGenera.setText(_translate("Principal", "Generar"))
        self.btnNuevo.setText(_translate("Principal", "Nuevo"))
        self.btnCalcular.setText(_translate("Principal", "Calcular"))
        self.label_7.setText(_translate("Principal", "Método Pert"))
        self.label_9.setText(_translate("Principal", "Autor: Baque Piloso Jorge Luis"))
        self.label_5.setText(_translate("Principal", "Autor: Baque Piloso Jorge Luis"))
        self.btnGenerar.setText(_translate("Principal", "Generar"))
        self.label.setText(_translate("Principal", "Cantidad de Variable:"))
        item = self.tablaVaria.verticalHeaderItem(0)
        item.setText(_translate("Principal", ">"))
        self.btnNuevo_2.setText(_translate("Principal", "Nuevo"))
        self.btnResultado.setText(_translate("Principal", "Mostrar Resultado"))
        self.label_4.setText(_translate("Principal", "Restricciones"))
        self.label_3.setText(_translate("Principal", "Cantidad de Restricciones: "))
        self.label_6.setText(_translate("Principal", "Función Objetivo"))
        self.label_8.setText(_translate("Principal", "Método Simplex"))
        self.menuMETODOS.setTitle(_translate("Principal", "METODOS"))
        self.actionSimplex.setText(_translate("Principal", "Simplex"))
        self.actionPerl.setText(_translate("Principal", "Perl"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
