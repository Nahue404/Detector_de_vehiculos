#Exportamos OpenCV
import cv2
import numpy as np

CAR = cv2.CascadeClassifier('cars.xml')
#Numero de camara --agregar boton de camara frontal
N = 0

#Camara
#Camara = cv2.VideoCapture(N)
Camara = cv2.VideoCapture('Auto1.mp4')

#Activar la camara
while True:
	ret, frame = Camara.read()

	#Sustracion de fondo

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#Detectar Auto
	cars = CAR.detectMultiScale(gray, 1.1, 11)

	#Captura de Vehiculos en un rectangu
	for (x,y,w,h) in cars:
		plate = frame[y:y + h, x:x + w]
		cv2.rectangle(frame,(x,y),(x +w, y +h) ,(51,51,255),2)
		cv2.rectangle(frame, (x, y - 40), (x + w, y), (51,51,255), -2)
		
		#Letra
		cv2.putText(frame, 'auto', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,(100, 200, 200), 2)
	
	frame = cv2.resize(frame,(600, 500))

	if ret == False: break

	cv2.imshow('VicenVision', frame)

	#Avisar si hay autos y si estan en movimientos


	#Agregar boton de salir
	if cv2.waitKey(1) & 0xFF == ord ('q'):
		break

Camara.release()
cv2.destroyAllWindows()