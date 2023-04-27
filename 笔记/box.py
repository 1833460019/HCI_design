from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, QRadioButton

import sys

""" PyQT 四种布局

QBoxLayout      盒子布局
QGridLayout     网格布局
QFormLayout     表单布局
QStackedLayout  抽屉布局

"""

class MyWindow(QWidget):  # 继承
    def __init__(self):
        super().__init__() # 调用父类的构造函数(里面包含对 UI 控件的初始化)
        self.init_ui()

    def init_ui(self):
        self.resize(400, 300)

        # 布局器可以嵌套
        
        # 最外层，包含爱好和性别
        container = QVBoxLayout()  # 垂直布局


        # ---------- 创建第 1 个组 垂直布局 爱好 ----------
        hobby_box = QGroupBox("爱好")
        v_layout = QVBoxLayout()  # 垂直布局
        btn1 = QRadioButton('打篮球')
        btn2 = QRadioButton('打羽毛球')
        btn3 = QRadioButton('打乒乓球')

        # 将按钮添加到 v_layout 布局器中
        v_layout.addWidget(btn1)    
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        # 将 v_layout 布局器添加到 hobby_box 中
        hobby_box.setLayout(v_layout)


        # ---------- 创建第 2 个组 水平布局 性别 ----------
        gender_box = QGroupBox("性别")
        h_layout = QHBoxLayout()  # 水平布局
        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')

        # 将按钮添加到 h_layout 布局器中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        # 将 h_layout 布局器添加到 gender_box 中
        gender_box.setLayout(h_layout)

        # 将两个组添加到最外层容器中
        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        # 显示最外层容器
        self.setLayout(container)

        # # QVBoxLayout 垂直布局
        # layout = QHBoxLayout()  # 水平布局

        # btn1 = QPushButton('Button1')
        # layout.addWidget(btn1) # 在布局器中添加按钮
        # btn2 = QPushButton('Button2')
        # layout.addWidget(btn2)
        # btn3 = QPushButton('Button3')
        # layout.addWidget(btn3)

        # # 默认布局器中控件位置平均分配
        # # 添加伸缩量的位置对样式影响很大
        # # 某位置有弹簧，那个该位置用空白填充，其他逐渐往外挤
        # # 里面的参数代表比例，单个 addStretch 没意义
        # layout.addStretch() # 伸缩量 -- 弹簧

        # self.setLayout(layout)  # 设置布局


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    sys.exit(app.exec_())
    