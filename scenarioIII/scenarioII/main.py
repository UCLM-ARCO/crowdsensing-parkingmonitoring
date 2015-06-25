#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-
import csv
import math
import glob
import matplotlib.pyplot as plt
import re
import copy
import getopt

#Civitas Cartrack module
from event import *
from svm import *

VENTANA = 7

left12mOn = "2015-05-09-18-56+0200-.scv"
left12mOff = "2015-05-09-18-57+0200-.scv"
left10mOn = "2015-05-09-18-59+0200-.scv"
left10mOff= "2015-05-09-18-59+0200-2.scv"
left7mOn = "2015-05-09-19-01+0200-.scv"
left7mOff= "2015-05-09-19-03+0200-.scv"
left5mOn = "2015-05-09-19-04+0200-.scv"
left5mOff = "2015-05-09-19-05+0200-.scv"
left2mOn = "2015-05-09-19-06+0200-.scv"
left2mOff = "2015-05-09-19-07+0200-.scv"
left0mOn= "2015-05-09-19-09+0200-.scv"
left0mOff= "2015-05-09-19-10+0200-.scv"


datalistfiles = glob.glob("./data/*")

dataclassnames=["left0mOn","left0mOff","left2mOn","left2mOff","left5mOn","left5mOff","left7mOn","left7mOff","left10mOn","left10mOff","left12mOn","left12mOff"]
datalistfiles2=[left0mOn,left0mOff,left2mOn,left2mOff,left5mOn,left5mOff,left7mOn,left7mOff,left10mOn,left10mOff,left12mOn,left12mOff]

print datalistfiles2

ContainerEvent = []

