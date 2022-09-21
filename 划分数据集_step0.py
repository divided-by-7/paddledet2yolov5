import os
import random

# argparse
image_path = "./images"
label_path = "./annotations"
shuffle = False  # 乱序
dataset_rate = [340, 513, 167]  # 训练集：验证集：测试集
train_path = "train.txt"
valid_path = "valid.txt"
test_path = "test.txt"


# ____________________________________________________________________________________
def main():
    image = os.listdir(image_path)
    # print(image)
    if shuffle:
        random.shuffle(image)
    train_rate = dataset_rate[0] / sum(dataset_rate)
    valid_rate = dataset_rate[1] / sum(dataset_rate)
    test_rate = dataset_rate[2] / sum(dataset_rate)

    train_idx = int(train_rate * len(image))
    valid_idx = train_idx + int(valid_rate * len(image))
    print(" 是否乱序：", shuffle, "\n", "比例：[训练集：验证集：测试集] = ", [train_idx,valid_idx-train_idx,len(image)-valid_idx])
    train = image[:train_idx]
    valid = image[train_idx:valid_idx]
    test = image[valid_idx:]

    # train.txt
    file0 = open(train_path, 'w')
    for i in train:
        file0.write(image_path + "/" + i + " " + label_path + "/" + i.replace("jpg", "") + "xml\n")
    file0.close()
    print(" 已保存训练集至%s" % train_path)

    # valid.txt
    file1 = open(valid_path, 'w')
    for i in valid:
        file1.write(image_path + "/" + i + " " + label_path + "/" + i.replace("jpg", "") + "xml\n")
    file1.close()
    print(" 已保存验证集至%s" % valid_path)

    # test.txt
    file2 = open(test_path, 'w')
    for i in test:
        file2.write(image_path + "/" + i + " " + label_path + "/" + i.replace("jpg", "") + "xml\n")
    file2.close()
    print(" 已保存测试集至%s" % test_path)
    print(" 注：本程序用于paddle detection及类似的划分。")


if __name__ == "__main__":
    main()
