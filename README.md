# xml2txt
将paddledetection用的xml数据格式转化为yolov5用的txt格式

使用方法：
1、假如您已存在一个文件夹同时包含.xml文件和.jpg等图片，您可以执行<b>拆分images和annotations_step1.py</b>程序，程序默认会将名为“all_data”文件夹下的图片和xml文件拆分至“images”和“annotations”文件夹

2、假如您已存在“images”和“annotations”文件夹，您可以执行<b>xml2txt_step2.py</b>程序，请确保在当前目录下存在“label_list.txt”，该文件为目标检测所包含的每个类名，以回车间隔；当您执行完程序
