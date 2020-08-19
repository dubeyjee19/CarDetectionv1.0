import cv2
cars_cascade = cv2.CascadeClassifier('C:\\Users\\N K Dubey\\OneDrive\\Desktop\\cars.xml')  # location of cars.xml file


def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,255,0), thickness=2)
        cv2.putText(frame, 'CAR', (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)  # text you want for the frame
    return frame


def Simulator():
    CarVideo = cv2.VideoCapture('C:\\Users\\N K Dubey\\OneDrive\\Desktop\\output.mp4')  # location of the recordeed video
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cars_frame = detect_cars(frame)
            cv2.imshow('frame', cars_frame)
        else:
            break
        if controlkey == ord('q'):  # press 'q' to exit application
            break

    CarVideo.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Simulator()
