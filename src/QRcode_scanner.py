from pyzbar import pyzbar
import logging
import time
import cv2


def qr_scanner():
    # write qr to file(will be upgrade)
    out_file = open('result.txt', 'w')

    current_qrcode: str = ""
    qr_code: str = ""

    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            qr_code = obj.data.decode("utf-8")

            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, qr_code, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

    # write qr to file(will be upgrade)
        if current_qrcode != qr_code:
            logging.warning(qr_code)
            out_file.write(f"time: {int(time.time())} - data: {qr_code} \n")
            current_qrcode = qr_code
            # time.sleep(5)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    out_file.close()
