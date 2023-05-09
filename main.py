from MQTT.MQTTUnit import MQTTUnit

if __name__ == '__main__':
    runner = MQTTUnit(input("user name: "))
    runner.run()
    print("ok")


