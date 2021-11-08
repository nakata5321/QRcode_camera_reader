#from pyzbar import
import qrtools
import subprocess
import numpy as np
import logging
import time
import cv2
import sys, qrcode

cap = cv2.VideoCapture("vid.mp4")
def qr_scanner():
    # write qr to file(will be upgrade)
    out_file = open('result.txt', 'w')

    current_qrcode: str = ""
    qr_code: str = ""

    #cap = cv2.VideoCapture("rtsp://admin:qwerty12345@192.168.1.64:554/Streaming/Channels/101")


    # command = ['ffmpeg',
    #            '-rtsp_transport', 'tcp',
    #            '-i', 'rtsp://admin:qwerty12345@192.168.1.64:554/Streaming/Channels/101',
    #            '-r', '25',
    #            '-f', 'image2pipe',  # Use image2pipe demuxer
    #            '-pix_fmt', 'bgr24',  # Set BGR pixel format
    #            # '-filter:v', 'fps=25',
    #            '-vcodec', 'rawvideo',  # Get rawvideo output format.
    #            '-']

    # p1 = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # width = 1920
    # height = 1080

    while True:
        # Capture frame-by-frame
        # raw_frame = p1.stdout.read(width * height * 3)
        ret, frame = cap.read()
        # frame = np.fromstring(raw_frame, np.uint8)
        # frame = frame.reshape((height, width, 3))
        #decoded_objects = pyzbar.decode(frame)
        #print(len(decoded_objects))
        qr = qrtools.QR()

        if qr.decode(frame):
            print(qr.data)
            print(qr.data_type)
            print(qr.data_to_string())
        #for obj in decoded_objects:
            #qr_code = obj.data.decode("utf-8")

            # (x, y, w, h) = obj.rect
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv2.putText(frame, qr_code, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            #             0.5, (0, 0, 255), 2)

    # write qr to file(will be upgrade)
        #if current_qrcode != qr_code:
            #logging.warning(qr_code)
            # out_file.write(f"time: {int(time.time())} - data: {qr_code} \n")
            # qcurrent_qrcode = qr_code
            # time.sleep(5)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    # try:
    #     p1.wait(1)
    # except (p1.TimeoutExpired):
    #     p1.terminate()
    # cv2.destroyAllWindows()
    out_file.close()

qr_scanner()
