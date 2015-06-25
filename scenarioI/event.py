import csv
import math
import glob
import matplotlib.pyplot as plt
import copy

class Reading:
    def __init__(self, row):
        self.time = float(row[0])
        self.magx = float(row[1])
        self.magy = float(row[2])
        self.magz = float(row[3])

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

        
    def __del__(self):
         self.data=[]
         self.avgX=0.0
         self.avgY=0.0
         self.avgZ=0.0
         self.sdz=0.0
         self.sdy=0.0
         self.sdx=0.0
        
    def insert_reading(self, read):
        self.data.append(copy.deepcopy(read))

    def getClass(self):
        return self.classtype
    
    def averageX(self):
        sum=0
        for i in self.data:
            sum+=i.magx
        self.avgX=sum/float(len(self.data))
        return self.avgX
    
    def averageY(self):
        sum=0
        for i in self.data:
            sum+=i.magy
        self.avgY=sum/float(len(self.data))
        return self.avgY

    def averageZ(self):
        sum=0
        for i in self.data:
            sum+=i.magz
        self.avgZ=sum/float(len(self.data))
        return self.avgZ
    
    def sdX(self):
        sum=0.0
        if self.avgX==0.0:
            self.averageX()
        for i in self.data:
            sum=sum+(i.magx-self.avgX) ** 2
        self.sdx=math.sqrt(sum/float(len(self.data)))
        return self.sdx

    def sdY(self):
        sum=0.0
        if self.avgY==0.0:
            self.averageY()
        for i in self.data:
            #sum=(i.magx-self.avgY) ** 2 # It is works! the original
            #sum=sum+(i.magx-self.avgX) ** 2 # It is works! the best
            sum=sum+(i.magy-self.avgY) ** 2
        self.sdy=math.sqrt(sum/float(len(self.data)))
        return self.sdy
    
    def sdZ(self):
        sum=0.0
        if self.avgZ==0.0:
            self.averageZ()
        for i in self.data:
            sum=sum+(i.magz-self.avgZ) ** 2
        self.sdz=math.sqrt(sum/float(len(self.data)))
        return self.sdz
    
    def number_readings(self):
        return len(self.data)
    
    def objectprint(self):
        print self.averageY()
        print self.sdY()
        print self.classtype
