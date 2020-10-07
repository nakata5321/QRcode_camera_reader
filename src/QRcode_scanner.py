from pyzbar import pyzbar
import logging
import time
import cv2

def QR_scanner():
    #write qr to file(will be upgrate)
    out_file = open('result.txt', 'w')

    current_QRcode: str = ""
    QR_code: str = ""

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            QR_code = obj.data.decode("utf-8")

    #write qr to file(will be upgrate)
        if(current_QRcode != QR_code):
            logging.warning(QR_code)
            out_file.write(f"time: {int(time.time())} - data: {QR_code}")
            current_QRcode = QR_code
            time.sleep(5)



        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    out_file.close()
