import cv2

if __name__ == "__main__":
    im = cv2.imread('test_black.png')
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    idx =0
    for cnt in contours:
        print(cnt)
        idx += 1
        x,y,w,h = cv2.boundingRect(cnt)
        roi=im[y:y+h,x:x+w]
        cv2.imwrite(str(idx) + '.jpg', roi)
        cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
    cv2.imshow('img',im)
    cv2.waitKey(0)