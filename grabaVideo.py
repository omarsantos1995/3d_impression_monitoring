#autor:Omar Santos Bernabé

"""grabaCamara:
algoritmo que abre una cámara en vivo y que camptura los frames del estudio de la impresora al instante"""



import numpy as np
import cv2



def grabaVideo():
    cap=cv2.VideoCapture(0)
    todook=False
    valido=False#Luego se borra esta linea cuando funcione funcion existeVideo
    while not todook:
        nombreVideo = input('Introduce nombre: ')
        #valido=existeVideo(nombreVideo)
        #if valido==False:
        todook=True
    if valido==False:
        # Define el codec y crea el objeto VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*"DIVX")
        out = cv2.VideoWriter(nombreVideo+'.avi',fourcc,20.0,(640,480))
        while(cap.isOpened()):
            #Captura cada frame
            ret, frame = cap.read()
            if ret==True:
                # gruarda
                out.write(frame)
                cv2.imshow('Camara',frame)
                #Si pulsamos la letra c durante la ejecución se parará
                if cv2.waitKey(1) & 0xFF == ord('c'):
                    break
        # When everything done, release the video capture object
        cap.release()
        # Cerramos todas las visualizaciones
        cv2.destroyAllWindows()
        