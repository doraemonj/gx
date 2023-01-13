import sys  # 系统参数操作
from PyQt5.QtWidgets import *  # 模块包含创造经典桌面风格的用户界面提供了一套UI元素的类
from PyQt5.QtCore import *  # 此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程
from PyQt5.QtGui import *  # 含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dongchedi.scarpy_car import dongchedi
from scrapy_baidu.scrapy_toutiao.fashion import news_fashion
from scrapy_baidu.scrapy_toutiao.food import news_food
from scrapy_baidu.scrapy_toutiao.military import news_military
from scrapy_baidu.scrapy_toutiao.n_game import news_game
from scrapy_baidu.scrapy_toutiao.n_hot import news_hot
from scrapy_baidu.scrapy_toutiao.n_tiyu import news_tiyu
from scrapy_baidu.scrapy_toutiao.n_world import news_world
from scrapy_baidu.scrapy_toutiao.n_yangsheng import news_regimen
from scrapy_baidu.scrapy_toutiao.n_yule import news_yule
from scrapy_baidu.scrapy_toutiao.news_finance import news_finance
from scrapy_baidu.scrapy_toutiao.all_detail import download_detail
from scrapy_baidu.scrapy_toutiao.tech import news_tech
from scrapy_baidu.scrapy_toutiao.travel import news_travel
from scrapy_baidu.scrapy_toutiao.weiboluntan import weiboluntan
from scrapy_baidu.scrapy_toutiao.weibomeinv import weibomeinv
from scrapy_baidu.scrapy_toutiao.weiboshuaige import weiboshuaige
from scrapy_video.xigua_detail import xigua_detail
from scrapy_video.xigua_srcapy import xigua_video
from scrapy_weibo.dongman import weibodongman
from scrapy_weibo.weibomeishi import weibomeishi
from scrapy_weibo.weibomeizhuang import weibomeizhuang
from scrapy_weibo.weiboqinggan import weiboqinggan
from scrapy_weibo.weiboxingzuo import weiboxingzuo


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(380, 154)
        Form.resize(1000, 800)
        self.allcheckBox = QtWidgets.QRadioButton(Form)
        self.allcheckBox.setGeometry(QtCore.QRect(50, 40, 1171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.allcheckBox.setFont(font)
        self.allcheckBox.setObjectName("allcheckBox")

        self.financecheckBox = QtWidgets.QRadioButton(Form)
        self.financecheckBox.setGeometry(QtCore.QRect(240, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.financecheckBox.setFont(font)
        self.financecheckBox.setObjectName("financecheckBox")

        self.dongmancheckBox = QtWidgets.QRadioButton(Form)
        self.dongmancheckBox.setGeometry(QtCore.QRect(440, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dongmancheckBox.setFont(font)
        self.dongmancheckBox.setObjectName("weibodongmancheckBox")

        self.dongchedicheckBox = QtWidgets.QRadioButton(Form)
        self.dongchedicheckBox.setGeometry(QtCore.QRect(640, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dongchedicheckBox.setFont(font)
        self.dongchedicheckBox.setObjectName("dongchedicheckBox")


        self.meinvcheckBox = QtWidgets.QRadioButton(Form)
        self.meinvcheckBox.setGeometry(QtCore.QRect(440, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.meinvcheckBox.setFont(font)
        self.meinvcheckBox.setObjectName("weibomeinvcheckBox")

        self.shuaigecheckBox = QtWidgets.QRadioButton(Form)
        self.shuaigecheckBox.setGeometry(QtCore.QRect(440, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.shuaigecheckBox.setFont(font)
        self.shuaigecheckBox.setObjectName("weiboshuaigecheckBox")


        self.weibomeishicheckBox = QtWidgets.QRadioButton(Form)
        self.weibomeishicheckBox.setGeometry(QtCore.QRect(440, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weibomeishicheckBox.setFont(font)
        self.weibomeishicheckBox.setObjectName("weibomeishicheckBox")

        self.weiboxingzuocheckBox = QtWidgets.QRadioButton(Form)
        self.weiboxingzuocheckBox.setGeometry(QtCore.QRect(440, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weiboxingzuocheckBox.setFont(font)
        self.weiboxingzuocheckBox.setObjectName("weiboxingzuocheckBox")

        self.weiboqinggancheckBox = QtWidgets.QRadioButton(Form)
        self.weiboqinggancheckBox.setGeometry(QtCore.QRect(440, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weiboqinggancheckBox.setFont(font)
        self.weiboqinggancheckBox.setObjectName("weiboqinggancheckBox")

        self.weibozhongcaocheckBox = QtWidgets.QRadioButton(Form)
        self.weibozhongcaocheckBox.setGeometry(QtCore.QRect(440, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weibozhongcaocheckBox.setFont(font)
        self.weibozhongcaocheckBox.setObjectName("weibozhongcaocheckBox")


        self.weiboluntancheckBox = QtWidgets.QRadioButton(Form)
        self.weiboluntancheckBox.setGeometry(QtCore.QRect(640, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weiboluntancheckBox.setFont(font)
        self.weiboluntancheckBox.setObjectName("weiboluntancheckBox")

        self.techcheckBox = QtWidgets.QRadioButton(Form)
        self.techcheckBox.setGeometry(QtCore.QRect(50, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.techcheckBox.setFont(font)
        self.techcheckBox.setObjectName("techcheckBox")

        self.worldcheckBox = QtWidgets.QRadioButton(Form)
        self.worldcheckBox.setGeometry(QtCore.QRect(240, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.worldcheckBox.setFont(font)
        self.worldcheckBox.setObjectName("worldcheckBox")

        self.sportscheckBox = QtWidgets.QRadioButton(Form)
        self.sportscheckBox.setGeometry(QtCore.QRect(50, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sportscheckBox.setFont(font)
        self.sportscheckBox.setObjectName("sportscheckBox")

        self.fashioncheckBox = QtWidgets.QRadioButton(Form)
        self.fashioncheckBox.setGeometry(QtCore.QRect(240, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fashioncheckBox.setFont(font)
        self.fashioncheckBox.setObjectName("fashioncheckBox")

        self.foodcheckBox = QtWidgets.QRadioButton(Form)
        self.foodcheckBox.setGeometry(QtCore.QRect(50, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.foodcheckBox.setFont(font)
        self.foodcheckBox.setObjectName("foodcheckBox")

        self.entertainmentcheckBox = QtWidgets.QRadioButton(Form)
        self.entertainmentcheckBox.setGeometry(QtCore.QRect(240, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entertainmentcheckBox.setFont(font)
        self.entertainmentcheckBox.setObjectName("entertainmentcheckBox")

        self.regimencheckBox = QtWidgets.QRadioButton(Form)
        self.regimencheckBox.setGeometry(QtCore.QRect(50, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.regimencheckBox.setFont(font)
        self.regimencheckBox.setObjectName("regimencheckBox")

        self.travelcheckBox = QtWidgets.QRadioButton(Form)
        self.travelcheckBox.setGeometry(QtCore.QRect(240, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.travelcheckBox.setFont(font)
        self.travelcheckBox.setObjectName("travelcheckBox")

        self.militarycheckBox = QtWidgets.QRadioButton(Form)
        self.militarycheckBox.setGeometry(QtCore.QRect(50, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.militarycheckBox.setFont(font)
        self.militarycheckBox.setObjectName("militarycheckBox")

        self.gamecheckBox = QtWidgets.QRadioButton(Form)
        self.gamecheckBox.setGeometry(QtCore.QRect(240, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gamecheckBox.setFont(font)
        self.gamecheckBox.setObjectName("gamecheckBox")
        #
        self.videocheckBox = QtWidgets.QRadioButton(Form)
        self.videocheckBox.setGeometry(QtCore.QRect(50, 320, 1171, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.videocheckBox.setFont(font)
        self.videocheckBox.setObjectName("videocheckBox")
        #
        # self.oumeivideocheckBox = QtWidgets.QRadioButton(Form)
        # self.oumeivideocheckBox.setGeometry(QtCore.QRect(50, 360, 1171, 35))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # self.oumeivideocheckBox.setFont(font)
        # self.oumeivideocheckBox.setObjectName("oumeivideocheckBox")

        # self.listView = QtWidgets.QListView(Form)
        # self.listView.setGeometry(QtCore.QRect(230, 40, 1171, 31))
        # self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setPlaceholderText("请输入预加载数量")
        self.lineEdit.setGeometry(QtCore.QRect(830, 40, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setObjectName("lineEdit")
        # self.pushButton = QtWidgets.QPushButton(Form)
        # self.pushButton.setGeometry(QtCore.QRect(230, 40, 1171, 31))
        # self.pushButton.setObjectName("pushButton")
        # self.retranslateUi(Form)
        # self.pushButton.clicked.connect(Form.add)
        # QtCore.QMetaObject.connectSlotsByName(Form)


        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(830, 80, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")


        self.downButton = QtWidgets.QPushButton(Form)
        self.downButton.setGeometry(QtCore.QRect(830, 120, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.downButton.setFont(font)
        self.downButton.setObjectName("downButton")


        self.downvideoButton = QtWidgets.QPushButton(Form)
        self.downvideoButton.setGeometry(QtCore.QRect(830, 160, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.downvideoButton.setFont(font)
        self.downvideoButton.setObjectName("downvideoButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "选择频道下载"))
        self.allcheckBox.setText(_translate("Form", "头条推荐")) #
        self.financecheckBox.setText(_translate("Form", "头条财经")) #
        self.dongmancheckBox.setText(_translate("Form", "微博动漫")) #
        self.meinvcheckBox.setText(_translate("Form", "微博美女")) #
        self.shuaigecheckBox.setText(_translate("Form", "微博帅哥")) #
        self.weibomeishicheckBox.setText(_translate("Form", "微博美食")) #
        self.weiboxingzuocheckBox.setText(_translate("Form", "微博星座")) #
        self.weiboqinggancheckBox.setText(_translate("Form", "微博情感")) #
        self.weibozhongcaocheckBox.setText(_translate("Form", "微博种草")) #
        self.weiboluntancheckBox.setText(_translate("Form", "微博论坛"))
        self.dongchedicheckBox.setText(_translate("Form", "懂车帝")) #
        self.techcheckBox.setText(_translate("Form", "头条科技")) #
        self.worldcheckBox.setText(_translate("Form", "头条国际")) #
        self.sportscheckBox.setText(_translate("Form", "头条体育")) #
        self.fashioncheckBox.setText(_translate("Form", "头条时尚")) #
        self.foodcheckBox.setText(_translate("Form", "头条美食")) #
        self.entertainmentcheckBox.setText(_translate("Form", "头条娱乐")) #
        self.regimencheckBox.setText(_translate("Form", "头条养生")) #
        self.travelcheckBox.setText(_translate("Form", "头条旅游")) #
        self.militarycheckBox.setText(_translate("Form", "头条军事")) #
        self.gamecheckBox.setText(_translate("Form", "头条游戏")) #
        self.videocheckBox.setText(_translate("Form", "西瓜短视频")) #
        # self.oumeivideocheckBox.setText(_translate("Form", "欧美视频"))

        # self.listView.setText(_translate("Form", "下载数量"))
        # self.lineEdit.setText(_translate("Form", ""))

        # self.pushButton.setText(_translate("Form", "下载数量"))

        self.okButton.setText(_translate("Form", "确定加载"))

        self.downButton.setText(_translate("Form", "头条下载"))
        self.downvideoButton.setText(_translate("Form", "视频下载"))

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.checkCheckBox)
        self.downButton.setEnabled(False)
        self.downvideoButton.setEnabled(False)
        self.downButton.clicked.connect(self.downButtonCheckBox)
        self.downvideoButton.clicked.connect(self.downvideoButtonCheckBox)
        self.weibo = False
        self.toutiao = False
        self.video = False

    def checkCheckBox(self):
        if self.lineEdit.text():
            # print(self.lineEdit.text())
            if self.allcheckBox.isChecked():
                news_hot(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'推荐频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.financecheckBox.isChecked():
                news_finance(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'财经频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.dongmancheckBox.isChecked():
                weibodongman(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博动漫频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.weibomeishicheckBox.isChecked():
                weibomeishi(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博美食频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.weiboxingzuocheckBox.isChecked():
                weiboxingzuo(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博星座频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.weiboqinggancheckBox.isChecked():
                weiboqinggan(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博情感频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.weibozhongcaocheckBox.isChecked():
                weibomeizhuang(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博美妆频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.meinvcheckBox.isChecked():
                weibomeinv(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博美女频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.shuaigecheckBox.isChecked():
                weiboshuaige(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博帅哥频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.weiboluntancheckBox.isChecked():
                weiboluntan(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'微博论坛频道已完成下载', QMessageBox.Close)
                # self.downButton.setEnabled(True)
                self.weibo = True
            if self.techcheckBox.isChecked():
                news_tech(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'科技频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.fashioncheckBox.isChecked():
                news_fashion(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'时尚频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.dongchedicheckBox.isChecked():
                dongchedi(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'懂车帝频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.worldcheckBox.isChecked():
                news_world(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'国际频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.sportscheckBox.isChecked():
                news_tiyu(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'体育频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.foodcheckBox.isChecked():
                news_food(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'美食频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.entertainmentcheckBox.isChecked():
                news_yule(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'娱乐频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.entertainmentcheckBox.isChecked():
                news_regimen(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'养生频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.travelcheckBox.isChecked():
                news_travel(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'旅游频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.militarycheckBox.isChecked():
                news_military(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'军事频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.gamecheckBox.isChecked():
                news_game(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'游戏频道已加载完成,等待下载', QMessageBox.Close)
                self.downButton.setEnabled(True)
                self.toutiao = True
            if self.videocheckBox.isChecked():
                xigua_video(self.lineEdit.text())
                QMessageBox.information(self, "消息框标题",'西瓜视频已加载完成,等待下载', QMessageBox.Close)
                self.downvideoButton.setEnabled(True)
                self.video = True


    def downButtonCheckBox(self):
        if self.toutiao:
            download_detail()

    def downvideoButtonCheckBox(self):
        if self.video:
            xigua_detail()

class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        '''
        构造函数，初始化登录对话框的内容
        :param args:
        :param kwargs:
        '''
        super().__init__(*args, **kwargs)
        self.setWindowTitle('欢迎登录')  # 设置标题
        self.resize(200, 200)  # 设置宽、高
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 设置隐藏关闭X的按钮

        '''
        定义界面控件设置
        '''
        self.frame = QFrame(self)  # 初始化 Frame对象
        self.verticalLayout = QVBoxLayout(self.frame)  # 设置横向布局
        self.verticalLayout

        self.login_id = QLineEdit()  # 定义用户名输入框
        self.login_id.setPlaceholderText("请输入登录账号")  # 设置默认显示的提示语
        self.verticalLayout.addWidget(self.login_id)  # 将该登录账户设置添加到页面控件

        self.passwd = QLineEdit()  # 定义密码输入框
        self.passwd.setPlaceholderText("请输入登录密码")  # 设置默认显示的提示语
        self.verticalLayout.addWidget(self.passwd)  # 将该登录密码设置添加到页面控件

        self.button_enter = QPushButton()  # 定义登录按钮
        self.button_enter.setText("登录")  # 按钮显示值为登录
        self.verticalLayout.addWidget(self.button_enter)  # 将按钮添加到页面控件

        self.button_quit = QPushButton()  # 定义返回按钮
        self.button_quit.setText("返回")  # 按钮显示值为返回
        self.verticalLayout.addWidget(self.button_quit)  # 将按钮添加到页面控件

        # 绑定按钮事件
        self.button_enter.clicked.connect(self.button_enter_verify)
        self.button_quit.clicked.connect(
            QCoreApplication.instance().quit)  # 返回按钮绑定到退出

    def button_enter_verify(self):
        # 校验账号是否正确
        # if self.login_id.text() != "crawler":
        if self.login_id.text() != "1":
            print("test1")
            return
        # 校验密码是否正确
        # if self.passwd.text() != "crawler88999@1234":
        if self.passwd.text() != "1":
            print("test2")
            return
        # 验证通过，设置QDialog对象状态为允许
        self.accept()

if __name__ == "__main__":
    # 创建应用
    window_application = QApplication(sys.argv)
    # 设置登录窗口
    login_ui = LoginDialog()
    # 校验是否验证通过
    if login_ui.exec_() == QDialog.Accepted:
        # 初始化主功能窗口
        main_window = MyMainForm()
        # 展示窗口
        main_window.show()
        # 设置应用退出
        sys.exit(window_application.exec_())