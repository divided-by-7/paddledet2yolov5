# xml2txt
本程序主要功能：

（1）若只想划分Paddle Detection支持的训练集、测试集、验证集，请阅读使用方法1、3
（2）若想将数据转化为ultralytics.yolov5支持的数据格式，请阅读使用方法1、2、3、4

使用方法：

1、假如您已存在一个文件夹同时包含.xml文件和.jpg等图片，您可以执行<b>拆分images和annotations_step1.py</b>程序，程序默认会将名为“all_data”文件夹下的图片和xml文件拆分至“images”和“annotations”文件夹

2、假如您已存在“images”和“annotations”文件夹，您可以执行<b>xml2txt_step2.py</b>程序，请确保在当前目录下存在“label_list.txt”，该文件为目标检测所包含的每个类名，以回车间隔；当您执行完程序会在当前目录下生成“label_txt”文件夹，存放yolov5支持的txt标签

3、划分paddle detection支持格式的训练集、测试集、验证集，请执行<b>划分数据集_step3.py</b>程序,将生成train.txt，label.txt，test.txt，分别包含三个集的路径。

4、划分ultralytics.yolov5支持的训练集、测试集、验证集，请先执行<b>划分数据集_step3.py</b>程序，再执行“划分yolo格式数据集_step4.py”，保存至Dataset文件夹。
