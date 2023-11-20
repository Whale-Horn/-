import cv2
img = cv2.imread("C:\\Users\\ASUS\\Desktop\\picture.jpg") # 读取图片内容

img_cvtGRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换灰度图

ret,img_binary1=cv2.threshold(img_cvtGRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE) # 采用大律法自适应计算合适的阈值进行二值化

contours,hierarchy = cv2.findContours(img_binary1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # 寻找图片轮廓
cv2.drawContours(img,contours,-1,(0,0,255),3) # 在已有的图片中画出轮廓
cv2.imshow('Image1',img_binary1) # 显示二值化后的图片
cv2.imshow('Image2',img) # 显示增加轮廓的图片

cv2.waitKey (0) # 等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框