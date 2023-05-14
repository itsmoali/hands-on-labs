import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time


def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

# Mqtt broker
mqttBroker ="mqtt.eclipseprojects.io" 

# Connecting User to broker
controls = mqtt.Client("User")
controls.connect(mqttBroker) 

#Connecting Robot to broker
robot_commands = mqtt.Client("Robot")
robot_commands.connect(mqttBroker)

# Publishing to the topic
controls.publish("Robot_Commands")

# Subscribing to the topic
robot_commands.subscribe("Robot_Commands")

# This is the function that runs when a message is received
robot_commands.on_message=on_message


robot_commands.loop_start()

while True:
    message = input('Enter your message: ')
    controls.publish("Robot_Commands", message)
    time.sleep(1)

    