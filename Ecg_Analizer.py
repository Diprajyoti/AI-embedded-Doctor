import serial
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd
import numpy as np
from tkinter import messagebox
from tensorflow.keras.models import load_model

class ECG():
    def __init__(self,Speed,Age,Sex,Medicine,Name):
        self.Speed=Speed

        self.Age = Age

        self.Sex = Sex

        self.Medicine = Medicine

        self.Name = Name

    def ecgserial(self):
        ecgdata=[]
        try:
             arduinodata= serial.Serial('COM3',9600)
        except:
             messagebox.showerror("From Dr.AI","Please connect the USB device first !")
        
        plt.ion()
        plt.show()
        i=0
        try:
            while i<700 :
                while (arduinodata.inWaiting()==0):
                    pass
                arduinoString= arduinodata.readline()
                Data= arduinoString.decode()
                ecg = int(Data)
                ecgdata.append(ecg)
                plt.cla()
                plt.plot(ecgdata)
                plt.pause(.000001)
                i=i+1
            arduinodata.close()
            ecgdata=np.array(ecgdata)
            self.ecgdata=ecgdata
               
            peaks=find_peaks(self.ecgdata,1,1,1)
            x= np.array([i for i in range(0,700)])
            height = peaks[1]['peak_heights']
            peak_pos = x[peaks[0]]
    
    
            df = pd.DataFrame(list(zip(height,peak_pos)),columns=['height','peak_pos'])
            R_wave=float(np.amax(height))
            r_wave= ((2.30/1023)*R_wave)
            self.Amplitude = r_wave
            print(self.Amplitude)
            max_heights= []
            for i in height:
                if(i>450):
                    max_heights.append(i)
    
            mx_height_pos=[]
            for i in max_heights:
                mx_height_pos.append(float(df.loc[df['height']==i,'peak_pos']))
    
            intervals=[]
            for i in range(0,len(mx_height_pos)-1):
                intervals.append(mx_height_pos[i+1]-mx_height_pos[i])
            RR_interval=np.average(intervals)/1000
            self.RR_interval=RR_interval
            print(self.RR_interval)
            messagebox.showinfo("From Dr.AI","Your ECG Data has been captured successfully.")
        except :
            messagebox.showwarning("From Dr. AI","NOISE DETECTED !!! \n 1. remove the charger.\n 2. Capture again.")
        




    def predict(self):


        model=load_model(r'C:\Users\DIPRAJYOTI MAJUMDAR\Desktop\AI embedded doctor\Ecg_analyse_model2.h5')
        self.Amplitude=float('{0:.3f}'.format(self.Amplitude))
        print(self.Amplitude)
        self.RR_interval=float('{0:.3f}'.format(self.RR_interval))
        print(self.RR_interval)
        result= model.predict([[self.Amplitude,self.RR_interval,self.Speed,self.Age,self.Sex,self.Medicine]])[0][0]*100

        result= float('{0:.2f}'.format(result))
        print(result)
        return result

















