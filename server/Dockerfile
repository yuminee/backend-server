FROM python:3.8-slim

LABEL email="ayuminee2@gmail.com"
LABEL name="Youmin Park"

WORKDIR /server

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]