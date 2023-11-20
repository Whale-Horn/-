import cv2
import os

index = 1

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
            cv2.imwrite("capture%d.jpeg" % (index,),frame)
            print("%d 张图片已拍摄"% (index,))
            index += 1
      if input == ord('q'):
            break

cap.release() # 释放摄像头资源

cv2.destroyAllWindows() # 关闭显示框
