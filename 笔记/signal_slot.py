""" 信号与槽
信号与槽是一种对象间通信机制，信号是发出者，槽是接收者

槽实际上就是一个函数，当信号发出时，槽就会被调用
"""

import sys  
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    # 声明一个信号 只能放在函数外面
    my_signal = pyqtSignal(str) # 信号的参数是 str 类型 发送字符串

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = [] # 用来存储历史消息
    
    def init_ui(self):
        self.resize(600, 600)

        self.setWindowTitle('信号与槽')

        # 创建一个整体布局器
        container = QVBoxLayout() # 垂直布局器

        self.msg = QLabel('')
        self.msg.resize(400, 0)
        # self.msg.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.msg.setWordWrap(True) # 自动换行
        self.msg.setAlignment(Qt.AlignTop) # 文本顶部对齐

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局器
        v_layout = QVBoxLayout()    
        v_layout.addWidget(scroll)

        # 创建水平布局器
        h_layout = QHBoxLayout()    
        # 创建一个按钮
        btn = QPushButton('开始检测', self)
        
        # 将按钮添加到水平布局器中
        h_layout.addWidget(btn)

        # 将垂直布局器和水平布局器添加到整体布局器中
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 给按钮绑定一个点击事件
        btn.clicked.connect(self.btn_clicked)

        # 给信号绑定一个槽
        self.my_signal.connect(self.show_msg)

        # 将整体布局器添加到窗口中
        self.setLayout(container)
        
    def show_msg(self, _msg):
        self.msg_history.append(_msg)
        self.msg.setText("\n".join(self.msg_history))
        self.msg.resize(400, len(self.msg_history) * 20)
        self.msg.repaint() # 重绘
    
    
    def btn_clicked(self):
        # 发射信号
        self.my_signal.emit('检测到有人进入') # 信号发射 相当于调用了槽函数
        # time.sleep(3)
        self.my_signal.emit('检测到有人离开')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

