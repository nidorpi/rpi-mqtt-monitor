FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#ENV MQTT_SERVER=127.0.0.1
#ENV HOSTNAME=raspberry

COPY . .

CMD [ "python", "report_status.py"]
