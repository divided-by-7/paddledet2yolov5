# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/21 9:58
@Auth ： 除以七  ➗7️⃣
@File ：xml2txt_step2.py
@E-mail ：divided.by.07@gmail.com
@Github ：https://github.com/divided-by-7
"""

import xml.etree.ElementTree as ET
import os
# ————————————————————————————————————————————————————————————————————————————————————————————
# 路径设置
label_list_path = "label_list.txt"  # label_list.txt路径
xml_input = "annotations"  # xml文件路径
save_dir = "label_txt"  # 保存的txt格式label路径
# ————————————————————————————————————————————————————————————————————————————————————————————
# 类别
f = open(label_list_path, encoding="utf-8")
CLASSES = [i.strip() for i in f.readlines()]

if not os.path.exists(save_dir):
    os.mkdir(save_dir)


def convert(size, box):
    # 将bbox的左上角点，右下角点坐标的格式，转换为bbox中心点+bbox的W,H的格式，并进行归一化
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    # 把图像image_id的xml文件转换为目标检测的label文件(txt)
    # 其中包含物体的类别cls,bbox的中心点坐标,以及bbox的W,H
    # 并将四个物理量归一化
    in_file = open(xml_input + "/" + image_id)
    image_id = image_id.split(".")[0]

    out_file = open(save_dir + "/%s.txt" % (image_id), "w")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)
    for obj in root.iter("object"):
        difficult = obj.find("difficult").text
        obj_cls = obj.find("name").text
        if obj_cls not in CLASSES or int(difficult) == 1:
            continue
        cls_id = CLASSES.index(obj_cls)
        xmlbox = obj.find("bndbox")
        points = (float(xmlbox.find("xmin").text),
                  float(xmlbox.find("xmax").text),
                  float(xmlbox.find("ymin").text),
                  float(xmlbox.find("ymax").text))
        bb = convert((w, h), points)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + "\n")


def make_label_txt():
    # labels文件夹下创建image_id.txt
    # 对应每个image_id.xml提取出的bbox信息
    filenames = os.listdir(xml_input)
    for file in filenames:
        convert_annotation(file)


if __name__ == "__main__":
    # 开始提取和转换
    make_label_txt()
