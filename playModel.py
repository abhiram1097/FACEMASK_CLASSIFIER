import tensorflow
from tensorflow import keras
import cv2
from cv2 import VideoCapture
from imutils.video import VideoStream
from keras.preprocessing.image import img_to_array 
from mtcnn.mtcnn import MTCNN
import numpy as np
import matplotlib.pyplot as plt 


def do(video) :
    while True:
        frame  =  video.read()
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #frame = cv2.resize(frame,(224,224))
        vectors = Face_detect.detect_faces(frame)
        #Wprint(vectors)
        for vector in vectors :
            x,y,width,height = vector['box']
            image = frame[y:y + height,x:x + width]
            
            #exit()
            image = cv2.resize(image,(224,224))
            #imageList.append(image)
            #cv2.imshow('Frame',image)
            #image = img_to_array(image)
            image = np.array([image])
        
            #print(image.shape)
            image = image/255
            #print(image.shape)
            prob  = Model.predict([image]) 
            prob = 1 - prob
            print(prob)
            rgb = (0,0,0)
            if prob < 0.38 :
                rgb = (255,0,0)
            else:
                rgb = (0,255,0)
             
            cv2.rectangle(frame,(x,y),(x+width,y+height),rgb,2)
            print('Hi')
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Camera',frame)
            


imageList = []
Model = keras.models.load_model('C:/Users/abhir/pgms/TensorFlow/Rep1')
Face_detect = MTCNN()
video = VideoStream(0).start()
#rint(video.isOpened())
cv2.namedWindow('Camera')
cv2.namedWindow('Frame')
try :
    do(video)
except:
    
    video.release()


