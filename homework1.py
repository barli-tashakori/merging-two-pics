import cv2 as cv
import numpy as np

my_image=cv.imread("me.jpg",0)
jisoo_image=cv.imread("3l9eq5e6a4o81.webp",0)

height,width=my_image.shape
jisoo_image_image=cv.resize(jisoo_image,(height,width))
merge1=my_image//2+jisoo_image//4
merge2=my_image//4+jisoo_image//2

result=np.zeros((height,width*2),dtype="uint8")
#result[0:height,0:width]=my_image
result[0:height,0:width]=merge1
result[0:height,width:width*2]=merge2
#result[0:height,width*3:width*4]=jisoo_image

cv.imshow("result.jpg",result)
cv.waitKey()
cv.imwrite("result.jpg",result)


