import cv2
import numpy as np
from datetime import datetime
from pyzbar.pyzbar import decode

videoCap = cv2.VideoCapture(0)
videoCap.set(3,1280)
videoCap.set(4,720)

while True:
    jasten, picture = videoCap.read()
    for code in decode(picture):
        qrCode = code.data.decode("utf-8")

        timeDate = datetime.now()
        dateTime = timeDate.strftime("%m/%d/%Y, %H:%M:%S")
        print("Date and Time:",dateTime)

        display = np.array([code.polygon], np.int32)
        display = display.reshape((-1,1,2))
        cv2.polylines(picture,[display], True,(0,0,225),3)

        dataTextFile = open('simbahon.txt', 'w')
        dataTextFile.write(f'{qrCode}\n\n{dateTime}')

        cv2.imshow('Final', picture)
        if cv2.waitKey(1) == ord('q'):
            break