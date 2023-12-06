FROM python:3.10.10-alpine

WORKDIR /opt/app

ADD ./requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
