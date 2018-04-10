#autor:Omar Santos Bernabé

"""videoTReal:
algoritmo que abre una cámara en vivo y procesa la imagen de forma que según el rango de colores que nos interese obtener de la imagen
aisla los objetos en ese rango y calcula su area remarcándola."""



import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import sqlite

def videoTReal():
    cap = cv2.VideoCapture(0)

    while(True):
        #Capturamos una imagen y la transformamos a canal HSV
        _, frame = cap.read()
        frame=cv2.blur(frame,(5,5))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Seleccionamos un rango de color que es el que nos interesa
        lower_color = np.array([100,100,100])
        upper_color = np.array([180,255,255])
        #Creamos la máscara respecto a esos valores del rango
        mask = cv2.inRange(hsv, lower_color, upper_color)
        #mask2 = cv2.inRange(hsv, lower_color, upper_color)
        #mask=mask+mask2
        res = cv2.bitwise_and(frame,frame, mask= mask)
        
        kernel1 = np.ones((15,15),np.uint8)
        kernel2 = np.ones((5,5),np.uint8)
        
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel1)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel2)
        res = cv2.bitwise_and(frame,frame, mask= opening)
        _,contours,_= cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #C
        for c in contours:
            area = cv2.contourArea(c)
            if area > 500:
                cv2.drawContours(frame, [c], 0, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.drawContours(res, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Original',frame)
        cv2.imshow('Objeto',res)
        cv2.imshow('Final',opening)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    cap.release()
    cv2.destroyAllWindows()