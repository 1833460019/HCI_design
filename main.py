import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import cv2

from my_detect import detect

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ''
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.timer_camera = QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流

        self.init_ui()
        self.init_slot()  # 初始化槽

    def init_ui(self):
        # 加载 Qt Designer 画的 ui 文件
        self.ui = uic.loadUi('./my_window.ui')
        print(self.ui.__dict__)
        self.button_start = self.ui.pushButton
        self.button_stop = self.ui.pushButton_2
        self.show_before = self.ui.label  # 原始图像
        self.show_after = self.ui.label_2  # 处理后的图像

    def init_slot(self):
        self.button_start.clicked.connect(
            self.button_open_camera_clicked)  # 若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera.timeout.connect(
            self.show_camera)  # 若定时器结束，则调用show_camera()

        # 若该按键被点击，则调用close()，注意这个close是父类QtWidgets.QWidget自带的，会关闭程序
        self.button_stop.clicked.connect(self.close_all)

    
    def close_all(self):
        """槽函数 关闭所有窗口"""
        QApplication.quit()

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:  # flag表示open()成不成功
                msg = QMessageBox.warning(
                    self, 'warning', "请检查相机于电脑是否连接正确", buttons=QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.button_start.setText('关闭相机')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.show_before.clear()  # 清空视频显示区域
            self.show_after.clear()  # 清空视频显示区域
            self.button_start.setText('打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取

        # 把读到的帧的大小重新设置为 400 x 400
        # print(self.image.shape) # (720, 1280, 3)
        print(self.image)
        show_before = cv2.resize(self.image, (400, 400))
        show_before = cv2.cvtColor(
            show_before, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage_before = QImage(show_before.data, show_before.shape[1], show_before.shape[0],
                                  QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        
        show_after = detect(self.image)
        # print(show_after.shape)  # (720, 1280, 3)
        print(show_after) 
        show_after = cv2.resize(show_after, (400, 400))
        show_after = cv2.cvtColor(
            show_after, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        showImage_after = QImage(show_after.data, show_after.shape[1], show_after.shape[0],
                                 QImage.Format_RGB888)

        self.show_before.setPixmap(
            QPixmap.fromImage(showImage_before))  # 往显示视频的Label里 显示QImage

        self.show_after.setPixmap(
            QPixmap.fromImage(showImage_after))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    # window.show()
    window.ui.show()
    sys.exit(app.exec_())
