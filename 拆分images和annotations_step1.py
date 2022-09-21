# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/21 9:58
@Auth ： 除以七  ➗7️⃣
@File ：拆分images和annotations_step1.py
@E-mail ：divided.by.07@gmail.com
@Github ：https://github.com/divided-by-7
"""

import os
import shutil
from tqdm import tqdm

data_path = "all_data"
images_path = "images"
annotations_path = "annotations"


# ————————————————————————————————————————————————————————————————————————————————
def create_path(image_path="images", annotation_path="annotations"):
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    if not os.path.exists(annotation_path):
        os.mkdir(annotation_path)


def split_file():
    tq = tqdm(os.listdir(data_path))
    for f in tq:
        tq.set_description("正在拆分image.jpg和annotation.xml文件...")
        if ".xml" in f:
            shutil.copy(data_path + "/" + f, annotations_path + "/" + f)
        else:
            shutil.copy(data_path + "/" + f, images_path + "/" + f)

    tq.close()


if __name__ == "__main__":
    create_path(images_path, annotations_path)
    split_file()
