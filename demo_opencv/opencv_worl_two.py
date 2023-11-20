import cv2
import numpy as np

img = cv2.imread("shape.jpg") # 读取图片文件
cv2.namedWindow("Image")
cv2.imshow("Image",img) # 显示该图片的内容
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #图片转换为灰度格式
edges = cv2.Canny(gray,90,110) # 对图片进行边缘检测
cv2.imshow('Hough',edges)

cv2.waitKey(0)
# 通过HoughCircle方法检测出圆形
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,100,param2=22,maxRadius=100,minRadius=30)
# 在图片中标识出找到的圆形
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for i in circles:
        center = (i[0], i[1])
        radius = int(i[2]) # 将半径转换为整数类型
        cv2.circle(img, center, radius, (0, 255, 0), 2)  # 画出外圆
        cv2.circle(img, center, 2, (0, 0, 255), 3)  # 画出圆心
else:
    print("未检测到圆形")

 # 通过HoughLinesP检测直线
lines = cv2.HoughLinesP(edges,1,np.pi/180,200,20,10)
# 在图片中标识出找到的直线
for line in lines:
    x1 = int(round(line[0][0]))
    y1 = int(round(line[0][1]))
    x2 = int(round(line[0][2]))
    y2 = int(round(line[0][3]))
    cv2.line(img,(x1,y1),(x2,y2),(255,255,0),10)

cv2.imshow('Hough_shape',img)
cv2.imwrite('Hough_shape.jpg',img)

cv2.waitKey (0) # 等待一定时间，让显示的内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框