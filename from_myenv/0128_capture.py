#0128_capture.py 

import cv2

HIGH_VALUE = 10000
WIDTH = HIGH_VALUE
HEIGHT = HIGH_VALUE

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)

print(width, height, fps)

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

# import cv2
# import time
# num = 1
# cap = cv2.VideoCapture(3)
# print("2")
# while True:
#     ret, img = cap.read()
#     #print("3")
#     cv2.imshow('Frame', img)
#     #print("4")
#     if cv2.waitKey(1) & 0xFF == ord('c'):
#         cv2.imwrite(str(num) + '.jpg', img)
#         print('capture ' + str(num) + ' successful')
#         num = num +1
#     if num==4:
#         break
# print("3")
# cap.release()
# cv2.destroyAllWindows()