# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/principal.ui'
#
# Created: Thu Jul  2 15:11:38 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName(_fromUtf8("Principal"))
        Principal.resize(529, 327)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Principal.sizePolicy().hasHeightForWidth())
        Principal.setSizePolicy(sizePolicy)
        Principal.setMinimumSize(QtCore.QSize(400, 292))
        Principal.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(Principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 491, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.canal1Tab = QtGui.QWidget()
        self.canal1Tab.setObjectName(_fromUtf8("canal1Tab"))
        self.groupBox_1 = QtGui.QGroupBox(self.canal1Tab)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_1.setCheckable(True)
        self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))
        self.unidadLbl_1 = QtGui.QLabel(self.groupBox_1)
        self.unidadLbl_1.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_1.setObjectName(_fromUtf8("unidadLbl_1"))
        self.unidad_1 = QtGui.QLineEdit(self.groupBox_1)
        self.unidad_1.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_1.setObjectName(_fromUtf8("unidad_1"))
        self.nombreLbl_1 = QtGui.QLabel(self.groupBox_1)
        self.nombreLbl_1.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_1.setObjectName(_fromUtf8("nombreLbl_1"))
        self.nombre_1 = QtGui.QLineEdit(self.groupBox_1)
        self.nombre_1.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_1.setObjectName(_fromUtf8("nombre_1"))
        self.calibrarBox_1 = QtGui.QGroupBox(self.groupBox_1)
        self.calibrarBox_1.setEnabled(True)
        self.calibrarBox_1.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_1.setCheckable(True)
        self.calibrarBox_1.setChecked(False)
        self.calibrarBox_1.setObjectName(_fromUtf8("calibrarBox_1"))
        self.pendienteLbl_1 = QtGui.QLabel(self.calibrarBox_1)
        self.pendienteLbl_1.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_1.setObjectName(_fromUtf8("pendienteLbl_1"))
        self.pendiente_1 = QtGui.QLineEdit(self.calibrarBox_1)
        self.pendiente_1.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_1.setObjectName(_fromUtf8("pendiente_1"))
        self.ordenadaLbl_1 = QtGui.QLabel(self.calibrarBox_1)
        self.ordenadaLbl_1.setGeometry(QtCore.QRect(0, 60, 71, 17))
        self.ordenadaLbl_1.setObjectName(_fromUtf8("ordenadaLbl_1"))
        self.ordenada_1 = QtGui.QLineEdit(self.calibrarBox_1)
        self.ordenada_1.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_1.setObjectName(_fromUtf8("ordenada_1"))
        self.tabWidget.addTab(self.canal1Tab, _fromUtf8(""))
        self.canal2Tab = QtGui.QWidget()
        self.canal2Tab.setObjectName(_fromUtf8("canal2Tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.canal2Tab)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.unidadLbl_2 = QtGui.QLabel(self.groupBox_2)
        self.unidadLbl_2.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_2.setObjectName(_fromUtf8("unidadLbl_2"))
        self.unidad_2 = QtGui.QLineEdit(self.groupBox_2)
        self.unidad_2.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_2.setObjectName(_fromUtf8("unidad_2"))
        self.nombreLbl_2 = QtGui.QLabel(self.groupBox_2)
        self.nombreLbl_2.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_2.setObjectName(_fromUtf8("nombreLbl_2"))
        self.nombre_2 = QtGui.QLineEdit(self.groupBox_2)
        self.nombre_2.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_2.setObjectName(_fromUtf8("nombre_2"))
        self.calibrarBox_2 = QtGui.QGroupBox(self.groupBox_2)
        self.calibrarBox_2.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_2.setCheckable(True)
        self.calibrarBox_2.setChecked(False)
        self.calibrarBox_2.setObjectName(_fromUtf8("calibrarBox_2"))
        self.pendienteLbl_2 = QtGui.QLabel(self.calibrarBox_2)
        self.pendienteLbl_2.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_2.setObjectName(_fromUtf8("pendienteLbl_2"))
        self.pendiente_2 = QtGui.QLineEdit(self.calibrarBox_2)
        self.pendiente_2.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_2.setObjectName(_fromUtf8("pendiente_2"))
        self.ordenadaLbl_2 = QtGui.QLabel(self.calibrarBox_2)
        self.ordenadaLbl_2.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_2.setObjectName(_fromUtf8("ordenadaLbl_2"))
        self.ordenada_2 = QtGui.QLineEdit(self.calibrarBox_2)
        self.ordenada_2.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_2.setObjectName(_fromUtf8("ordenada_2"))
        self.tabWidget.addTab(self.canal2Tab, _fromUtf8(""))
        self.canal3Tab = QtGui.QWidget()
        self.canal3Tab.setObjectName(_fromUtf8("canal3Tab"))
        self.groupBox_3 = QtGui.QGroupBox(self.canal3Tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.unidadLbl_3 = QtGui.QLabel(self.groupBox_3)
        self.unidadLbl_3.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_3.setObjectName(_fromUtf8("unidadLbl_3"))
        self.unidad_3 = QtGui.QLineEdit(self.groupBox_3)
        self.unidad_3.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_3.setObjectName(_fromUtf8("unidad_3"))
        self.nombreLbl_3 = QtGui.QLabel(self.groupBox_3)
        self.nombreLbl_3.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_3.setObjectName(_fromUtf8("nombreLbl_3"))
        self.nombre_3 = QtGui.QLineEdit(self.groupBox_3)
        self.nombre_3.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_3.setObjectName(_fromUtf8("nombre_3"))
        self.calibrarBox_3 = QtGui.QGroupBox(self.groupBox_3)
        self.calibrarBox_3.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_3.setCheckable(True)
        self.calibrarBox_3.setChecked(False)
        self.calibrarBox_3.setObjectName(_fromUtf8("calibrarBox_3"))
        self.pendienteLbl_3 = QtGui.QLabel(self.calibrarBox_3)
        self.pendienteLbl_3.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_3.setObjectName(_fromUtf8("pendienteLbl_3"))
        self.pendiente_3 = QtGui.QLineEdit(self.calibrarBox_3)
        self.pendiente_3.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_3.setObjectName(_fromUtf8("pendiente_3"))
        self.ordenadaLbl_3 = QtGui.QLabel(self.calibrarBox_3)
        self.ordenadaLbl_3.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_3.setObjectName(_fromUtf8("ordenadaLbl_3"))
        self.ordenada_3 = QtGui.QLineEdit(self.calibrarBox_3)
        self.ordenada_3.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_3.setObjectName(_fromUtf8("ordenada_3"))
        self.tabWidget.addTab(self.canal3Tab, _fromUtf8(""))
        self.canal4Tab = QtGui.QWidget()
        self.canal4Tab.setObjectName(_fromUtf8("canal4Tab"))
        self.groupBox_4 = QtGui.QGroupBox(self.canal4Tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.unidadLbl_4 = QtGui.QLabel(self.groupBox_4)
        self.unidadLbl_4.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_4.setObjectName(_fromUtf8("unidadLbl_4"))
        self.unidad_4 = QtGui.QLineEdit(self.groupBox_4)
        self.unidad_4.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_4.setObjectName(_fromUtf8("unidad_4"))
        self.nombreLbl_4 = QtGui.QLabel(self.groupBox_4)
        self.nombreLbl_4.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_4.setObjectName(_fromUtf8("nombreLbl_4"))
        self.nombre_4 = QtGui.QLineEdit(self.groupBox_4)
        self.nombre_4.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_4.setObjectName(_fromUtf8("nombre_4"))
        self.calibrarBox_4 = QtGui.QGroupBox(self.groupBox_4)
        self.calibrarBox_4.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_4.setCheckable(True)
        self.calibrarBox_4.setChecked(False)
        self.calibrarBox_4.setObjectName(_fromUtf8("calibrarBox_4"))
        self.pendienteLbl_4 = QtGui.QLabel(self.calibrarBox_4)
        self.pendienteLbl_4.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_4.setObjectName(_fromUtf8("pendienteLbl_4"))
        self.pendiente_4 = QtGui.QLineEdit(self.calibrarBox_4)
        self.pendiente_4.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_4.setObjectName(_fromUtf8("pendiente_4"))
        self.ordenadaLbl_4 = QtGui.QLabel(self.calibrarBox_4)
        self.ordenadaLbl_4.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_4.setObjectName(_fromUtf8("ordenadaLbl_4"))
        self.ordenada_4 = QtGui.QLineEdit(self.calibrarBox_4)
        self.ordenada_4.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_4.setObjectName(_fromUtf8("ordenada_4"))
        self.tabWidget.addTab(self.canal4Tab, _fromUtf8(""))
        self.canal5Tab = QtGui.QWidget()
        self.canal5Tab.setObjectName(_fromUtf8("canal5Tab"))
        self.groupBox_5 = QtGui.QGroupBox(self.canal5Tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.unidadLbl_5 = QtGui.QLabel(self.groupBox_5)
        self.unidadLbl_5.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_5.setObjectName(_fromUtf8("unidadLbl_5"))
        self.unidad_5 = QtGui.QLineEdit(self.groupBox_5)
        self.unidad_5.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_5.setObjectName(_fromUtf8("unidad_5"))
        self.nombreLbl_5 = QtGui.QLabel(self.groupBox_5)
        self.nombreLbl_5.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_5.setObjectName(_fromUtf8("nombreLbl_5"))
        self.nombre_5 = QtGui.QLineEdit(self.groupBox_5)
        self.nombre_5.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_5.setObjectName(_fromUtf8("nombre_5"))
        self.calibrarBox_5 = QtGui.QGroupBox(self.groupBox_5)
        self.calibrarBox_5.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_5.setCheckable(True)
        self.calibrarBox_5.setChecked(False)
        self.calibrarBox_5.setObjectName(_fromUtf8("calibrarBox_5"))
        self.pendienteLbl_5 = QtGui.QLabel(self.calibrarBox_5)
        self.pendienteLbl_5.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_5.setObjectName(_fromUtf8("pendienteLbl_5"))
        self.pendiente_5 = QtGui.QLineEdit(self.calibrarBox_5)
        self.pendiente_5.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_5.setObjectName(_fromUtf8("pendiente_5"))
        self.ordenadaLbl_5 = QtGui.QLabel(self.calibrarBox_5)
        self.ordenadaLbl_5.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_5.setObjectName(_fromUtf8("ordenadaLbl_5"))
        self.ordenada_5 = QtGui.QLineEdit(self.calibrarBox_5)
        self.ordenada_5.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_5.setObjectName(_fromUtf8("ordenada_5"))
        self.tabWidget.addTab(self.canal5Tab, _fromUtf8(""))
        self.canal6Tab = QtGui.QWidget()
        self.canal6Tab.setObjectName(_fromUtf8("canal6Tab"))
        self.groupBox_6 = QtGui.QGroupBox(self.canal6Tab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setChecked(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.unidadLbl_6 = QtGui.QLabel(self.groupBox_6)
        self.unidadLbl_6.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_6.setObjectName(_fromUtf8("unidadLbl_6"))
        self.unidad_6 = QtGui.QLineEdit(self.groupBox_6)
        self.unidad_6.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_6.setObjectName(_fromUtf8("unidad_6"))
        self.nombreLbl_6 = QtGui.QLabel(self.groupBox_6)
        self.nombreLbl_6.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_6.setObjectName(_fromUtf8("nombreLbl_6"))
        self.nombre_6 = QtGui.QLineEdit(self.groupBox_6)
        self.nombre_6.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_6.setObjectName(_fromUtf8("nombre_6"))
        self.calibrarBox_6 = QtGui.QGroupBox(self.groupBox_6)
        self.calibrarBox_6.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_6.setCheckable(True)
        self.calibrarBox_6.setChecked(False)
        self.calibrarBox_6.setObjectName(_fromUtf8("calibrarBox_6"))
        self.pendienteLbl_6 = QtGui.QLabel(self.calibrarBox_6)
        self.pendienteLbl_6.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_6.setObjectName(_fromUtf8("pendienteLbl_6"))
        self.pendiente_6 = QtGui.QLineEdit(self.calibrarBox_6)
        self.pendiente_6.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_6.setObjectName(_fromUtf8("pendiente_6"))
        self.ordenadaLbl_6 = QtGui.QLabel(self.calibrarBox_6)
        self.ordenadaLbl_6.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_6.setObjectName(_fromUtf8("ordenadaLbl_6"))
        self.ordenada_6 = QtGui.QLineEdit(self.calibrarBox_6)
        self.ordenada_6.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_6.setObjectName(_fromUtf8("ordenada_6"))
        self.tabWidget.addTab(self.canal6Tab, _fromUtf8(""))
        self.canal7Tab = QtGui.QWidget()
        self.canal7Tab.setObjectName(_fromUtf8("canal7Tab"))
        self.groupBox_7 = QtGui.QGroupBox(self.canal7Tab)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.unidadLbl_7 = QtGui.QLabel(self.groupBox_7)
        self.unidadLbl_7.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_7.setObjectName(_fromUtf8("unidadLbl_7"))
        self.unidad_7 = QtGui.QLineEdit(self.groupBox_7)
        self.unidad_7.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_7.setObjectName(_fromUtf8("unidad_7"))
        self.nombreLbl_7 = QtGui.QLabel(self.groupBox_7)
        self.nombreLbl_7.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_7.setObjectName(_fromUtf8("nombreLbl_7"))
        self.nombre_7 = QtGui.QLineEdit(self.groupBox_7)
        self.nombre_7.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_7.setObjectName(_fromUtf8("nombre_7"))
        self.calibrarBox_7 = QtGui.QGroupBox(self.groupBox_7)
        self.calibrarBox_7.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_7.setCheckable(True)
        self.calibrarBox_7.setChecked(False)
        self.calibrarBox_7.setObjectName(_fromUtf8("calibrarBox_7"))
        self.pendienteLbl_7 = QtGui.QLabel(self.calibrarBox_7)
        self.pendienteLbl_7.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_7.setObjectName(_fromUtf8("pendienteLbl_7"))
        self.pendiente_7 = QtGui.QLineEdit(self.calibrarBox_7)
        self.pendiente_7.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_7.setObjectName(_fromUtf8("pendiente_7"))
        self.ordenadaLbl_7 = QtGui.QLabel(self.calibrarBox_7)
        self.ordenadaLbl_7.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_7.setObjectName(_fromUtf8("ordenadaLbl_7"))
        self.ordenada_7 = QtGui.QLineEdit(self.calibrarBox_7)
        self.ordenada_7.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_7.setObjectName(_fromUtf8("ordenada_7"))
        self.tabWidget.addTab(self.canal7Tab, _fromUtf8(""))
        self.canal8Tab = QtGui.QWidget()
        self.canal8Tab.setObjectName(_fromUtf8("canal8Tab"))
        self.groupBox_8 = QtGui.QGroupBox(self.canal8Tab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 351, 111))
        self.groupBox_8.setCheckable(True)
        self.groupBox_8.setChecked(False)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.unidadLbl_8 = QtGui.QLabel(self.groupBox_8)
        self.unidadLbl_8.setGeometry(QtCore.QRect(0, 60, 56, 17))
        self.unidadLbl_8.setObjectName(_fromUtf8("unidadLbl_8"))
        self.unidad_8 = QtGui.QLineEdit(self.groupBox_8)
        self.unidad_8.setGeometry(QtCore.QRect(59, 55, 113, 27))
        self.unidad_8.setObjectName(_fromUtf8("unidad_8"))
        self.nombreLbl_8 = QtGui.QLabel(self.groupBox_8)
        self.nombreLbl_8.setGeometry(QtCore.QRect(0, 30, 56, 17))
        self.nombreLbl_8.setObjectName(_fromUtf8("nombreLbl_8"))
        self.nombre_8 = QtGui.QLineEdit(self.groupBox_8)
        self.nombre_8.setGeometry(QtCore.QRect(59, 25, 113, 27))
        self.nombre_8.setObjectName(_fromUtf8("nombre_8"))
        self.calibrarBox_8 = QtGui.QGroupBox(self.groupBox_8)
        self.calibrarBox_8.setGeometry(QtCore.QRect(190, 0, 161, 131))
        self.calibrarBox_8.setCheckable(True)
        self.calibrarBox_8.setChecked(False)
        self.calibrarBox_8.setObjectName(_fromUtf8("calibrarBox_8"))
        self.pendienteLbl_8 = QtGui.QLabel(self.calibrarBox_8)
        self.pendienteLbl_8.setGeometry(QtCore.QRect(0, 30, 61, 17))
        self.pendienteLbl_8.setObjectName(_fromUtf8("pendienteLbl_8"))
        self.pendiente_8 = QtGui.QLineEdit(self.calibrarBox_8)
        self.pendiente_8.setGeometry(QtCore.QRect(70, 24, 91, 27))
        self.pendiente_8.setObjectName(_fromUtf8("pendiente_8"))
        self.ordenadaLbl_8 = QtGui.QLabel(self.calibrarBox_8)
        self.ordenadaLbl_8.setGeometry(QtCore.QRect(0, 60, 61, 17))
        self.ordenadaLbl_8.setObjectName(_fromUtf8("ordenadaLbl_8"))
        self.ordenada_8 = QtGui.QLineEdit(self.calibrarBox_8)
        self.ordenada_8.setGeometry(QtCore.QRect(70, 54, 91, 27))
        self.ordenada_8.setObjectName(_fromUtf8("ordenada_8"))
        self.tabWidget.addTab(self.canal8Tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frecuenciaLbl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setBold(True)
        font.setWeight(75)
        self.frecuenciaLbl.setFont(font)
        self.frecuenciaLbl.setObjectName(_fromUtf8("frecuenciaLbl"))
        self.horizontalLayout.addWidget(self.frecuenciaLbl)
        self.frecuenciaSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.frecuenciaSpinBox.setDecimals(3)
        self.frecuenciaSpinBox.setMinimum(0.153)
        self.frecuenciaSpinBox.setMaximum(1000.0)
        self.frecuenciaSpinBox.setProperty("value", 10.0)
        self.frecuenciaSpinBox.setObjectName(_fromUtf8("frecuenciaSpinBox"))
        self.horizontalLayout.addWidget(self.frecuenciaSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setObjectName(_fromUtf8("menu_Archivo"))
        self.menu_Experimento = QtGui.QMenu(self.menubar)
        self.menu_Experimento.setObjectName(_fromUtf8("menu_Experimento"))
        self.menuA_yuda = QtGui.QMenu(self.menubar)
        self.menuA_yuda.setObjectName(_fromUtf8("menuA_yuda"))
        self.menu_Ventana = QtGui.QMenu(self.menubar)
        self.menu_Ventana.setObjectName(_fromUtf8("menu_Ventana"))
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Principal.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Principal)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Principal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMedir = QtGui.QAction(Principal)
        self.actionMedir.setObjectName(_fromUtf8("actionMedir"))
        self.actionSalir = QtGui.QAction(Principal)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionGuardar = QtGui.QAction(Principal)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionAyuda = QtGui.QAction(Principal)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.actionAcercaDe = QtGui.QAction(Principal)
        self.actionAcercaDe.setObjectName(_fromUtf8("actionAcercaDe"))
        self.menu_Archivo.addAction(self.actionGuardar)
        self.menu_Archivo.addAction(self.actionSalir)
        self.menu_Experimento.addAction(self.actionMedir)
        self.menuA_yuda.addAction(self.actionAyuda)
        self.menuA_yuda.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menu_Experimento.menuAction())
        self.menubar.addAction(self.menu_Ventana.menuAction())
        self.menubar.addAction(self.menuA_yuda.menuAction())
        self.toolBar.addAction(self.actionMedir)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(Principal)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(_translate("Principal", "LibreLab v0.01", None))
        self.groupBox_1.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_1.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_1.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_1.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_1.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_1.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal1Tab), _translate("Principal", "Canal 1", None))
        self.groupBox_2.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_2.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_2.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_2.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_2.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_2.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal2Tab), _translate("Principal", "Canal 2", None))
        self.groupBox_3.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_3.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_3.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_3.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_3.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_3.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal3Tab), _translate("Principal", "Canal 3", None))
        self.groupBox_4.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_4.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_4.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_4.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_4.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_4.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal4Tab), _translate("Principal", "Canal 4", None))
        self.groupBox_5.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_5.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_5.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_5.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_5.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_5.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal5Tab), _translate("Principal", "Canal 5", None))
        self.groupBox_6.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_6.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_6.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_6.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_6.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_6.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal6Tab), _translate("Principal", "Canal 6", None))
        self.groupBox_7.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_7.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_7.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_7.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_7.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_7.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal7Tab), _translate("Principal", "Canal 7", None))
        self.groupBox_8.setTitle(_translate("Principal", "Activar", None))
        self.unidadLbl_8.setText(_translate("Principal", "Unidad", None))
        self.nombreLbl_8.setText(_translate("Principal", "Nombre", None))
        self.calibrarBox_8.setTitle(_translate("Principal", "Calibrar", None))
        self.pendienteLbl_8.setText(_translate("Principal", "Pendiente", None))
        self.ordenadaLbl_8.setText(_translate("Principal", "Ordenada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canal8Tab), _translate("Principal", "Canal 8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Principal", "Analógico", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Principal", "Digital", None))
        self.frecuenciaLbl.setText(_translate("Principal", "Frecuencia (Hz)", None))
        self.menu_Archivo.setTitle(_translate("Principal", "&Archivo", None))
        self.menu_Experimento.setTitle(_translate("Principal", "&Experimento", None))
        self.menuA_yuda.setTitle(_translate("Principal", "Ay&uda", None))
        self.menu_Ventana.setTitle(_translate("Principal", "&Ventana", None))
        self.toolBar.setWindowTitle(_translate("Principal", "toolBar", None))
        self.actionMedir.setText(_translate("Principal", "&Medir", None))
        self.actionMedir.setToolTip(_translate("Principal", "Iniciar una medición", None))
        self.actionSalir.setText(_translate("Principal", "&Salir", None))
        self.actionSalir.setToolTip(_translate("Principal", "Abandona el programa", None))
        self.actionGuardar.setText(_translate("Principal", "&Guardar", None))
        self.actionGuardar.setToolTip(_translate("Principal", "Guardar los datos de la última medición", None))
        self.actionAyuda.setText(_translate("Principal", "&Ayuda", None))
        self.actionAyuda.setToolTip(_translate("Principal", "Ayuda sobre el uso del programa", None))
        self.actionAcercaDe.setText(_translate("Principal", "A&cerca de...", None))
        self.actionAcercaDe.setToolTip(_translate("Principal", "Información sobre el programa", None))
