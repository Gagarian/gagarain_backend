FROM python:3
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ENV PYTHONPATH /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/