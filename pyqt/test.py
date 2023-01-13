import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QFormLayout, QSplitter, QHBoxLayout, QFrame
from PyQt5.QtCore import *


class MyWindow(QWidget):

    def __init__(self):  # self 就是一个实例对象
        super().__init__()  # 子类的方法调用父类的方法进行初始化

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Splitter')

        self.layout_splitter()

    def layout_splitter(self):

        # 实例化QFrame控件 相当于做了两个容器
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)

        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)

        textedit = QTextEdit()

        # 实例化QSplitter控件并设置初始为水平方向布局 水平拖动的布局
        splitter1 = QSplitter(Qt.Horizontal)

        # 向Splitter内添加控件。并设置游戏的初始大小
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        # 实例化Splitter管理器，添加控件到其中，设置垂直方向的布局
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        # splitter2.addWidget(bottom)

        # 设置全局布局为水平布局 设置窗体全局布局以及子布局的添加
        hbox = QHBoxLayout()
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用对象
    window = MyWindow()  # 创建MyWindow实例
    window.show()   # 展示窗口
    sys.exit(app.exec_())  # 进入主程序循环 并安全退出
