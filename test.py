import os
import time

source_path = r"D:\mstifiynotes"  # .md files path
target_path = r"D:\blog\hexo\source\_posts"  # hexo source\_posts path
tags = '学习记录'  # 批量修改的文章标签

for root, dirs, files in os.walk(source_path, topdown = False):
    for name in files:
        _path = os.path.join(root, name)
        _name = name[:len(name) - 3]
        if str.lower(name[-3:]) != '.md':
            continue
        # 获取文件最后一次修改时间
        t = os.path.getmtime(_path)
        timeStruce = time.localtime(t)
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', timeStruce)

        with open(_path, "r+", encoding = "utf-8") as f:
            txt = str(f.read())
            hexo_title = f"---\ntitle: {_name}\ndate: {mtime}\ntags: {tags}\n---\n"
            txt = hexo_title + txt

        with open(os.path.join(target_path, name), 'a', encoding = "utf-8") as f:
            f.write(txt)