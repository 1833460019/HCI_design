""" Qt 中线程
主线程负责界面刷新
子线程负责网络和文件操作

线程同步 
"""

import sys  
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


