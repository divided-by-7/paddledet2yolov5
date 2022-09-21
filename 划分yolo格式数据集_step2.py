import pandas as pd
import os
import shutil
from tqdm import tqdm

# 请确保已经运行过step1
# argparse：
file_name = "yolov5数据集"  # 数据将在此目录下存为yolov5格式副本
train_file_name = "train.txt"  # paddle detection的训练集样本名字的位置
valid_file_name = "valid.txt"  # paddle detection的验证集样本名字的位置
test_file_name = 'test.txt'  # paddle detection的测试集样本名字的位置
txt_label_file_name = "label_txt"  # xml2txt保存的txt文件位置
is_valid_dataset = True  # 是否划分出验证集，为True则分为训练集，测试集，验证集；为False分为训练集，测试集。
# _______________________________________________________________________________________
train = pd.read_csv(train_file_name, sep=" ", names=['image', 'label'])
valid = pd.read_csv(valid_file_name, sep=" ", names=['image', 'label'])
test = pd.read_csv(test_file_name, sep=" ", names=['image', 'label'])


# make dir
# 注：ultralytics公司提供的yolov5能自动划分训练集和验证集，因此只需要划分验证集和测试集即可
def makedir():
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    if not os.path.exists(file_name + "/Train_dataset"):
        os.mkdir(file_name + "/Train_dataset")
        os.mkdir(file_name + "/Train_dataset/images")
        os.mkdir(file_name + "/Train_dataset/labels")

    if not os.path.exists(file_name + "/Test_dataset"):
        os.mkdir(file_name + "/Test_dataset")
        os.mkdir(file_name + "/Test_dataset/images")
        os.mkdir(file_name + "/Test_dataset/labels")

    if not os.path.exists(file_name + "/Valid_dataset"):
        os.mkdir(file_name + "/Valid_dataset")
        os.mkdir(file_name + "/Valid_dataset/images")
        os.mkdir(file_name + "/Valid_dataset/labels")


# 复制训练集
def copydata():
    # tqdm.write("")
    A = tqdm(train['image'])
    for train_img in A:
        A.set_description("正在复制训练集图片样本到.Train_dataset/images/")
        shutil.copy(train_img, file_name + "/Train_dataset/images/" + train_img.replace("./images/", ""))
    A.close()

    B = tqdm(train['label'])
    for train_label in B:
        B.set_description("正在复制训练集图片标签到.Train_dataset/labels/")
        shutil.copy(txt_label_file_name + train_label.replace("./annotations", "").replace(".xml", "") + ".txt",
                    file_name + "/Train_dataset/labels/" + train_label.replace("./annotations", "").replace(".xml",
                                                                                                      "") + ".txt")
    B.close()

    if is_valid_dataset:
        # # 复制验证集到验证集
        C = tqdm(valid['image'])
        for valid_img in C:
            C.set_description("正在复制验证集图片样本到.Valid_dataset/images/")
            shutil.copy(valid_img, file_name + "/Valid_dataset/images/" + valid_img.replace("./images/", ""))
        C.close()

        D = tqdm(valid['label'])
        for valid_label in D:
            D.set_description("正在复制验证集图片标签到.Valid_dataset/labels/")
            shutil.copy(txt_label_file_name + valid_label.replace("./annotations", "").replace(".xml", "") + ".txt",
                        file_name + "/Valid_dataset/labels/" + valid_label.replace("./annotations", "").replace(".xml",
                                                                                                                "") + ".txt")
        D.close()

    else:
        # 复制验证集到训练集
        E = tqdm(valid['image'])
        for valid_img in E:
            E.set_description("正在复制验证集图片样本到.Train_dataset/images/")
            shutil.copy(valid_img, file_name + "/Train_dataset/images/" + valid_img.replace("./images/", ""))
        E.close()

        F = tqdm(valid['label'])
        for valid_label in F:
            F.set_description("正在复制验证集图片标签到.Train_dataset/labels/")
            shutil.copy(txt_label_file_name + valid_label.replace("./annotations", "").replace(".xml", "") + ".txt",
                        file_name + "/Train_dataset/labels/" + valid_label.replace("./annotations", "").replace(".xml",
                                                                                                                "") + ".txt")
        F.close()

    # 复制测试集
    G = tqdm(test['image'])
    for test_img in G:
        G.set_description("正在复制测试集图片样本到.Test_dataset/images/")
        shutil.copy(test_img, file_name + "/Test_dataset/images/" + test_img.replace("./images/", ""))
    G.close()

    H = tqdm(test['label'])
    for test_label in H:
        H.set_description("正在复制测试集图片标签到.Test_dataset/labels/")
        shutil.copy(txt_label_file_name + test_label.replace("./annotations", "").replace(".xml", "") + ".txt",
                    file_name + "/Test_dataset/labels/" + test_label.replace("./annotations", "").replace(".xml",
                                                                                                          "") + ".txt")
    H.close()

if __name__ == "__main__":
    makedir()
    copydata()
