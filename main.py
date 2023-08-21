import os
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

    def loadFile(self):
        filename, _type = QtWidgets.QFileDialog.getOpenFileName(self, "打开文章", "./", "Md(*.md);;Txt (*.txt)")
        if filename:
            if filename.endswith('.md'):  # 读取文章信息
                # 显示路径
                # self.file_info['path'] = filename
                self.lineEdit.setText(filename)
                # 显示标题，默认为文件名
                title = os.path.basename(filename).replace('.md', '')
                # self.file_info['title'] = title
                self.title_lineEdit.setText(title)
                # 显示日期，默认为文件最后一次修改时间
                t = os.path.getmtime(filename)
                timeStruce = time.localtime(t)
                date = time.strftime('%Y-%m-%d %H:%M:%S', timeStruce)
                # self.file_info['date'] = date
                self.date_lineEdit.setText(date)
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

        # 修改追加文章信息
        with open(self.file_info['path'], "r+", encoding = "utf-8") as f:
            txt = str(f.read())
            hexo_title = f'---\n'
            for key, val in self.file_info.items():
                if val != '' and val != [''] and key != 'imgBed':
                    hexo_title += f'{key}: {val}\n'
            hexo_title += f'---\n'
            content = hexo_title + txt
        with open(os.path.join(self.post_path, self.file_info['title']+'.md'), 'w', encoding = "utf-8") as f:
            f.write(content)

        # hexo本地文章上传github
        import subprocess
        cmd = 'hexo clean' + "&&" + 'hexo g' + "&&" + 'hexo d'
        p = subprocess.Popen(cmd, shell = True, cwd = 'D:/blog/hexo', stdout = subprocess.PIPE)
        print(p.stdout.read().decode('utf-8'))  # 打印命令行输出信息
        self.statusBar.showMessage('文章上传成功！', 3000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName('mstifiy')
    win = HexoAssistantWin()
    win.show()
    app.exec_()
