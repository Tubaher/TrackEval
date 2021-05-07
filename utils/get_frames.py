import cv2

# Opens the Video file
cap= cv2.VideoCapture('clarocrop.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i>=0 and i <10:
        cv2.imwrite('./frames/00_000_00000'+str(i)+'.jpg',frame)
    elif i >=10 and i<=99:
        cv2.imwrite('./frames/00_000_0000'+str(i)+'.jpg',frame)
    elif i >=100 and i<=999:
        cv2.imwrite('./frames/00_000_000'+str(i)+'.jpg',frame)

    #cv2.imwrite('./crops/00_000_000'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()