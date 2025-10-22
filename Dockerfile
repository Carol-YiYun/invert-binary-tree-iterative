# 指定 Dockerfile 語法版本
# syntax=docker/dockerfile:1

# 基底映像：使用輕量版 Python 3.13.7（Debian slim）
FROM python:3.13.7-slim

# 設定容器內的工作目錄，之後的操作都以 /app 為基準
WORKDIR /app

# 設定環境變數：
# - PYTHONDONTWRITEBYTECODE=1 ：防止產生 .pyc 檔案，減少映像大小
# - PYTHONUNBUFFERED=1 ：讓 Python 輸出即時顯示，不經緩衝
# - PIP_NO_CACHE_DIR=1 ：安裝套件時不保留快取，節省空間
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 若有 requirements.txt 則安裝其中的套件；
# 若沒有，至少安裝 pytest 以便進行測試。
COPY requirements.txt* ./
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; else pip install pytest; fi

# 將專案全部複製進容器的 /app 目錄中
COPY . .

# 複製啟動腳本（entrypoint.sh）並賦予可執行權限
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# 設定容器啟動時的預設執行命令
# entrypoint.sh 會根據參數決定執行 pytest 或主程式
ENTRYPOINT ["./entrypoint.sh"]


