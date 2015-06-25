import csv
import math
import glob
import matplotlib.pyplot as plt
import copy

class Reading:
    def __init__(self, row, header):
        self.time = float(row[header.index('Time')])
        try:
            self.longitude = float(row[header.index(' Longitude')])
        except ValueError:
            pass

        try:
            self.latitude = float(row[header.index(' Latitude')])
        except ValueError:
            pass
        
        try:
            self.accx = float(row[header.index(' Accx')])
        except ValueError:
            pass

        try:
            self.accy = float(row[header.index(' Accy')])
        except ValueError:
            pass
        try:
            self.accz = float(row[header.index(' Accz')])
        except ValueError:
            pass
        try:
            self.magx = float(row[header.index(' Magx')])
        except ValueError:
            pass
        try:
            self.magy = float(row[header.index(' Magy')])
        except ValueError:
            pass
        try:
            self.magz = float(row[header.index(' Magz')])
        except ValueError:
            pass
        try:
            self.gyrox = float(row[header.index(' Gyrox')])
        except ValueError:
            pass
        try:
            self.gyroy = float(row[header.index(' Gyroy')])
        except ValueError:
            pass
        try:
            self.gyroz = float(row[header.index(' Gyroz')])
        except ValueError:
            pass
        
    def __str__(self):
        return str(self.time) + ' '+str(self.longitude)+' '+str(self.latitude)

        
class Event:
    avgX=0.0
    avgY=0.0
    avgZ=0.0
    classtype=''
    
    def __init__(self, classtype='Unknown'):
        self.classtype=classtype;
        self.data = []
        self.avgX=0.0
        self.avgY=0.0
        self.avgZ=0.0
        self.sdz=0.0
        self.sdy=0.0
        self.sdx=0.0
        
    def insert_reading(self, read):
        self.data.append(copy.deepcopy(read))
        self.time = read.time;
    
    def getClass(self):
        return self.classtype
    
    def MagaverageX(self):
        sum=0
        for i in self.data:
            sum+=i.magx
        self.magavgX=sum/float(len(self.data))
        return self.magavgX
    
    def MagaverageY(self):
        sum=0
        for i in self.data:
            sum+=i.magy
        self.magavgY=sum/float(len(self.data))
        return self.magavgY

    def MagaverageZ(self):
        sum=0
        for i in self.data:
            sum+=i.magz
        self.magavgZ=sum/float(len(self.data))
        return self.magavgZ
    
    def MagsdX(self):
        sum=0.0
        if self.magavgX==0.0:
            self.MagaverageX()
        for i in self.data:
            sum=sum+(i.magx-self.magavgX) ** 2
        self.magsdx=math.sqrt(sum/float(len(self.data)))
        return self.magsdx

    def MagsdY(self):
        sum=0.0
        if self.magavgY==0.0:
            self.MagaverageY()
        for i in self.data:
            sum=sum+(i.magy-self.avgY) ** 2
        self.magsdy=math.sqrt(sum/float(len(self.data)))
        return self.magsdy
    
    def MagsdZ(self):
        sum=0.0
        if self.magavgZ==0.0:
            self.MagaverageZ()
        for i in self.data:
            sum=sum+(i.magz-self.magavgZ) ** 2
        self.magsdz=math.sqrt(sum/float(len(self.data)))
        return self.magsdz
    
    def AccaverageX(self):
        sum=0
        for i in self.data:
            sum+=i.accx
        self.accavgX=sum/float(len(self.data))
        return self.accavgX
    
    def AccaverageY(self):
        sum=0
        for i in self.data:
            sum+=i.accy
        self.accavgY=sum/float(len(self.data))
        return self.accavgY

    def AccaverageZ(self):
        sum=0
        for i in self.data:
            sum+=i.accz
        self.accavgZ=sum/float(len(self.data))
        return self.accavgZ
    
    def AccsdX(self):
        sum=0.0
        if self.accavgX==0.0:
            self.AccaverageX()
        for i in self.data:
            sum=sum+(i.accx-self.accavgX) ** 2
        self.accsdx=math.sqrt(sum/float(len(self.data)))
        return self.accsdx

    def AccsdY(self):
        sum=0.0
        if self.accavgY==0.0:
            self.AccaverageY()
        for i in self.data:
            sum=sum+(i.accy-self.avgY) ** 2
        self.accsdy=math.sqrt(sum/float(len(self.data)))
        return self.accsdy
    
    def AccsdZ(self):
        sum=0.0
        if self.accavgZ==0.0:
            self.AccaverageZ()
        for i in self.data:
            sum=sum+(i.accz-self.accavgZ) ** 2
        self.accsdz=math.sqrt(sum/float(len(self.data)))
        return self.accsdz

    def GyroaverageX(self):
        sum=0
        for i in self.data:
            sum+=i.gyrox
        self.gyroavgX=sum/float(len(self.data))
        return self.gyroavgX
    
    def GyroaverageY(self):
        sum=0
        for i in self.data:
            sum+=i.gyroy
        self.gyroavgY=sum/float(len(self.data))
        return self.gyroavgY

    def GyroaverageZ(self):
        sum=0
        for i in self.data:
            sum+=i.gyroz
        self.gyroavgZ=sum/float(len(self.data))
        return self.gyroavgZ
    
    def GyrosdX(self):
        sum=0.0
        if self.gyroavgX==0.0:
            self.GyroaverageX()
        for i in self.data:
            sum=sum+(i.gyrox-self.gyroavgX) ** 2
        self.gyrosdx=math.sqrt(sum/float(len(self.data)))
        return self.gyrosdx

    def GyrosdY(self):
        sum=0.0
        if self.gyroavgY==0.0:
            self.GyroaverageY()
        for i in self.data:
            sum=sum+(i.gyroy-self.avgY) ** 2
        self.gyrosdy=math.sqrt(sum/float(len(self.data)))
        return self.gyrosdy
    
    def GyrosdZ(self):
        sum=0.0
        if self.gyroavgZ==0.0:
            self.GyroaverageZ()
        for i in self.data:
            sum=sum+(i.gyroz-self.gyroavgZ) ** 2
        self.gyrosdz=math.sqrt(sum/float(len(self.data)))
        return self.gyrosdz
    
    def number_readings(self):
        return len(self.data)
    
    def objectprint(self):
        print self.averageY()
        print self.sdY()
        print self.classtype
