FROM python:3.9-slim

ADD /requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN groupadd -g 61000 app
RUN useradd -g 61000 -l -m -s /bin/false -u 61000 app
USER app

EXPOSE 8000

ADD /app app

WORKDIR /app

CMD ["python3", "app.py"]