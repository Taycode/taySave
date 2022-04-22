FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /main_server
COPY requirements.txt /main_server/
RUN pip install -r requirements.txt
COPY . /main_server/
