#autor:Omar Santos Bernabé

"""videoTReal:
algoritmo que abre una cámara en vivo y procesa la imagen de forma que según el rango de colores que nos interese obtener de la imagen
aisla los objetos en ese rango y calcula su area remarcándola."""



import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import sqlite

#falta conseguir que funcione la carga del video y procesar las imagenes del video como en videoTReal()
def cargaVideo():
    todook=False
    valido=True#Luego se borra esta linea cuando funcione funcion existeVideo
    while not todook:
        nombreVideo = input('Introduce nombre: ')
        #valido=existeVideo(nombreVideo)
        #if valido==True:
        todook=True
    if valido==True:
        video = cv2.VideoCapture(nombreVideo+'.avi')
        # Comprueba que los videos se han abierto bien
        if(video.isOpened()== False): 
            print("Error al abrir algún fichero de video")
            video.open()
        #Lee el video entero
        while(video.isOpened):
            #Captura cada frame
            ret, frame = video.read()
            #plt.imshow(frame)
            if ret==True :
                cv2.imshow('Video',frame)
            else: 
                break#print("El video se ha terminado o se ha producido un error")
        # When everything done, release the video capture object
        video.release()
        # Cerramos todas las visualizaciones
        cv2.destroyAllWindows()