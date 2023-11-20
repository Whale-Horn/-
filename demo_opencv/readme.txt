opencv_work_one:
按x进行拍照，最终保存的jpeg文件过多，且文件命名方式并不唯一，为避免混淆，故在此统一介绍：
picture_primary.jpeg：原始图像
dst.jpeg：直方图均衡化
cvtHSV.jpeg：色彩变换
img_cvtGRAY.jpeg：灰度化
cvtGRAY0.jpeg：采用固定阈值100进行二值化
cvtGRAY1.jpeg：采用大律法自适应计算合适的阈值进行二值化
cvtGRAY2.jpeg：采用三角法自适应计算合适的阈值进行二值化
canny1.jpeg：开运算
canny2.jpeg：闭运算
Image2_contour.jpeg：增加轮廓后的图片
重复运行新拍摄的图片会替代原有图片，并不会占用多余内存

opencv_work_two:
略