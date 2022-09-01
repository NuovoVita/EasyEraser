# EasyEraser

Linux 系统文件删除工具，为了方便非Linux用户删除特定文件使用。

## 环境

> Linux 或 MacOS
>
> Python 3.8

## 开发环境搭建

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 编译

```bash
python -m  PyQt5.uic.pyuic EasyEraser.ui -o EasyEraser.py
pyinstaller --clean -F -w -i static/EasyEraser.ico EasyEraserMain.py
```

## Docker 编译

```bash
docker image build -t easy-eraser .
docker run -d -p 8000:8000 --name http-server easy-eraser
# 使用浏览器打开对外开发的8000端口，编译结果文件在dist目录下
```

## Ubuntu 系统创建桌面图标

1. 将文件easy-eraser.desktop放入到/usr/share/applications目录下
2. 修改easy-eraser.desktop文件中的执行文件路径和图标路径

## Todo List

1. License 认证开发
2. 设置和帮助文档开发
3. 自动化部署成为系统Desktop应用
4. arm 运行OK，编译环境是BJ ssh lua@192.168.1.70:/opt/.audit 123文件；cd /opt && cp -b .audit audit.zip && unzip audit.zip Galax@8888

## FAQ

> -clean ：告诉pyinstaller删除缓存和临时文件
>
> -F ：告诉pyinstaller将打包的结果放在一个exe文件中，也就是说最终结果将只有一个exe文件，如果不使用这个参数，那么结果会是一个exe加很多依赖文件，不利于我们分发软件。
>
> -w ：告诉pyinstaller我们要生成的是一个窗口应用。
>
> -i ：为我们的应用指定一个图标，否则默认的话会使用python图标。
>
> 一般来说，这些参数就足够日常使用了，如果需要更深入的功能，比如加密等等，就需要阅读手册了。

## 参考

- [ARM架构安装PyQT5](https://blog.csdn.net/foreverey/article/details/121410672)
