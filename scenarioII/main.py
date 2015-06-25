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




datalistfiles = glob.glob("./data/2015-04-28-09-50+0200-spacio-disca.scv")

print datalistfiles

ProcessingEvent = Event('Unknow')
ContainerEvent = []
VENTANA=5

def populate_vector(datalistfiles):
    global ContainerEvent
    indexEvent=0
    for i in datalistfiles:
        with open(i, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            index=0
            ProcessingEvent=Event()
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
                ProcessingEvent=Event()
    
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


    for i in ContainerEvent:
        XpointsX.append(i.time)
        XpointsY.append(i.MagaverageX())
        YpointsX.append(i.time)
        YpointsY.append(i.MagaverageY())
        ZpointsX.append(i.time)
        ZpointsY.append(i.MagaverageZ())
        
        
    plt.scatter(XpointsX, XpointsY,marker='o')
    plt.xlabel('Time (ms)')
    plt.ylabel('Average X axis magnetometer readings (uT)')
    plt.figure()
    
    plt.scatter(YpointsX, YpointsY,marker='o')
    plt.xlabel('Time (ms)')
    plt.ylabel('Average Y axis magnetometer readings (uT)')
    plt.figure()
    plt.scatter(ZpointsX, ZpointsY,marker='o')
    plt.xlabel('Time (ms)')
    plt.ylabel('Average Z axis magnetometer readings (uT)')
    
    #plt.show()
    print "Total number of points:"
    print len(ContainerEvent)


    
def main(argv=None):
    """CityParkingTrack: main.
    """
    populate_vector(datalistfiles)
    # svmC = Classification(ContainerEvent)
    # svmC.svc();
    # Eventprediction = ContainerEvent[0]
    # Eventprediction.objectprint()
    # print "Ese Evento pertenece a la clase:"
    # print svmC.predict([Eventprediction.averageY(),Eventprediction.sdY()])
    plt.figure()
    paint(ContainerEvent)
    plt.show()
    # svmC.confusion_matrix()

            


if __name__ == "__main__":
    main()




