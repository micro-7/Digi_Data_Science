import cv2
path= r'C:\Users\mihir\Videos\Valorant\New folder\Valorant 2023.05.09 - 02.01.06.04.DVR.mp4'
video = cv2.VideoCapture(path)

while True:
    status, image = video.read()
    if not status:
        print('could not read frame')
        break

    #logic
    image = cv2.resize(image,(0,0),fx=0.4,fy=0.4)
    img_edge = cv2.Canny(image, 100, 200)
    cv2.imshow('video', img_edge)
    if cv2.waitKey(1)==ord('q'): #if q is pressed then break
        break

video.release()

cv2.destroyAllWindows()