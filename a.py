import cv2

image = cv2.imread(r"C:\Users\Asus\OneDrive\Desktop\intern\pencil_sketch\pexels-flickr-151511.jpg")

gimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not (gimg)

blur= cv2.GaussianBlur (invert, (21,21),0)

ib= cv2.bitwise_not(blur)

s=cv2.divide (gimg, ib, scale=256.0)

cv2.imwrite("s.jpg", s)