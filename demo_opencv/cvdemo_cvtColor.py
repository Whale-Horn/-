import cv2

img = cv2.imread("C:\\Users\\ASUS\\Desktop\\picture.jpg") # 读取图片内容

cv2.namedWindow("Image")
cv2.imshow("Image",img) # 显示该图片内容

img_cvtHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) # 图片转换HSV空间
cv2.imshow("cvtHSV",img_cvtHSV) # 显示HSV图片

img_GRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换GRAY空间
cv2.imshow("cvtGRAY", img_GRAY) # 显示GRAY图片

cv2.waitKey(0) # 等待一定时间，让显示的内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框