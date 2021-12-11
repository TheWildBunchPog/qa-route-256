FROM python:3.9-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app/app.py"]