def populate_vector(datalistfiles):
    global ContainerEvent
    indexEvent=0
    indexFile = 0
    for i in datalistfiles:
        i="data/"+i
        with open(i, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            index=0
            ProcessingEvent=Event(dataclassnames[indexFile])
            for row in spamreader:
                if (index==0): # first line is the header
                    index=index+1
                    header = row
                    continue
                index=index+1
                x=Reading(row, header)
                ProcessingEvent.insert_reading(copy.deepcopy(x))
                if (index%VENTANA!=0):
                    continue
                ContainerEvent.append(copy.deepcopy(ProcessingEvent))
                indexEvent=indexEvent+1;
                #ProcessingEvent.reset()
                ProcessingEvent=Event(dataclassnames[indexFile])
            indexFile=indexFile+1
            
def paint(ContainerEvent):
    indexEvent = 0
    Xleft12mOn = []
    Xleft12mOff = []
    Xleft10mOn = []
    Xleft10mOff= []
    Xleft7mOn = []
    Xleft7mOff= []
    Xleft5mOn = []
    Xleft5mOff = []
    Xleft2mOn = []
    Xleft2mOff = []
    Xleft0mOn= []
    Xleft0mOff= []
    Yleft12mOn = []
    Yleft12mOff = []
    Yleft10mOn = []
    Yleft10mOff= []
    Yleft7mOn = []
    Yleft7mOff= []
    Yleft5mOn = []
    Yleft5mOff = []
    Yleft2mOn = []
    Yleft2mOff = []
    Yleft0mOn= []
    Yleft0mOff= []



    # for i in ContainerEvent:
    #     print i.classtype
    #     if i.classtype == 'left0mOn':
    #         Xleft0mOn.append(i.MagaverageX())
    #         Yleft0mOn.append(i.MagsdX())

    #     if i.classtype == 'left2mOn':
    #         Xleft2mOn.append(i.MagaverageX())
    #         Yleft2mOn.append(i.MagsdX())     
 
    #     if i.classtype == 'left5mOn':
    #         Xleft5mOn.append(i.MagaverageX())
    #         Yleft5mOn.append(i.MagsdX())
            
    #     if i.classtype == 'left7mOn':
    #         Xleft7mOn.append(i.MagaverageX())
    #         Yleft7mOn.append(i.MagsdX())
            
    #     if i.classtype == 'left10mOn':
    #         Xleft10mOn.append(i.MagaverageX())
    #         Yleft10mOn.append(i.MagsdX())
            
    #     if i.classtype == 'left12mOn':
    #         Xleft12mOn.append(i.MagaverageX())
    #         Yleft12mOn.append(i.MagsdX())
            
    for i in ContainerEvent:
        print i.classtype
        if i.classtype == 'left0mOn':
            Xleft0mOn.append(i.MagaverageX())
            Yleft0mOn.append(0)

        if i.classtype == 'left2mOn':
            Xleft2mOn.append(i.MagaverageX())
            Yleft2mOn.append(2)     
 
        if i.classtype == 'left5mOn':
            Xleft5mOn.append(i.MagaverageX())
            Yleft5mOn.append(5)
            
        if i.classtype == 'left7mOn':
            Xleft7mOn.append(i.MagaverageX())
            Yleft7mOn.append(7)
            
        if i.classtype == 'left10mOn':
            Xleft10mOn.append(i.MagaverageX())
            Yleft10mOn.append(10)
            
        if i.classtype == 'left12mOn':
            Xleft12mOn.append(i.MagaverageX())
            Yleft12mOn.append(12)

        if i.classtype == 'left0mOff':
            Xleft0mOff.append(i.MagaverageX())
            Yleft0mOff.append(0)

        if i.classtype == 'left2mOff':
            Xleft2mOff.append(i.MagaverageX())
            Yleft2mOff.append(2)     
 
        if i.classtype == 'left5mOff':
            Xleft5mOff.append(i.MagaverageX())
            Yleft5mOff.append(5)
            
        if i.classtype == 'left7mOff':
            Xleft7mOff.append(i.MagaverageX())
            Yleft7mOff.append(7)
            
        if i.classtype == 'left10mOff':
            Xleft10mOff.append(i.MagaverageX())
            Yleft10mOff.append(10)
            
        if i.classtype == 'left12mOff':
            Xleft12mOff.append(i.MagaverageX())
            Yleft12mOff.append(12)


    addedlegends=[]        
    for i in range(len(Xleft0mOn)):
        if "0m, Engine on" in addedlegends:
            plt.scatter(Xleft0mOn[i],Yleft0mOn[i],marker='o', s=100, c="gray")
        else:
            plt.scatter(Xleft0mOn[i],Yleft0mOn[i],marker='o', s=100, c="gray", label= "0m, Engine on")
            addedlegends.append( "0m, Engine on");
             
    
    for i in range(len(Xleft2mOn)):
        if "2.5m, Engine on" in addedlegends:
            plt.scatter(Xleft2mOn[i],Yleft2mOn[i],marker='3', s=100, c="gray")
        else:
            plt.scatter(Xleft2mOn[i],Yleft2mOn[i],marker='3', s=100, c="gray", label= "2.5m, Engine on")
            addedlegends.append( "2.5m, Engine on");
    

    for i in range(len(Xleft5mOn)):
        if "5m, Engine on" in addedlegends:
            plt.scatter(Xleft5mOn[i],Yleft5mOn[i],marker='s', s=100, c="gray")
        else:
            plt.scatter(Xleft5mOn[i],Yleft5mOn[i],marker='s', s=100, c="gray", label= "5m, Engine on")
            addedlegends.append( "5m, Engine on");
            
    for i in range(len(Xleft7mOn)):
        if "7.5m, Engine on" in addedlegends:
            plt.scatter(Xleft7mOn[i],Yleft7mOn[i],marker='h', s=100, c="gray")
        else:
            plt.scatter(Xleft7mOn[i],Yleft7mOn[i],marker='h', s=100, c="gray", label= "7.5m, Engine on")
            addedlegends.append( "7.5m, Engine on");

    for i in range(len(Xleft10mOn)):
        if "10m, Engine on" in addedlegends:
            plt.scatter(Xleft10mOn[i],Yleft10mOn[i],marker='^', s=100, c="gray")
        else:
            plt.scatter(Xleft10mOn[i],Yleft10mOn[i],marker='^', s=100, c="gray", label= "10m, Engine on")
            addedlegends.append( "10m, Engine on");

    for i in range(len(Xleft12mOn)):
        if "12.5m, Engine on" in addedlegends:
            plt.scatter(Xleft12mOn[i],Yleft12mOn[i],marker='D', s=100, c="gray")
        else:
            plt.scatter(Xleft12mOn[i],Yleft12mOn[i],marker='D', s=100, c="gray", label= "12.5m, Engine on")
            addedlegends.append( "12.5m, Engine on");
    

    plt.xlabel("Average value of the magnetometer for X axis(uT)")
    plt.ylabel("Distance from test-bed car to the car parked to the left (m)")
    plt.legend(scatterpoints=1, loc='lower right', numpoints=6)
    plt.show()
    
    addedlegends=[]
    for i in range(len(Xleft0mOff)):
        if "0m, Engine off" in addedlegends:
            plt.scatter(Xleft0mOff[i],Yleft0mOff[i],marker='o', s=100, c="gray")
        else:
            plt.scatter(Xleft0mOff[i],Yleft0mOff[i],marker='o', s=100, c="gray", label= "0m, Engine off")
            addedlegends.append( "0m, Engine off");
             
    
    for i in range(len(Xleft2mOff)):
        if "2.5m, Engine off" in addedlegends:
            plt.scatter(Xleft2mOff[i],Yleft2mOff[i],marker='3', s=100, c="gray")
        else:
            plt.scatter(Xleft2mOff[i],Yleft2mOff[i],marker='3', s=100, c="gray", label= "2.5m, Engine off")
            addedlegends.append( "2.5m, Engine off");
    

    for i in range(len(Xleft5mOff)):
        if "5m, Engine off" in addedlegends:
            plt.scatter(Xleft5mOff[i],Yleft5mOff[i],marker='s', s=100, c="gray")
        else:
            plt.scatter(Xleft5mOff[i],Yleft5mOff[i],marker='s', s=100, c="gray", label= "5m, Engine off")
            addedlegends.append( "5m, Engine off");
            
    for i in range(len(Xleft7mOff)):
        if "7.5m, Engine off" in addedlegends:
            plt.scatter(Xleft7mOff[i],Yleft7mOff[i],marker='h', s=100, c="gray")
        else:
            plt.scatter(Xleft7mOff[i],Yleft7mOff[i],marker='h', s=100, c="gray", label= "7.5m, Engine off")
            addedlegends.append( "7.5m, Engine off");

    for i in range(len(Xleft10mOff)):
        if "10m, Engine off" in addedlegends:
            plt.scatter(Xleft10mOff[i],Yleft10mOff[i],marker='^', s=100, c="gray")
        else:
            plt.scatter(Xleft10mOff[i],Yleft10mOff[i],marker='^', s=100, c="gray", label= "10m, Engine off")
            addedlegends.append( "10m, Engine off");

    for i in range(len(Xleft12mOff)):
        if "12.5m, Engine off" in addedlegends:
            plt.scatter(Xleft12mOff[i],Yleft12mOff[i],marker='D', s=100, c="gray")
        else:
            plt.scatter(Xleft12mOff[i],Yleft12mOff[i],marker='D', s=100, c="gray", label= "12.5m, Engine off")
            addedlegends.append( "12.5m, Engine off");
    
  
    
            
    # plt.scatter(Xleft2mOff,Yleft2mOff,marker='3', s=100, c="gray")
    # plt.scatter(Xleft5mOff,Yleft5mOff,marker='s', s=100, c="gray")
    # plt.scatter(Xleft7mOff,Yleft7mOff,marker='h', s=100, c="gray")
    # plt.scatter(Xleft10mOff,Yleft10mOff,marker='^',s=100,c="gray")
    # plt.scatter(Xleft12mOff,Yleft12mOff,marker='D',s=100,c="gray")
    plt.xlabel("Average value of the magnetometer for X axis(uT)")
    plt.ylabel("Distance from test-bed car to the car parked to the left (m)")
    plt.legend(scatterpoints=1, loc='lower right', numpoints=6)
    plt.show()
    
    
    print "Total number of points:"
    print len(Xleft7mOn)
    print len(Yleft7mOn)
    print len(ContainerEvent)

populate_vector(datalistfiles2)
paint(ContainerEvent)

