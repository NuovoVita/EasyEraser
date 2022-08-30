# EasyEraser

Linux 系统文件删除工具，为了方便非Linux用户删除特定文件使用。

## 环境

> Linux 或 MacOS
>
> Python 3.9

## 开发环境搭建

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 编译

```bash
python -m  PyQt5.uic.pyuic EasyEraser.ui -o EasyEraser.py
pyinstaller --clean -F -w -i xataxi-icon.ico Register4TaxiLicenseMain.py
```
