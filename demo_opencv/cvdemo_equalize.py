import cv2

img = cv2.imread("C:\\Users\\ASUS\\Desktop\\picture.jpg") # 读取图片内容
cv2.imshow("Image",img)

#彩色图像均衡化，需要分解通道 对每一个通道均衡化
(b,g,r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

# 合并每一个通道
result = cv2.merge((bH,gH,rH))
cv2.imshow('dst',result)

cv2.waitKey (0) # 等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框