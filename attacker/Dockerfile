FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
RUN mkdir templates
COPY templates ./templates
RUN mkdir static
COPY static ./static

CMD [ "flask", "run", "--host=0.0.0.0" ]
