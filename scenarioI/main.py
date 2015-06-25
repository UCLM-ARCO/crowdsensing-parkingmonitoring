import csv
import math
import glob
import matplotlib.pyplot as plt
import re
import copy

#Civitas Cartrack module
from event import *
from svm import *

datalistfiles = glob.glob("./data/*.scv")
print datalistfiles

ProcessingEvent = Event('Unknow')
ContainerEvent = []


def getClassOfEvents(metadatafile):
    metadata = open(metadatafile, 'r')
    for line in metadata:
        if line.startswith("#"):
            fileclass=re.split(r'^#',line)[1]
            fileclass = fileclass[:-1]
            
    metadata.close()
    return fileclass
    
def populate_vector(datalistfiles):
    global ContainerEvent
    indexEvent=0
    for i in datalistfiles:
        with open(i, 'rb') as csvfile:
            fileroot=re.split(r'\.(?!\d)',i)
            metafilename='.'+fileroot[1]+'.metadata'
            classevent=getClassOfEvents(metafilename); 
            spamreader = csv.reader(csvfile, delimiter=',')
            index=0
            ProcessingEvent=Event(classevent)
            for row in spamreader:
                if (index==0): # first line is the header
                    index=index+1
                    continue
                index=index+1
                x=Reading(row)
                ProcessingEvent.insert_reading(copy.deepcopy(x))
                if (index%3!=0):
                    continue
                ContainerEvent.append(copy.deepcopy(ProcessingEvent))
                indexEvent=indexEvent+1;
                #ProcessingEvent.reset()
                ProcessingEvent=Event(classevent)
    
def SearchPosition(Classlist, classl):
    for i in range(0,len(Classlist)):
        if(Classlist[i] == classl):
            return i
        
def paint(ContainerEvent):
    indexEvent = 0
    XpointsX = []
    XpointsY = []
    YpointsX = []
    YpointsY = []
    ZpointsX = []
    ZpointsY = []
    colorVector = []
    colors=['black', 'gray', 'blue', 'hotpink', 'black', 'brown','gray','magenta','cyan','gold','indigo','hotpink']
    classes=['ssb','rsb','rsl','rsn','ssn','ssl']
    filenumber=0
    classesVector=[]
    markerType = ['o','p','s','h','^','H']
    markerVector=[]
    for i in ContainerEvent:
        XpointsX.append(i.averageX())
        XpointsY.append(i.sdX())
        YpointsX.append(i.averageY())
        YpointsY.append(i.sdY())
        ZpointsX.append(i.averageZ())
        ZpointsY.append(i.sdZ())
        colorVector.append(colors[SearchPosition(classes,i.getClass())])
        markerVector.append(markerType[SearchPosition(classes,i.getClass())])
        classesVector.append(i.getClass())

    addedlegends=[]
    for x in range(len(ContainerEvent)):
        if classesVector[x] in addedlegends:
            plt.scatter(YpointsX[x], XpointsX[x], c=colorVector[x], marker=markerVector[x],s=200)
        else:
            plt.scatter(YpointsX[x], XpointsX[x], c=colorVector[x], marker=markerVector[x],s=200, label=classesVector[x])
            addedlegends.append(classesVector[x])
        
    plt.legend(scatterpoints=1, loc='lower left', numpoints=6)
    plt.xlabel('Average X axis magnetometer readings')
    plt.ylabel('Average Y axis magnetometer readings')
    
    

    

populate_vector(datalistfiles)
svmC = Classification(ContainerEvent)
svmC.svc();
plt.figure()
paint(ContainerEvent)
svmC.confusion_matrix()


