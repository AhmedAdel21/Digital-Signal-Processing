from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from numpy import loadtxt
import numpy as np
import pandas as pd
import pyqtgraph as pg
from GUI_TABS import *
import scipy.io as sio
from scipy.io import wavfile
from scipy import fftpack
import sounddevice as sd
from Pop_up import Pop_up


class Pop_up_methods(Pop_up):
    def __init__ (self, MainWindow):
        super(Pop_up_methods, self).setupUi(MainWindow)
        self.result_widgets=[self.differece1_plot,self.differece2_plot]
        self.add_counter = 0
        self.compare_sig = dict()
        self.widgets=[self.differece1_plot,self.differece2_plot]
        self.combo_boxs=[self.difference1_combobox,self.difference2_combobox]
        self.rates=[]
        self.types=[]

        #connecting buttons
        self.combo_boxs[0].currentTextChanged.connect(lambda:self.plot_signal(0))
        self.combo_boxs[1].currentIndexChanged.connect(lambda:self.plot_signal(1)) 
        self.reset_difference1.clicked.connect(self.reset)
        self.reset_difference2.clicked.connect(self.reset)
        self.save_difference1_2.clicked.connect(lambda:self.save(0))
        self.save_difference2.clicked.connect(lambda:self.save(1))
    def add_signal(self, data,Rate,Type):
        if self.add_counter is 9:
            print('max signal')
        else:
            self.compare_sig.update({'Signal'+str(self.add_counter+1):data})
            self.combo_boxs[0].addItem("Signal"+str(self.add_counter+1))
            self.combo_boxs[1].addItem("Signal"+str(self.add_counter+1))
            self.rates.append(Rate)
            self.types.append(Type)
            self.add_counter += 1
    def plot_signal(self,i):
        if str(self.combo_boxs[i].currentText()) != "":
         self.widgets[i].plotItem.clear()
         self.widgets[i].plotItem.plot(self.compare_sig[str(self.combo_boxs[i].currentText())])

    def return_data(self,i):
        return self.compare_sig[str(self.combo_boxs[i].currentText())]

    def reset(self,i):

        text=str(self.combo_boxs[i].currentText())
        for i in range(2):
            if str(self.combo_boxs[i].currentText()) == text:
                self.widgets[i].plotItem.clear()
            self.combo_boxs[i].removeItem(self.combo_boxs[i].findText(text))    
        del self.compare_sig[text]  

    def save(self,i):
        data=fftpack.irfft(self.compare_sig[str(self.combo_boxs[i].currentText())])
        index=int(str(self.combo_boxs[i].currentText())[-1])-1
        name = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File',".wav")
        path = name[0]
        if path:
            path = path + ".wav"
            wavfile.write(path,self.rates[index],data.astype(self.types[index]))     