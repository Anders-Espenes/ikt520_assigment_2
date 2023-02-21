import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("connect with result code(rc): " + str(rc))
    client.subscribe(userdata)


def on_message(mqttc, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, userdata, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print("Userdata: " + str(obj))


def on_log(mqttc, userdata, level, string):
    print(string)


def main():
    host = "mqtt.eclipseprojects.io"
    port = 1883
    keepalive = 60

    topic = "CyberSec/IKT520"

    client = mqtt.Client()

    client.user_data_set(topic)

    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    print("Connecting to " + host + " port: " + str(port))
    client.connect(host, port, keepalive)

    client.loop_forever()


if __name__ == "__main__":
    main()