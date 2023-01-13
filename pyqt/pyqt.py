from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QRadioButton-单选框 - PyQt5中文网')
window.resize(600, 450)
window.move(300, 300)

btn1 = QRadioButton('推荐', window)
btn1.setIcon(QIcon('1.png'))
btn1.move(60, 60)
btn1.resize(80, 35)
btn1.setStyleSheet('background-color:green')

btn2 = QRadioButton('军事', window)
btn2.setIcon(QIcon('2.png'))
btn2.move(60, 120)
btn2.resize(80, 35)
btn2.setStyleSheet('background-color:green')

# ==============默认选择=============== # 代码分割线 - 开始
btn1.setChecked(True)
# ==============默认选择=============== # 代码分割线 - 结束

# ==============QRadioButton可用信号=============== # 代码分割线 - 开始
btn2.toggled.connect(lambda isChecked: print(isChecked))  # 切换信号
# 单选变多选
# btn2.setAutoExclusive(False)
# ==============QRadioButton可用信号=============== # 代码分割线 - 结束

window.show()
sys.exit(app.exec_())
