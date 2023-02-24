import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from random import randint


def on_connect(mqttc, obj, flags, rc):
    print("connect rc: " + str(rc))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def main():
    host = "mqtt.eclipseprojects.io"
    port = 1883
    keepalive = 60

    topic = "SensorTemp"

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_publish = on_publish

    print("Connecting to " + host + " port: " + str(port))
    client.connect(host, port, keepalive)

    client.loop_start()

    msg_txt = "Hello, World!"
    print("Publishing: "+msg_txt)
    infot = client.publish(topic, msg_txt, 1)
    infot.wait_for_publish()

    client.disconnect()

    publish_single_example(host, port, keepalive)
    publish_multi_example(host, port, keepalive)


def publish_single_example(host, port, keepalive=60):
    msgs = [
        (f"WildCardSingle/{randint(1000,9999)}", "Match", 1),
        ("WildCardSingle/", "Match", 1),
        ("WildCardSingle", "Not Match", 1),
        (f"WildCardSingle/{randint(1000,9999)}/blarg", "Not Match", 1)
    ]
    publish.multiple(msgs, host, port, "", keepalive)


def publish_multi_example(host, port, keepalive=60):
    msgs = [
        (f"WildCardMulti/{randint(1000,9999)}", "Match", 1),
        ("WildCardMulti/", "Match", 1),
        ("WildCardMulti", "Match", 1),
        (f"WildCardMulti/{randint(1000,9999)}/blarg", "Match", 1)
    ]
    publish.multiple(msgs, host, port, "", keepalive)


if __name__ == "__main__":
    main()
