import cv2
img=cv2.imread('img.jpg')
gray=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Anime',img)#do not convert into rgb
cv2.imshow('Anime_gray',gray)
cv2.waitKey(0)#0 for imfinite time
cv2.destroyAllWindows()