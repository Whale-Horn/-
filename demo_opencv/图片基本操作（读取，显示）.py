import cv2

img = cv2.imread("C:\\Users\\ASUS\\Desktop\\5944bf6cfeec98c198000223e784a5c.jpg") # 读取该图片文件

cv2.namedWindow("Image")
cv2.imshow("Image",img) # 显示该图片内容

cv2.waitKey (0) # 等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框
