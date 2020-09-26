# keras-yolo3
keras编写的yolov3，做出了以下更改：

1. 添加了"VOC测试集信息生成.py"，用于对测试文件"2007_test.txt"中记录的图片生成测试信息，
	存放到Object-Detection-Metrics-master文件夹中的detections和groundtruths文件夹中，一个xml文件对应一个txt文件

2. 更改了yolo.py文件里的"detect_image"函数，增加了一个返回值，便于"VOC测试集信息生成.py"处理

3. 添加了"main.py"，用于根据第一步的生成的2个文件夹中的txt信息进行IOU和mAP，文件网址"https://github.com/Cartucho/mAP"



注意事项：
	voc_annotations.py文件生成2007_test文件时注意路径的生成
	"VOC测试集信息生成.py"中的路径需要注意空格，其中对字符串用空格切分了


效果：
	Object-Detection-Metrics-master文件夹中的detections和groundtruths文件夹中生成了大量测试txt文件，并且运行main.py能显示计算mAP
