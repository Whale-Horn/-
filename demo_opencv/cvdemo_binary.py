import cv2
img = cv2.imread("C:\\Users\\ASUS\\Desktop\\picture.jpg") # 读取图片内容
cv2.namedWindow("Image")
cv2.imshow("Image",img) # 显示该图片内容

img_GRAY = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) # 图片转换GRAY空间

ret,img_binary0=cv2.threshold(img_GRAY,100,255,cv2.THRESH_BINARY) # 采用固定阈值100进行二值化
cv2.imshow("cvtGRAY0", img_binary0) # 显示固定阈值二值化结果

ret,img_binary1=cv2.threshold(img_GRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) # 采用大律法自适应计算合适的阈值进行二值化
cv2.imshow("cvtGRAY1", img_binary1) # 显示自适应大律法阈值二值化结果

ret,img_binary2=cv2.threshold(img_GRAY,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE) # 采用三角法自适应计算合适的阈值进行二值化
cv2.imshow("cvtGRAY3", img_binary2) # 显示自适应三角法阈值二值化结果

cv2.waitKey (0) # 等待一定时间，让显示内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框