import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QFileDialog

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 设置支持高分辨率屏幕自适应


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(250, 281))
        Form.setMaximumSize(QtCore.QSize(500, 281))
        Form.setStyleSheet("")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("#frame{\n"
                                 "    border-image: url(:/bg/source/img/bg_1.jpg);\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font-size: 10pt;\n"
                                 "    border-radius: 1px;\n"
                                 "    background-color: rgba(241,135, 184, 130);\n"
                                 "    color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 "\n"
                                 "/* === QPushButton === */\n"
                                 "QPushButton {\n"
                                 "    border: 1px solid #333333;\n"
                                 "    padding: 4px;\n"
                                 "    min-width: 65px;\n"
                                 "    min-height: 12px;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #f187b8;\n"
                                 "    border-color: #333333;\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: white;\n"
                                 "    border-color: #333333;\n"
                                 "    color: #f187b8;\n"
                                 "}\n"
                                 "QPushButton:disabled {\n"
                                 "    color: #333333;\n"
                                 "}\n"
                                 "\n"
                                 "/* === QCheckBox === */\n"
                                 "QCheckBox\n"
                                 "{\n"
                                 "    background-color: rgba(241,135, 184, 130);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked\n"
                                 "{\n"
                                 "    border: 1px solid #333333;\n"
                                 "    width: 16px;\n"
                                 "    height: 16px;\n"
                                 "    background-color: white;\n"
                                 "}\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    border: 1px solid #333333;\n"
                                 "    width: 16px;\n"
                                 "    height: 16px;\n"
                                 "    background-color: #f187b8;\n"
                                 "}\n"
                                 "\n"
                                 "/* ===QLineEdit=== */\n"
                                 "QLineEdit{\n"
                                 "    padding-left:2px;\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "    border: 1px solid #333333;\n"
                                 "    border-radius: 1px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadBtn = QtWidgets.QPushButton(self.frame)
        self.loadBtn.setObjectName("loadBtn")
        self.verticalLayout.addWidget(self.loadBtn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.title_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.horizontalLayout_2.addWidget(self.title_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.date_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.horizontalLayout_3.addWidget(self.date_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.tags_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.tags_lineEdit.setObjectName("tags_lineEdit")
        self.horizontalLayout_5.addWidget(self.tags_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.categories_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.categories_lineEdit.setObjectName("categories_lineEdit")
        self.horizontalLayout_6.addWidget(self.categories_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.indexImg_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.indexImg_lineEdit.setObjectName("indexImg_lineEdit")
        self.horizontalLayout_4.addWidget(self.indexImg_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.excerpt_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.excerpt_lineEdit.setObjectName("excerpt_lineEdit")
        self.horizontalLayout_7.addWidget(self.excerpt_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.imgBed_checkBox = QtWidgets.QCheckBox(self.frame)
        self.imgBed_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.imgBed_checkBox.setTristate(False)
        self.imgBed_checkBox.setObjectName("imgBed_checkBox")
        self.verticalLayout.addWidget(self.imgBed_checkBox, 0, QtCore.Qt.AlignRight)
        self.uploadBtn = QtWidgets.QPushButton(self.frame)
        self.uploadBtn.setObjectName("uploadBtn")
        self.verticalLayout.addWidget(self.uploadBtn)
        self.imgBed_checkBox.raise_()
        self.loadBtn.raise_()
        self.uploadBtn.raise_()
        self.horizontalLayout_8.addWidget(self.frame)

        # 信号和槽函数
        self.loadBtn.clicked.connect(self.loadFile)  # 设置绑定事件
        self.uploadBtn.clicked.connect(self.uploadFile)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hexo Assistant"))
        self.loadBtn.setText(_translate("Form", "选择文章"))
        self.label.setText(_translate("Form", "路径："))
        self.label_2.setText(_translate("Form", "标题："))
        self.label_3.setText(_translate("Form", "日期："))
        self.label_5.setText(_translate("Form", "标签："))
        self.label_6.setText(_translate("Form", "分类："))
        self.label_4.setText(_translate("Form", "封面："))
        self.label_7.setText(_translate("Form", "摘要："))
        self.imgBed_checkBox.setText(_translate("Form", "图片上传图床"))
        self.uploadBtn.setText(_translate("Form", "上传博客"))


import images_rc
