from voc_eval import voc_eval

rec,prec,ap = voc_eval('D:/UntitledFolder/keras-yolo3-master/results/{}.txt','D:/UntitledFolder/keras-yolo3-master//VOCdevkit/VOC2007/Annotations/{}.xml','D:/UntitledFolder/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/test.txt','pig','.')

print("rec: ",rec)
print("prec: ",prec)
print("ap: ",ap)