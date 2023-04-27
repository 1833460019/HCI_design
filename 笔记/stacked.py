from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_stacked_layout()
        self.init_ui()
    
    def create_stacked_layout(self):
        """
        添加了两个要显示的界面
        相当于一个列表中有两个元素
        不过由于是堆栈布局，所以每次只能显示一个界面
        """
        # 创建一个堆叠布局
        self.stacked_layout = QStackedLayout()

        # 创建单独 Widget
        win1 = window1()
        win2 = window2()

        # 将两个窗口添加到堆叠布局中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)


    def init_ui(self):
        # 设置 Widget 宽高
        self.setFixedSize(300, 270)

        # 创建整体的布局器
        container = QVBoxLayout()

        # 创建一个要显示具体内容的子 Widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet('background-color: grey;')

        # 创建两个按钮
        btn1 = QPushButton('窗口 1')
        btn2 = QPushButton('窗口 2')

        # 给按钮绑定点击事件
        # 没有括号，只是绑定一个方法，而不是调用一个方法
        btn1.clicked.connect(self.show_win1)
        btn2.clicked.connect(self.show_win2)
        
        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)
        
        # 显示整体窗口
        self.setLayout(container)

    def show_win1(self):
        # 切换到第一个界面 stacked_layout 抽屉布局器的索引
        self.stacked_layout.setCurrentIndex(0)

    def show_win2(self):
        # 切换到第二个界面
        self.stacked_layout.setCurrentIndex(1)


class window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('用户名', self)


class window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('密码', self)


if __name__ == '__main__':
    print(123)
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec_())