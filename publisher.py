import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("connect rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


def main():
    host = "mqtt.eclipseprojects.io"
    port = 1883
    keepalive = 60

    topic = "CyberSec/IKT520"

    client = mqtt.Client()

    client.on_message = on_message
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_subscribe = on_subscribe

    print("Connecting to " + host + " port: " + str(port))
    client.connect(host, port, keepalive)

    client.loop_start()

    msg_txt = "Hello, World!"
    print("Publishing: "+msg_txt)
    infot = client.publish(topic, msg_txt)
    infot.wait_for_publish()

    client.disconnect()


if __name__ == "__main__":
    main()
