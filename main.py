import os
import shutil
import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from UI_MainWindow import Ui_Form

__appname__ = 'Hexo Assistant'
__version__ = '1.0'


class Worker(QtCore.QThread, QtCore.QObject):  # 自定义信号，执行run()函数时，从线程发射此信号
    def __init__(self, obj, parent = None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.obj = obj

    def run(self):
        self.obj.uploadBtn.setEnabled(False)  # 设置上传按钮不可用
        self.obj.uploadFile_thread()
        self.obj.uploadBtn.setEnabled(True)


class HexoAssistantWin(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(HexoAssistantWin, self).__init__(parent)
        self.setupUi(self)
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setSizeGripEnabled(False)  # 屏蔽右下角有伸缩功能的小三角形
        self.statusBar.setStyleSheet("color:#f187b8;font-size:7pt;font-weight:bold")
        self.verticalLayout.addWidget(self.statusBar)
        self.setAcceptDrops(True)  # 设置接受拖拽
        self.thread_upload = Worker(self, None)  # 设置上传线程，防止程序假死
        self.setWindowTitle('{} - v{}'.format(__appname__, __version__))
        # self.setWindowIcon(QtGui.QIcon('source/icon/app_logo.png'))
        # 文章信息
        self.file_info = {'path': '',
                          'title': '',
                          'date': '',
                          'tags': [],
                          'categories': [],
                          'index_img': '',
                          'excerpt': '',
                          'imgBed': False}
        # 加载配置文件
        self.load_settings()

    def load_settings(self):
        try:
            self.settings = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
            self.post_path = self.settings.value('PATH/post_path')  # blog文章存放路径
            self.index_path = self.settings.value('PATH/index_path')  # blog封面图片存放路径
            self.hexo_path = self.settings.value('PATH/hexo_path')  # hexo路径
        except Exception:
            self.statusBar.showMessage('配置文件加载出错，请检查config.ini文件！', 3000)

    def parse_md(self, filename):
        # 显示路径
        self.lineEdit.setText(filename)
        self.file_info['path'] = filename
        # 显示标题，默认为文件名
        title = os.path.basename(filename).replace('.md', '')
        self.title_lineEdit.setText(title)
        self.file_info['title'] = title
        # 显示日期，默认为文件最后一次修改时间
        t = os.path.getmtime(filename)
        timeStruce = time.localtime(t)
        date = time.strftime('%Y-%m-%d %H:%M:%S', timeStruce)
        self.date_lineEdit.setText(date)
        self.file_info['date'] = date

    def copyImg(self, srcfile):
        if not os.path.isfile(srcfile):
            self.statusBar.showMessage('没有找到封面哦，要不检查一下路径吧~', 2000)
            # print("%s not exist!" % srcfile)
            return None
        else:
            fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
            dstfile = os.path.join(self.index_path, fname)
            if not os.path.exists(fpath):
                os.makedirs(fpath)  # 创建路径
            shutil.copyfile(srcfile, dstfile)  # 复制文件
            # print("copy %s -> %s" % (srcfile, dstfile))
            return f'/img/{fname}'  # 返回相对路径

    def loadFile(self):
        filename, _type = QtWidgets.QFileDialog.getOpenFileName(self, "打开文章", "./", "Md(*.md)")
        if filename:
            if filename.endswith('.md'):  # 读取文章信息
                self.parse_md(filename)
            else:
                print("不支持文件格式！")
        self.statusBar.showMessage('文章加载成功！', 3000)

    def uploadFile(self):
        # 获取文章信息
        self.file_info['path'] = self.lineEdit.text()
        self.file_info['title'] = self.title_lineEdit.text()
        self.file_info['date'] = self.date_lineEdit.text()
        self.file_info['tags'] = self.tags_lineEdit.text().split(' ')  # 空格隔开
        self.file_info['categories'] = self.categories_lineEdit.text().split(' ')
        self.file_info['index_img'] = self.indexImg_lineEdit.text()
        self.file_info['excerpt'] = self.excerpt_lineEdit.text()
        self.file_info['imgBed'] = self.imgBed_checkBox.isChecked()
        if self.file_info['path'] == '':
            self.statusBar.showMessage('请先加载文章哦~', 2000)
            return
        # self.parse_md(self.file_info['path'])
        self.statusBar.showMessage('正在努力上传中，不要乱点，嗯哼...', 0)
        # 修改追加文章信息
        if self.file_info['imgBed']:
            self.change_pic_path()  # 图片上传图床
        with open(self.file_info['path'], "r+", encoding = "utf-8") as f:
            txt = str(f.read())
            hexo_title = f'---\n'
            for key, val in self.file_info.items():
                if val != '' and val != [''] and key != 'imgBed':
                    if key == 'index_img':
                        relative_path = self.copyImg(val)  # 复制文件
                        if relative_path:
                            hexo_title += f'{key}: {relative_path}\n'
                        continue
                    hexo_title += f'{key}: {val}\n'
            hexo_title += f'---\n'
            content = hexo_title + txt
        with open(os.path.join(self.post_path, self.file_info['title'] + '.md'), 'w', encoding = "utf-8") as f:
            f.write(content)
        # 启用多线程
        self.thread_upload.start()

    def uploadFile_thread(self):
        # hexo本地文章上传github
        import subprocess
        cmd = 'hexo g' + "&&" + 'hexo d'
        # cmd = 'hexo clean' + "&&" + 'hexo g' + "&&" + 'hexo d'
        p = subprocess.Popen(cmd, shell = True, cwd = self.hexo_path, stdout = subprocess.PIPE)
        print(p.stdout.read().decode('utf-8'))  # 打印命令行输出信息
        self.statusBar.showMessage('文章上传成功！', 3000)

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:  # 拖动进入事件
        if a0.mimeData().hasUrls():
            a0.acceptProposedAction()
        else:
            a0.ignore()

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:  # 放下事件
        mimeData = a0.mimeData()
        if mimeData.hasUrls():
            urlList = mimeData.urls()
            filename = urlList[0].toLocalFile()
            if filename:
                # 获取文章或图片
                _, suffix = os.path.splitext(filename)
                if suffix == '.md':  # 文章加载
                    self.parse_md(filename)
                elif suffix == '.png' or suffix == '.jpg':  # 封面图片
                    self.indexImg_lineEdit.setText(filename)
                    self.file_info['index_img'] = filename
                else:
                    self.statusBar.showMessage('不支持拖放文件类型！', 2000)

    def change_pic_path(self):
        import re
        print("please wait a moment")
        try:
            with open(self.file_info['path'], 'r', encoding = 'utf-8') as md:
                article_content = md.read()
                pic_block = re.findall(r'\!.*?\)', article_content)  # 获取添加图片的Markdown文本
                for i in range(len(pic_block)):
                    pic_origin_url = re.findall(r'\((.*?)\)', pic_block[i])  # 获取插入图片时图片的位置
                    pic_new_url = self.upload_gitee(pic_origin_url[0])  # 上传得到gitee图片链接
                    print("pic_new_url is {}".format(pic_new_url))
                    article_content = article_content.replace(pic_origin_url[0], pic_new_url)
            # 替换原md文件中的图片链接
            with open(self.file_info['path'], 'w', encoding = 'utf-8') as md:
                md.write(article_content)
            print("job done")
        except BaseException as err:
            print("error in change_pic_path\n{}".format(err))

    def upload_gitee(self, pic_origin_url):  # 上传至Gitee
        if not os.path.exists(pic_origin_url):
            return pic_origin_url
        import base64
        import hashlib
        import datetime
        import requests
        try:
            token = self.settings.value('Gitee/token')
            owner = self.settings.value('Gitee/owner')
            repo = self.settings.value('Gitee/repo')
        except Exception:
            self.statusBar.showMessage('图片上传错误，请检查Gitee图床配置！', 2000)
            return
        message = 'upload image'
        mdname = ''
        with open(pic_origin_url, "rb") as f:
            content = base64.b64encode(f.read())
            data = {'access_token': token, 'message': message, 'content': content}

            filename = hashlib.md5(content).hexdigest() + pic_origin_url[pic_origin_url.rfind('.'):]
            path = 'typora/' + (mdname if mdname != '' else str(datetime.date.today())) + '/' + filename
            res = requests.post('https://gitee.com/api/v5/repos/' + owner + '/' + repo + '/contents/' + path, data)
            if res.status_code == 201 or res.text == '{"message":"文件名已存在"}':
                # print('https://gitee.com/' + owner + '/' + repo + '/raw/master/' + path)
                return 'https://gitee.com/' + owner + '/' + repo + '/raw/master/' + path
            else:
                print('Error uploading Gitee, please check')
                return None


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName('mstifiy')
    win = HexoAssistantWin()
    win.show()
    app.exec_()
