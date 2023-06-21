import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = [('coco', 'trainlist')]  # 改成自己建立的myData

classes = ['person','car']
objnum = [0,0,0]
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(year, image_id):
    in_file = open('extracted_train_dataset/annotations/%s.xml' % (image_id))  # 原始碼VOCdevkit/VOC%s/Annotations/%s.xml
    out_file = open('extracted_train_dataset/labels/%s.txt' % (image_id), 'w')  # 原始碼VOCdevkit/VOC%s/labels/%s.txt
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()

wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('extracted_train_dataset/labels/'):  # 改成自己建立的myData
        os.makedirs('extracted_train_dataset/labels/')
    image_ids = open('%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s_%s.txt' % (year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/images/%s.png\n' % (wd, image_id))
        convert_annotation(year, image_id)
    
    list_file.close()