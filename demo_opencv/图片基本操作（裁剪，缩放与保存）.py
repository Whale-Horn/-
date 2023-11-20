import cv2

img = cv2.imread("picture.jpeg") # 读取图片文件

cv2.namedWindow('Image')
cv2.imshow("Image",img) # 显示该图片内容

img_cropped=img[0:128,0:128] # 按照像素范围裁剪图片
cv2.imshow('Cropped',img_cropped) # 显示被剪切的图片部分

size=img.shape # 获取图片大小（长，宽，通道数）
img_resize=cv2.resize(img,(size[1]*2,size[0]*2),cv2.INTER_LINEAR) # 图片放大为原来的尺寸 
cv2.imshow('Resized',img_resize) # 显示被放大的图片

cv2.imwrite("picture_resized.jpeg",img_resize) # 保存被放大的图片文件

cv2.waitKey(0) # 等待一定时间，使显示的内容可以被看到

cv2.destroyAllWindows() # 关闭所有显示框