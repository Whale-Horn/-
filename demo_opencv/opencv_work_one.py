import cv2
import os
import numpy as np

cap = cv2.VideoCapture(0) # 初始化摄像头对象
width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height) # 设置摄像头的长宽参数 ： 640*480
while True:
      ret, frame = cap.read() # 读取摄像头的一帧
      cv2.imshow("capture",frame) # 显示摄像画面
      input = cv2.waitKey(1) & 0xFF # 读取按键（x为拍照，q为退出循环）
      if input == ord("x"): # 保存图片
            cv2.imwrite("picture_primary.jpeg",frame) # 将该帧数据写入图片文件
            break
cap.release() # 释放摄像头资源

# 对图片进行直方图均衡化
img = cv2.imread("picture_primary.jpeg") # 读取图片内容
cv2.imshow("Image",img)
#彩色图像均衡化，需要分解通道 对每一个通道均衡化
(b,g,r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
dst = cv2.merge((bH,gH,rH))
cv2.imshow('dst',dst)
cv2.imwrite("dst.jpeg",dst)

#色彩空间变换
img_cvtHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # 图片转换HSV空间
cv2.imshow("cvtHSV",img_cvtHSV) # 显示HSV图片
cv2.imwrite("cvtHSV.jpeg",img_cvtHSV) 
#重新初始化原图
img = cv2.imread("picture_primary.jpeg") 

#灰度化
img_cvtGRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换灰度图
cv2.imshow('img_cvtGRAY',img_cvtGRAY)
cv2.imwrite("img_cvtGRAY.jpeg",img_cvtGRAY)

#二值化
img_GRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换GRAY空间
ret,img_binary0=cv2.threshold(img_GRAY,100,255,cv2.THRESH_BINARY) # 采用固定阈值100进行二值化
cv2.imshow("cvtGRAY0", img_binary0) # 显示固定阈值二值化结果
cv2.imwrite("cvtGRAY0.jpeg",img_binary0)
ret,img_binary1=cv2.threshold(img_GRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) # 采用大律法自适应计算合适的阈值进行二值化
cv2.imshow("cvtGRAY1", img_binary1) # 显示自适应大律法阈值二值化结果
cv2.imwrite("cvtGRAY1.jpeg",img_binary1)
ret,img_binary2=cv2.threshold(img_GRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE) # 采用三角法自适应计算合适的阈值进行二值化
cv2.imshow("cvtGRAY2", img_binary2) # 显示自适应三角法阈值二值化结果
cv2.imwrite("cvtGRAY2.jpeg",img_binary2)

#开闭运算
kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) # 十字结构
opening = cv2.morphologyEx(img_binary0,cv2.MORPH_OPEN,kernel) # 开运算
cv2.imshow('canny1',opening)
cv2.imwrite('canny1.jpeg',opening)
closing = cv2.morphologyEx(img_binary0,cv2.MORPH_CLOSE,kernel) # 闭运算
cv2.imshow('canny2',closing)
cv2.imwrite('canny2.jpeg',closing)

#寻找轮廓
contours,hierarchy = cv2.findContours(img_binary1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # 寻找图片轮廓
cv2.drawContours(img,contours,-1,(0,0,255),3) # 在已有的图片中画出轮廓
cv2.imshow('Image_contour',img) # 显示增加轮廓的图片
cv2.imwrite('Image_contour.jpeg',img)

cv2.waitKey (0) # 等待一定时间，让显示的内容可以被看到
cv2.destroyAllWindows() # 关闭所有显示框
