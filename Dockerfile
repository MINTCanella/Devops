FROM python:3.9

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY app.py ./app.py
COPY templates ./templates

CMD ["python", "app.py"]