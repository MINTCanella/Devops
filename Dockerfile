FROM python:3.9

RUN pip install flask

COPY app.py ./app.py
COPY templates ./templates

CMD ["python", "app.py"]