#!/usr/bin/env python

"""
(C) Marek Kocinski
marekkoc 

v.03
As the previous version was not working, the file is updated to new version of libraries e.g. matplotlib.


Name history:
    1. mk_Viewer3D_ver1 - 2015
    2. mkViewer1-v02.py - 2016.06.10 (v.0.02)
    3. mkViewer1.py - 2025.04.12 (v.0.03)

Created: 2015
Updated: 2025.04.12 (v.0.03)

"""
import os
import sys
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons



class Viewer3D:

    def __init__(self, X, figName='', debug=True):
        """ """

        self.debug = debug
        self.image_name = figName.split(os.sep)[-1]

        zsize, ysize, xsize = X.shape
        self.slices,rows,cols = X.shape
        self.ind  = int(self.slices/2)

        self.val0 = int(self.slices/2)
        self.cmap = plt.cm.gray
        self.X = X

        self.fig = plt.figure(figsize=(12, 10))
        self.fig.suptitle(self.image_name, color='blue', fontsize=16)
       
        # Dodajemy więcej miejsca na dole
        plt.subplots_adjust(bottom=0.15)

        rows_cols = (3, 5) # wiresze, kolumny
        # Główny obraz zajmujący obszar 3x3 w siatce 4x4
        self.ax = plt.subplot2grid(rows_cols, (0, 1), colspan=3, rowspan=3)
        self.l = self.ax.imshow(self.X[self.val0,:,:], interpolation='nearest',cmap=self.cmap)
        plt.axis('off')
        self.ax.set_title('Current slice (dir 0) - slice %d'%self.val0)
        self.fig.colorbar(self.l, ax=self.ax)

        # Obrazy w ostatniej kolumnie
        self.a0 = plt.subplot2grid(rows_cols, (0, 4))
        self.i0 = self.a0.imshow(self.X.max(0),interpolation='nearest',cmap=self.cmap)
        plt.axis('off')
        self.a0.set_title('MIP (dir 0)')
        self.fig.colorbar(self.i0, ax=self.a0)

        self.a1 = plt.subplot2grid(rows_cols, (1, 4))
        self.i1 = self.a1.imshow(self.X.max(1), interpolation='nearest', cmap=self.cmap)
        plt.axis('off')
        self.a1.set_title('MIP (dir 1)')
        self.fig.colorbar(self.i1, ax=self.a1)

        self.a2 = plt.subplot2grid(rows_cols, (2, 4))
        self.i2 = self.a2.imshow(self.X.max(2), interpolation='nearest', cmap=self.cmap)
        plt.axis('off')
        self.a2.set_title('MIP (dir 2)')
        self.fig.colorbar(self.i2, ax=self.a2)

        # Kontrolki w dolnym wierszu
        self.axcolor = 'lightgoldenrodyellow'
        
        # Zmodyfikowana pozycja suwaka - wyżej od dołu
        slider_ax = self.fig.add_axes((0.2, 0.08, 0.6, 0.03), facecolor=self.axcolor)  # [left, bottom, width, height]

        self.samp = Slider(slider_ax, 'xpos', 0, int(self.slices-1), valinit=int(self.val0))
        self.samp.on_changed(self.__update__)        

        # Przyciski radio i reset
        rax = plt.subplot2grid(rows_cols, (0, 0), rowspan=2)
        self.radio = RadioButtons(rax, ('gray', 'jet', 'hot', 'copper', 'hot', 'hsv', 'winter', 'summer', 'spring', 'nipy_spectral', 'autumn'), active=0)
        self.radio.on_clicked(self.__colorfunc__)

        resetax =plt.subplot2grid(rows_cols, (2, 0))
        resetax.set_aspect(0.2)  # Zmniejsza wysokość przycisku
        self.button = Button(resetax, 'Reset', color=self.axcolor, hovercolor='0.975')        

        self.__update__(self.samp.val)
        self.button.on_clicked(self.__reset__)

        cid1 = self.fig.canvas.mpl_connect('button_press_event', self.__onclick__)
        cid2 = self.fig.canvas.mpl_connect('scroll_event', self.__onscroll__)
        cid3 = self.fig.canvas.mpl_connect('key_press_event', self.__toogle_images__)

        #self.fig.show()
        # Modyfikujemy tight_layout, aby uwzględnić dodatkowe miejsce na dole
        plt.tight_layout(rect=(0, 0.15, 1, 0.95))
        plt.show()


    def __update__(self,val):
        val = int(val)
        self.l.set_data(self.X[val,:,:])
        self.ax.set_title('Current slice (dir 0) - slice %d'%val)
        self.fig.canvas.draw_idle()

    def __colorfunc__(self,label):
        self.l.set_cmap(label)        
        self.i0.set_cmap(label)        
        self.i1.set_cmap(label)        
        self.i2.set_cmap(label)
        self.fig.canvas.draw_idle()


    def __onclick__(self,event):
        if event.inaxes == self.ax.axes:
            img = 'ax'
        elif event.inaxes == self.a0.axes :
            img = 'a0'
        elif event.inaxes == self.a1.axes:
            img = 'a1'
        elif event.inaxes == self.a2.axes:
            img = 'a2'
        else:
            return
        if self.debug: print( '%s, button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(img,
            event.button, event.x, event.y, event.xdata, event.ydata))

    def __onscroll__(self,event):
        #print event.button, event.step
        if event.button=='up':
            self.samp.set_val(int(self.samp.val+1))
        else:
            self.samp.set_val(int(self.samp.val-1))
        self.fig.canvas.draw_idle()

    def __reset__(self,event):
        self.samp.reset()
        self.fig.canvas.draw_idle()
        if self.debug: print('reset')



    def __toogle_images__(self,event):
        """ttoogle amont images displayed on ax2,ax3,ax4: (max,mean,std,min)"""
        if event.key == '1':
            s = ' MIP'
            if self.debug: print('pressd key:'+event.key + s)
            self.a0.set_title('%s (dir 0)'%(s))
            self.i0.set_data(self.X.max(0))
            
            self.a1.set_title('%s (dir 1)'%(s))
            self.i1.set_data(self.X.max(1))
            
            self.a2.set_title('%s (dir 2)'%(s))
            self.i2.set_data(self.X.max(2))
            
            self.fig.canvas.draw_idle()
        elif event.key == '2':
            s =' mean'
            if self.debug: print ('pressd key:'+event.key + s)
            self.a0.set_title('%s (dir 0)'%(s))
            self.i0.set_data(self.X.mean(0))
           
            self.a1.set_title('%s (dir 1)'%(s))
            self.i1.set_data(self.X.mean(1))
            
            self.a2.set_title('%s (dir 2)'%(s))
            self.i2.set_data(self.X.mean(2))

            self.fig.canvas.draw_idle()
        elif event.key == '3':
            s = ' std'
            if self.debug: print ('pressd key:'+event.key + s)
            self.a0.set_title('%s (dir 0)'%(s))
            self.i0.set_data(self.X.std(0))
            
            self.a1.set_title('%s (dir 1)'%(s))
            self.i1.set_data(self.X.std(1))
            
            self.a2.set_title('%s (dir 2)'%(s))
            self.i2.set_data(self.X.std(2))

            self.fig.canvas.draw_idle()
        elif event.key == '4':
            s = ' mIP'
            if self.debug: print ('pressd key:'+event.key + s)
            self.a0.set_title('%s (dir 0)'%(s))
            self.i0.set_data(self.X.min(0))
            
            self.a1.set_title('%s (dir 1)'%(s))
            self.i1.set_data(self.X.min(1))
            
            self.a2.set_title('%s (dir 2)'%(s))
            self.i2.set_data(self.X.min(2))
            
            self.fig.canvas.draw_idle()
        else: return


