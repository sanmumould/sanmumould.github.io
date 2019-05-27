
import cv2
import glob

for x in glob.glob('./*.jpg'):
    img = cv2.imread(x)
    h, w, c = img.shape
    s = 600.0 / h
    print(x, s)
    
    if s < 1:
        print(x)
        h, w = int(h*s+0.5), int(w*s+0.5)
        img = cv2.resize(img, (w,h))
        cv2.imwrite(x, img)

