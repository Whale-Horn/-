import cv2
import os

cap = cv2.VideoCapture(0) # 初始化摄像头对象

width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height) # 设置摄像头的长宽参数 ： 640*480

ret, frame = cap.read() # 读取摄像头的一帧
cv2.imwrite("capture.jpeg",frame) # 将该帧数据写入图片文件

cap.release() # 释放摄像机资源
