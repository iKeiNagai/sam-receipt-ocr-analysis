# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install pip requirements
COPY docker/requirements.txt .
RUN python -m pip install -r requirements.txt


COPY notebook /app/notebook

COPY xraw-data/items-receipts/01.png /app/xraw-data/items-receipts/01.png

EXPOSE 8888

CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root" ]



