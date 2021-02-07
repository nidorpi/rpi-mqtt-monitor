#!/usr/bin/env python3

import random
import os
from time import sleep
from paho.mqtt import client as mqtt_client
from gpiozero import CPUTemperature, DiskUsage

cpu = CPUTemperature()
disk_usage = DiskUsage()

broker = os.getenv('MQTT_SERVER', '127.0.0.1')
port = os.getenv('MQTT_PORT', 1833)
hostname = os.getenv('HOSTNAME', 'raspberry')

client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, int(port))
    return client

def publish(client):
    client.publish(f"rpi-status/{hostname}/temp",f"{cpu.temperature}")
    client.publish(f"rpi-status/{hostname}/disk_usage",f"{int(disk_usage.value*100)}")


def run():
    client = connect_mqtt()
    while True:
        publish(client)
        sleep(60)

if __name__ == '__main__':
    run()
