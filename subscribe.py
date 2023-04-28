import paho.mqtt.client as mqtt

# define callback function
def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode()))

# create MQTT client and connect to broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)

# subscribe to a topic
client.subscribe("NCUEMQTT")

# set callback function
client.on_message = on_message

# start the loop to listen for messages
client.loop_forever()
