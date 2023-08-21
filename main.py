import os
import shutil
import sys
import time
from PyQt5 import QtWidgets, QtGui

from UI_MainWindow import Ui_Form

__appname__ = 'Hexo Assistant'
__version__ = '1.0'


class HexoAssistantWin(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent = None):
        super(HexoAssistantWin, self).__init__(parent)
        self.setupUi(self)
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setSizeGripEnabled(False)  # 屏蔽右下角有伸缩功能的小三角形
        self.statusBar.setStyleSheet("color:#f187b8;font-size:7pt;font-weight:bold")
        self.verticalLayout.addWidget(self.statusBar)
        self.setAcceptDrops(True)  # 设置接受拖拽
        self.setWindowTitle('{} - v{}'.format(__appname__, __version__))
        self.setWindowIcon(QtGui.QIcon('source/icon/app_logo.png'))
        # 文章信息
        self.file_info = {'path': '',
                          'title': '',
                          'date': '',
                          'tags': [],
                          'categories': [],
                          'index_img': '',
                          'excerpt': '',
                          'imgBed': False}
        # blog文章存放路径
        self.post_path = 'D:/blog/hexo/source/_posts'
        # blog封面图片存放路径
        self.index_path = 'D:/blog/hexo/source/img'

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
        if self.file_info['path'] == '':
            self.statusBar.showMessage('请先加载文章哦~', 2000)
            return

        # 获取文章信息
        self.file_info['path'] = self.lineEdit.text()
        self.file_info['title'] = self.title_lineEdit.text()
        self.file_info['date'] = self.date_lineEdit.text()
        self.file_info['tags'] = self.tags_lineEdit.text().split(' ')  # 空格隔开
        self.file_info['categories'] = self.categories_lineEdit.text().split(' ')
        self.file_info['index_img'] = self.indexImg_lineEdit.text()
        self.file_info['excerpt'] = self.excerpt_lineEdit.text()
        self.file_info['imgBed'] = self.imgBed_checkBox.isChecked()
        # self.parse_md(self.file_info['path'])

        # 修改追加文章信息
        with open(self.file_info['path'], "r+", encoding = "utf-8") as f:
            txt = str(f.read())
            hexo_title = f'---\n'
            for key, val in self.file_info.items():
                if val != '' and val != [''] and key != 'imgBed':
                    if key == 'index_img':
                        relative_path = self.copyImg(val)  # 复制文件
                        hexo_title += f'{key}: {relative_path}\n'
                        continue
                    hexo_title += f'{key}: {val}\n'
            hexo_title += f'---\n'
            content = hexo_title + txt
        with open(os.path.join(self.post_path, self.file_info['title'] + '.md'), 'w', encoding = "utf-8") as f:
            f.write(content)

        # hexo本地文章上传github
        import subprocess
        cmd = 'hexo clean' + "&&" + 'hexo g' + "&&" + 'hexo d'
        p = subprocess.Popen(cmd, shell = True, cwd = 'D:/blog/hexo', stdout = subprocess.PIPE)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName('mstifiy')
    win = HexoAssistantWin()
    win.show()
    app.exec_()
