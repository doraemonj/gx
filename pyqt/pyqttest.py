import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDateTime
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLineEdit
# 使用调色板等
from PyQt5.QtGui import QIcon


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(650, 400)  # 窗口大小
        self.setWindowTitle("主窗口")

        # 开始计数按钮
        start_button = QPushButton("开始计数", self)
        # 关联到计数函数
        # start_button.clicked.connect(self.start_calculation)
        start_button.clicked.connect(self.calculation)

        # 终止计数按钮
        stop_button = QPushButton("终止计数", self)
        stop_button.clicked.connect(self.stop_calculation)

        # 布局
        layout = QGridLayout()
        layout.addWidget(start_button, 1, 1)
        layout.addWidget(stop_button, 1, 2)
        self.setLayout(layout)

        # 子窗口对象是否存在
        self.childWindowExist = False  # 默认为不存在

    # 开始计数
    def start_calculation(self):
        print("开始计数")
        self.num = 0  # 初始计数

        self.timer = QTimer()
        self.timer.start(1000)  # 间隔1秒钟执行一次操作
        self.timer.timeout.connect(self.calculation)

    # 终止计数
    def stop_calculation(self):
        print("停止计数")
        self.num = 0
        self.timer.stop()
        if self.childWindowExist:
            self.child_window.close()
        self.childWindowExist = False

    # 计数函数
    def calculation(self):
        # 每次加1
        # self.num += 1
        # print("当前计数为{}".format(self.num))

        # if self.num % 10 == 0:
        self.childWindowExist = True
        # 如果能够整除10，则弹窗
        self.child_window = Child()
        # self.child_window.window_show("当前计数为{}".format(self.num))
        self.child_window.show()

# 创建一个子线程
class UpdateThread(QThread):
    # 创建一个信号，触发时传递当前时间给槽函数
    update_data = pyqtSignal(str)

    def run(self):
        # 无限循环，每秒钟传递一次时间给UI
        while True:
            for i in [111,222,333,444]:
                self.update_data.emit(str(i))
                time.sleep(1)


class Child(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 100)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(400, 100)

        # 创建子线程
        self.subThread = UpdateThread()
        # 将子线程中的信号与timeUpdate槽函数绑定
        self.subThread.update_data.connect(self.timeUpdate)
        # 启动子线程（开始更新时间）
        self.subThread.start()

        # 添加窗口标题
        self.setWindowTitle("SubThreadDemo")

    # 被子线程的信号触发，更新一次时间
    def timeUpdate(self, data):
        self.lineEdit.setText(data)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("images/icon.ico"))
#     # 创建一个主窗口
#     mainWin = DemoWin()
#     # 显示
#     mainWin.show()
#     # 主循环
#     sys.exit(app.exec_())


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())