def main():
    if len(sys.argv)<2:
        print("Usage:\nVeiwer3D_ver1.1 fileToDispaly.npy")
        #pth = os.path.join('/', 'media', 'marek', 'p1ext4', 'work', '00', 'all_data')
        #data = np.load(os.path.join(pth, 'normal01.npy'))
        file = os.path.join("data", "tofGRAY.npy")
        data = np.load(file)
        print("*** Loaded...default image ***")

    else:
        file, ext = os.path.splitext(sys.argv[1])
        if ext == ".raw":
            if len(sys.argv)<4:
                print("*** Zla liczba parametrow! ***\n\n*** Usage:\n*** Veiwer3D_ver1.1 fileToDispaly.raw size dtype")
                return
            else:
                data = np.fromfile(sys.argv[1] ,dtype=str(sys.argv[3]))
                res = int(sys.argv[2])
                data.shape = res,res,res
        elif ext == ".npy" and os.path.exists(sys.argv[1]):
            data = np.load(sys.argv[1])
        elif ext == ".nii" or ext == ".nii.gz":
            data = nib.load(sys.argv[1]).get_fdata()
            data = data.reshape(data.shape, order='C')
        else:
            print('\n*** Cos nie tak:\n-nieobslugiwany format plikow,\n-plik o podanej nazwie nieistenieje,\n-zla liczba parametrow ***\n')
            return

    print(data.shape, type(data))
    Viewer3D(data, file )


#############################################
############ STAND ALONE PROGRAM ############
#############################################

if __name__ == '__main__':

    main()
#else:
#    print 'Class Viewer3D imported successfully from Viewer3D_ver1.1.py'
