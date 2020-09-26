import os
from yolo import YOLO, detect_video
from PIL import Image

def main():
	yolo = YOLO()
	with open('2007_test.txt', 'r') as f:
		lines = f.readlines()	
	pic = [t.strip('\n') for t in lines]

	with open('model_data\\voc_classes.txt') as f:
		class_names = f.readlines()
	class_names = [c.strip('\n') for c in class_names]
	for i in range(len(pic)):
		print("pic: ", pic[i])	####
		f1 = open('Object-Detection-Metrics-master/groundtruths/'+pic[i].split('.')[0].split('\\')[-1]+'.txt' , 'w')	#这个“\\”着重注意
		for j in range(len(pic[i].split(' '))):
			if j>0:		####重要
				#class_name = class_names[int(pic[i].split(' ')[j].split(',')[-1])]
				#print((pic[i].split(' ')[j].split(',')[-1]))
				#print(pic[i].split(' ')[j].split(',')[0]+' '+pic[i].split(' ')[j].split(',')[1]+' '+pic[i].split(' ')[j].split(',')[2]+' '+pic[i].split(' ')[j].split(',')[3]+'\n')

				class_name = class_names[int(pic[i].split(' ')[j].split(',')[-1])]
				#print(pic[i].split(' '))
				box = pic[i].split(' ')[j].split(',')[0]+' '+pic[i].split(' ')[j].split(',')[1]+' '+pic[i].split(' ')[j].split(',')[2]+' '+pic[i].split(' ')[j].split(',')[3]+'\n'
				#print(class_name)
				content = class_name+' '+box
				#content = box
				f1.write(content)
		f1.close()




		print(pic[i].split(' ')[0])
		image = Image.open(pic[i].split(' ')[0])
		print(type(image))
		r_image, output = yolo.detect_image(image)
		#r_image = yolo.detect_image(image)

		f2 = open('Object-Detection-Metrics-master/detections/'+pic[i].split('.')[0].split('\\')[-1]+'.txt' , 'w')	#这个“\\”着重注意
		for i, c in reversed(list(enumerate(output[2]))):
			box = output[0][i]
			score = output[1][i]
			top, left, bottom, right = box
			content = '%s %.5f %d %d %d %d\n'%(class_names[c], score, left, top, right, bottom)
			f2.write(content)
		f2.close()




if __name__=='__main__':
	main()


