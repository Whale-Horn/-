import cv2
import numpy as np

img = cv2.imread("C:\\Users\\ASUS\\Desktop\\picture.jpg") # 读取图片内容
cv2.imshow("Image",img)

img_cvtGRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换GRAY空间
ret,img_binary0=cv2.threshold(img_cvtGRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE) # 采用三角法自适应计算合适的阈值进行二值化
cv2.imshow("cvtGRAY2", img_binary0) # 显示自适应三角法阈值二值化结果

kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) # 十字结构

opening = cv2.morphologyEx(img_binary0,cv2.MORPH_OPEN,kernel) # 开运算
cv2.imshow('canny1',opening)

closing = cv2.morphologyEx(img_binary0,cv2.MORPH_CLOSE,kernel) # 闭运算
cv2.imshow('canny2',closing)

cv2.waitKey (0) # 等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框