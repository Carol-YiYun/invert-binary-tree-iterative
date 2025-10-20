# syntax=docker/dockerfile:1
FROM python:3.13.7-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 有 requirements.txt 就裝；沒有就裝 pytest
COPY requirements.txt* ./
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; else pip install pytest; fi

# 複製程式碼
COPY . .

# 預設執行測試
CMD ["pytest", "-v"]

# 預設執行主程式
# CMD ["python", "source/main.py"]
