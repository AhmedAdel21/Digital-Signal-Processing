from jpeg import *
import sys
from PIL import Image
from io import BytesIO
import io
import os

class ApplicationWindow(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(ApplicationWindow, self).setupUi(MainWindow)
        self.imageLabels = [self.label_1,self.label_2,self.label_3,self.label_4,self.label_5,
                            self.label_6,self.label_7,self.label_8,self.label_9,self.label_10]
        self.openImage.triggered.connect(self.open)

    def open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', "D:\Sys & Bio\Sys & Bio 3rd year\2nd Semester\DSP\assignments\task_3\First Version") #,"WAV (*.wav)"
        self.imageAdd = fname[0]
        if self.imageAdd:
            imageFile = open(self.imageAdd,'rb')
            imageDataOriginal = imageFile.read()
            imageData = imageFile.read()
            sos = b'\xff\xda'
            i = 0
            imageStart =0
            while True:
                if i ==5:
                    break
                imageStart += 1+imageData.find(sos)
                imageFile.seek(imageStart+1)
                imageData = imageFile.read()
                i += 1
            imageDataSegment = int(len(imageData)/9)
            for i in range(10):
                data  = imageDataOriginal[0:imageStart+(imageDataSegment*i)] + b'\xff\xd9'
                stream = BytesIO(bytearray(data))
                image = Image.open(stream)
                imageNewAdd = str("image/"+str(os.path.splitext(os.path.basename(self.imageAdd))[0])+str(i)+str(os.path.splitext(self.imageAdd)[1]))
                imageSave =image.save(imageNewAdd)
                stream.close()
                imageShow = QtGui.QImage(imageNewAdd).scaled(self.label_1.width(),self.label_1.height())
                self.imageLabels[i].setPixmap(QtGui.QPixmap.fromImage(imageShow))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ApplicationWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())