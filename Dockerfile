FROM python:3.8-bullseye

WORKDIR /app

ADD . /app

RUN python -m pip install --upgrade pip -i https://pypi.douban.com/simple && \
    pip install -r requirements.txt -i https://pypi.douban.com/simple && \
    pyinstaller --clean -F -w -i static/EasyEraser.ico EasyEraserMain.py

EXPOSE 8000

CMD ["python3", "-m", "http.server", "8000"]
