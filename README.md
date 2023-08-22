# HexoAssistant
Hexo Assistant————博客便捷上传助手
## 关于如何使用？
- 首先将本仓库克隆到本地。
```
git clone https://github.com/mstifiy/HexoAssistant.git
```
- 安装python相关依赖库。
```
PyQt5
requests
```
- 在源文件目录下新建config.ini文件，按照以下模板编写。
```
;Hexo Assistant Config File
[PATH]
post_path = <blog文章存放路径>
index_path = <blog文章图片存放路径>
hexo_path = <hexo文件夹路径>

[Gitee]
token = <Gitee私人令牌>
owner = <图床仓库所有者>
repo = <图床仓库名>
```
- 运行main.py，进入软件界面。
- Hexo Assistant的使用流程介绍完毕啦~
