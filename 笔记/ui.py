import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget
from PyQt5.QtGui import QIcon

"""

最常用的功能模块

1. QtCore
包含了非GUI功能，如事件循环、时间、文件、线程、内存管理、数据类型和流等

2. QtGui
包含了窗口系统集成、图像、事件处理、2D/3D图形、字体和文本等功能

3. QtWidgets 控件
包含了常用的GUI元素，如窗口、按钮、标签、文本框、布局管理器等

# 左上角(0, 0)

横 x
竖 y

"""

if __name__ == '__main__':
    # sys.argv 是一个来自命令行的参数列表
    app = QApplication(sys.argv)

    # QWidget 窗口
    w = QWidget() 

    # 设置窗口标题
    w.setWindowTitle('Human Computer Interaction')

    # 设置窗口大小
    w.resize(400, 300)

    # 添加控件：按钮 
    # 同时将按钮添加到窗口中
    btn = QPushButton('Button', w)  # 出生就给一个父亲 （笑）
    # or btn.setParent(w)
    
    # 添加控件：纯文本
    label = QLabel('账号', w)

    # 设置标签的位置和大小 (x, y, w, h)
    label.setGeometry(50, 100, 200, 50)  # (x, y) 左上角坐标 绝对定位

    # 添加控件：输入框
    edit = QLineEdit(w)
    edit.setPlaceholderText('Input your name')
    edit.setGeometry(100, 100, 200, 50)

    # 显示在屏幕中间位置
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)

    """ 怎么利用官方文档？

    PyQt5.QtCore.QPoint(719, 462) 遇到一个新的类
    去 https://doc.qt.io/ 搜索 PyQt5.QtCore.QPoint
    
    QPoint 是一个类

    所有类：https://doc.qt.io/qt-5/classes.html

    """

    """ 学会利用搜索引擎

    PyQT + 功能点
    
    """
    x = center_pointer.x() # x = w.width() / 2
    y = center_pointer.y() # y = w.height() / 2
    # print(x, y)
    # w.move(x, y) # 不对，作用：把左上角移到中间 -> 我们想要的是把框的中心移到桌面的中间
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width // 2, y - height // 2)

    # 设置图标
    # w.setWindowIcon(QIcon('logo.png')) # mac 无法设置


    # 展示 QWidget
    w.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())