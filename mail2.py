import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QMessageBox, 
                             QPlainTextEdit)
from PyQt5.QtGui import QIcon


class Calculator(QWidget):  # QWidget을 상속받아 정의
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()  
        self.te1.setReadOnly(True)  

        # "Message" 버튼 생성 및 클릭 이벤트 연결
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)

        # "Clear" 버튼 생성 및 클릭 이벤트 연결
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)

        # 버튼들을 수평으로 배치
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        # 전체 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))  # 아이콘 파일 필요
        self.resize(256, 256)
        self.show()

    # "Message" 버튼 클릭 시 호출되는 함수
    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")

    # "Clear" 버튼 클릭 시 호출되는 함수
    def clearMessage(self):
        self.te1.clear()


# 메인 실행 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
