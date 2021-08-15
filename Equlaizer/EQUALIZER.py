#libraries
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
from Pop_up_methods import Pop_up_methods




class Equalizer(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(Equalizer, self).setupUi(MainWindow)
        
        #data and flags
        self.sliders=[self.slider1,self.slider2,self.slider3,self.slider4,self.slider5,self.slider6,self.slider7,self.slider8,self.slider9,self.slider10]
        self.sliders_funcs=[lambda:self.slider_update(0),lambda:self.slider_update(1),lambda:self.slider_update(2),lambda:self.slider_update(3),
                            lambda:self.slider_update(4),lambda:self.slider_update(5),lambda:self.slider_update(6),lambda:self.slider_update(7),
                            lambda:self.slider_update(8),lambda:self.slider_update(9)]
        self.sliders_data=[1 for i in range(len(self.sliders))]
        self.slic_freq = [100,1000,2000,4000, 5000, 8000, 10000, 12000, 14000, 16000, 20000]
        self.signals_plot_flag=False
        self.file_flag=False
        self.sound_flag=False
        self.freq_labels=[self.freq1,self.freq2,self.freq3,self.freq4,self.freq5,self.freq6,self.freq7,self.freq8,self.freq9,self.freq10]
        for i in range(len(self.freq_labels)):
            self.freq_labels[i].setText(str(self.slic_freq[i+1])+"Hz")    
        self.sliders_labels=[self.slider_label5,self.slider_label4,self.slider_label3,self.slider_label2,self.slider_label1]
        self.slider_ranges={"min":-3,"max":3,"step":1,"value":1}
        self.results_data=[]
        self.audio_freqs=[]
        self.audio=[]
        self.audio_DFT=[]
        self.time=[]
        self.equalizer_data=[]
        self.inverse_equalizer_data=[]
        self.window = QtWidgets.QMainWindow()
        self.ui = Pop_up_methods(self.window)
        #connect buttons
        for i in range(len(self.sliders)):
            self.sliders[i].setMaximum(self.slider_ranges["max"])
            self.sliders[i].setMinimum(self.slider_ranges["min"])
            self.sliders[i].setValue(self.slider_ranges["value"])
            self.sliders[i].setSingleStep(self.slider_ranges["step"])
            self.sliders[i].valueChanged.connect(self.sliders_funcs[i])
        for i in range(len(self.sliders_labels)):
            self.sliders_labels[i].setText(str(int(((self.slider_ranges["max"]-self.slider_ranges["min"])/len(self.sliders_labels)) * i)))
        self.play_button_home.clicked.connect(lambda:self.play_sound(self.sound_flag))
        self.Open.triggered.connect(self.open_file)
        self.play_button_signals.clicked.connect(self.ploting_signals)
        self.reset_button_home.clicked.connect(self.reset)
        self.save_result_button.clicked.connect(self.saving_results)
        self.show_result_button.clicked.connect(self.pop_up)
        self.ui.edit_difference1.clicked.connect(lambda:self.get_data(0))
        self.ui.edit_difference2.clicked.connect(lambda:self.get_data(1))
        self.Save.triggered.connect(self.saving_files)
        
        #timer
        # self.timer=QtCore.QTimer()
        # self.timer.setInterval(50)
        # self.timer.timeout.connect(self.update_home)


#  pop_up
    def pop_up(self):

        self.window.show()

#sliders
    def slider_update(self,i):   
        if self.file_flag:
            print(self.sliders[i].value())
            if (self.sliders[i].value()<0):
                if(self.sliders[i].value == -1):
                    self.sliders == 0.8
                else:
                    self.slider_val = 1 / np.abs(self.sliders[i].value())
            else:
                self.slider_val = self.sliders[i].value()
            
            if(self.sliders_data[i] != 0):
                new_gain = (self.slider_val/self.sliders_data[i])
                print(new_gain)
                self.Old_data = self.equalizer_data
            else: 
                new_gain = (self.slider_val)
                self.Old_data = self.audio_DFT

            min_range = int(self.slic_freq[i] / self.step)
            max_range = int(self.slic_freq[i+1] / self.step)
            print('min', min_range)
            if max_range>len(self.audio_DFT):
                max_range=len(self.audio_DFT) 
            if (str(self.comboBox.currentText())) != "Rectangle":
                if (str(self.comboBox.currentText())) == "Hanning":
                    spectrum_list = np.hanning((max_range - min_range)*2)
                elif (str(self.comboBox.currentText())) == "Hamming":
                    spectrum_list = np.hamming((max_range - min_range)*2)
                self.multi_list=spectrum_list[int(1/4*len(spectrum_list)):int(3/4 * len(spectrum_list) )]
                self.leftBand = spectrum_list[0: int(1/4*len(spectrum_list))]
                self.rightBand = spectrum_list[int(3/4 * len(spectrum_list)) : len(spectrum_list)]
                if i is not 0:
                    print('spec', len(spectrum_list))
                    print(min_range-int(1/4*len(spectrum_list)))
                    print('old', len(self.Old_data))
                    print('gain',new_gain)
                    self.equalizer_data[min_range-int(1/4*len(spectrum_list)) : min_range] += np.multiply(new_gain*(self.leftBand), self.Old_data[min_range-int(1/4*len(spectrum_list)) : min_range])
                if i is not 9:
                    self.equalizer_data[max_range : max_range + len(spectrum_list) - int(3/4*len(spectrum_list))] += np.multiply((new_gain*self.rightBand), self.Old_data[max_range : max_range + len(spectrum_list) - int(3/4*len(spectrum_list))])
            else:
                self.multi_list = np.asarray([1 for i in range(max_range - min_range)])
            self.equalizer_data[min_range:max_range]= np.multiply((new_gain)*(self.multi_list), self.Old_data[min_range:max_range])
            self.inverse_equalizer_data=fftpack.irfft(self.equalizer_data)
            self.play_sound()
            self.update_home()
            self.update_signals_data()
            self.sliders_data[i]=self.slider_val
            
            
#opening files
    def open_file(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', "D:\\DSP\\Dsp_task2","WAV (*.wav)")
        if fname[0]:
            self.file_flag=True
            self.rate,self.audio = wavfile.read(fname[0])
            if type(self.audio[0])==np.ndarray:
                self.data_type=type(self.audio[0][0])
                self.audio=self.audio[:,0]
            else:
                self.data_type=type(self.audio[0])
                  
            self.inverse_equalizer_data=[]
            self.time = self.get_Time(self.audio,self.rate)
            self.audio_DFT = fftpack.rfft(self.audio)
            self.audio_freqs = np.linspace(self.slic_freq[0],self.slic_freq[-1], len(self.audio_DFT))
            self.step=self.audio_freqs[1]-self.audio_freqs[0]
            self.equalizer_data=self.audio_DFT.copy()
            self.inverse_equalizer_data=fftpack.irfft(self.equalizer_data)
            #reset the plot
            # self.timer.stop()
            
            self.equalizer_plot.plotItem.clear()
            self.reset()
            self.plot_home()

#reset
    def reset(self):
        for i in range(len(self.sliders)):
            self.sliders[i].setValue(1)
            self.sliders_data[i]=1
        if self.file_flag:
            self.equalizer_data=self.audio_DFT.copy()
        
#ploting signals
    def ploting_signals(self):
        if self.file_flag:
            self.signals_plot_flag= not self.signals_plot_flag
            if self.signals_plot_flag:
                self.update_signals_data()
                for i in range(len(self.signals_widgets)):
                    self.signals_widgets[i].plotItem.plot(self.signals_x_axis[i],self.signals_y_axis[i])
            else:
                for i in self.signals_widgets:
                    i.plotItem.clear()


#get data from pop_up window
    def get_data(self,i):
        self.equalizer_data=self.ui.return_data(i)
        self.update_home()
        for slider in self.sliders:
            slider.setValue(1)


#play
    def play_sound(self,S_flag= True):
        if self.file_flag:
            self.sound_flag = not self.sound_flag
            S_flag= not S_flag
            if S_flag:
                sd.play(self.inverse_equalizer_data.astype(self.data_type))
            else:   
                sd.stop()    
                         
#update_signals_data
    def update_signals_data(self):
        self.signals_widgets=[self.input_fourier_plot,self.input_time_plot,self.output_time_plot,self.output_fourier_plot]
        self.signals_x_axis=[self.audio_freqs,self.time,self.time,self.audio_freqs]
        self.signals_y_axis=[np.abs(self.audio_DFT)/len(self.audio_DFT),self.audio/len(self.audio),self.inverse_equalizer_data,np.abs(self.equalizer_data)/len(self.equalizer_data)]

#ploting the equalizer
    def plot_home(self):
        if self.file_flag:
            # self.timer.start()
            self.data_line=self.equalizer_plot.plotItem.plot(self.audio_freqs,np.abs(self.audio_DFT)/len(self.audio))

    def update_home(self):
        self.data_line.setData(self.audio_freqs,np.abs(self.equalizer_data/len(self.equalizer_data)))    
#saving results
    def saving_results(self):
        self.ui.add_signal(np.abs(self.equalizer_data),self.rate,self.data_type)
#x-axis of audio file
    def get_Time(self,data,rate):
        '''
        get the time of the audio 

        Parameters:
            data: numpy array
               data of the recored
            rate: int  
                the smaple rate of the wav file

        Returns:
            f: ndarray
                Array of length n containing the time of audio
        '''
        length = data.shape[0]
        ArrayOfLength = np.arange(length)
        time = ArrayOfLength / rate
        return time


    def saving_files(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File',".wav")
        name = path[0]
        if name:
            name = name+ ".wav"

            wavfile.write(name,self.rate,self.inverse_equalizer_data)        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Equalizer(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())