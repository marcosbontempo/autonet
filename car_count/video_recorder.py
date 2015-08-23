# Bibliotecas
import sys
import cv
import cv2
import time
import numpy as np

################# Gravacao do video ########################
CAM=int(sys.argv[1])
VIDEO_FILE=sys.argv[2]
COUNT_TIME=int(sys.argv[3])
# Capturando o video
cap = cv2.VideoCapture(CAM)
# Criando o objeto de gravacao de video 
out = cv2.VideoWriter(VIDEO_FILE,cv2.cv.CV_FOURCC('M','J','P','G'), 30, (640,480))
# Contagem de gravacao
time_in=time.time()
time_now=time.time()
# Gravando
while((time_now-time_in)<COUNT_TIME):
    ret, frame = cap.read()
    if ret==True:

        # Escrevendo o frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    time_now=time.time()
# Libera a janela de gravacao
cv2.destroyAllWindows()

