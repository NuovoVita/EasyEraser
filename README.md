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
```

## 参考

- [ARM架构安装PyQT5](https://blog.csdn.net/foreverey/article/details/121410672)
