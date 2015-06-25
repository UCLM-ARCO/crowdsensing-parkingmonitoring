
import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from event import *


class Classification:
    Points = []
    PointClass = []
    target_names = []
    
    def __init__(self,Events):
        self.ContainerEvents = Events;
        print len(self.ContainerEvents)
        self.clf = svm.SVC()
        for i in self.ContainerEvents:
            self.Points.append([i.averageY(),i.averageX()])
            EventClass= i.getClass()
            self.PointClass.append(EventClass)
            if (EventClass in self.target_names)==False:
                self.target_names.append(EventClass)
        
    def svc(self):
        self.clf.fit(self.Points,self.PointClass)

    def predict(self, point):
        return self.clf.predict(point)
    
    def plot_confusion_matrix(self, cm, title='Confusion matrix', cmap=plt.cm.Blues):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(self.target_names))
        plt.xticks(tick_marks, self.target_names, rotation=45)
        plt.yticks(tick_marks, self.target_names)
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    def confusion_matrix(self):
        X_train, X_test, y_train, y_test = train_test_split(self.Points, self.PointClass, random_state=0)
        print "Total number of points: "+ str(len(self.Points)) + ", "+ str(len(X_train))+ " points will be used for the model and "+str(len(X_test))+" will be used to test the model"
      
        #self.classf = svm.SVC(kernel='linear', C=0.01)
        self.classf = svm.SVC()
        y_pred = self.classf.fit(X_train, y_train).predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)
        print('Confusion matrix, without normalization')
        print(cm)
        plt.figure()
        self.plot_confusion_matrix(cm)
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print('Normalized confusion matrix')
        print(cm_normalized)
        plt.figure()
        self.plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix')
        plt.show()
