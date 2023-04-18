FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5053

ENV NAME Multiplication

CMD ["python", "app.py"]


