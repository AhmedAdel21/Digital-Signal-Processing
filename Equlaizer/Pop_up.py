# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Pop_up(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_15 = QtWidgets.QFrame(self.centralwidget)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.differece1_plot = PlotWidget(self.frame_15)
        self.differece1_plot.setMinimumSize(QtCore.QSize(0, 200))
        self.differece1_plot.setObjectName("differece1_plot")
        self.verticalLayout.addWidget(self.differece1_plot)
        self.frame_7 = QtWidgets.QFrame(self.frame_15)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save_difference1 = QtWidgets.QFrame(self.frame_7)
        self.save_difference1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.save_difference1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.save_difference1.setObjectName("save_difference1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.save_difference1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.save_difference1_2 = QtWidgets.QPushButton(self.save_difference1)
        self.save_difference1_2.setObjectName("save_difference1_2")
        self.gridLayout_4.addWidget(self.save_difference1_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.save_difference1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reset_difference1 = QtWidgets.QPushButton(self.frame)
        self.reset_difference1.setObjectName("reset_difference1")
        self.gridLayout_3.addWidget(self.reset_difference1, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.frame_22 = QtWidgets.QFrame(self.frame_7)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edit_difference1 = QtWidgets.QPushButton(self.frame_22)
        self.edit_difference1.setObjectName("edit_difference1")
        self.gridLayout_2.addWidget(self.edit_difference1, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_22)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.frame_16 = QtWidgets.QFrame(self.frame_7)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.difference1_combobox = QtWidgets.QComboBox(self.frame_16)
        self.difference1_combobox.setObjectName("difference1_combobox")
        self.gridLayout_18.addWidget(self.difference1_combobox, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_16)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_7)
        self.line_2 = QtWidgets.QFrame(self.frame_15)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.differece2_plot = PlotWidget(self.frame_17)
        self.differece2_plot.setMinimumSize(QtCore.QSize(0, 200))
        self.differece2_plot.setObjectName("differece2_plot")
        self.verticalLayout_4.addWidget(self.differece2_plot)
        self.frame_9 = QtWidgets.QFrame(self.frame_17)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.frame_4 = QtWidgets.QFrame(self.frame_9)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.save_difference2 = QtWidgets.QPushButton(self.frame_4)
        self.save_difference2.setObjectName("save_difference2")
        self.gridLayout_14.addWidget(self.save_difference2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_4)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.frame_5 = QtWidgets.QFrame(self.frame_9)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.reset_difference2 = QtWidgets.QPushButton(self.frame_5)
        self.reset_difference2.setObjectName("reset_difference2")
        self.gridLayout_15.addWidget(self.reset_difference2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_5)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.frame_24 = QtWidgets.QFrame(self.frame_9)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.edit_difference2 = QtWidgets.QPushButton(self.frame_24)
        self.edit_difference2.setObjectName("edit_difference2")
        self.gridLayout_16.addWidget(self.edit_difference2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_24)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.frame_19 = QtWidgets.QFrame(self.frame_9)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.difference2_combobox = QtWidgets.QComboBox(self.frame_19)
        self.difference2_combobox.setObjectName("difference2_combobox")
        self.gridLayout_20.addWidget(self.difference2_combobox, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_19)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.gridLayout_13.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.line_4 = QtWidgets.QFrame(self.frame_17)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.gridLayout_12.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_17)
        self.gridLayout_22.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
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
        self.save_difference1_2.setText(_translate("MainWindow", "Save"))
        self.reset_difference1.setText(_translate("MainWindow", "Reset"))
        self.edit_difference1.setText(_translate("MainWindow", "Edit"))
        self.save_difference2.setText(_translate("MainWindow", "Save"))
        self.reset_difference2.setText(_translate("MainWindow", "Reset"))
        self.edit_difference2.setText(_translate("MainWindow", "Edit"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
