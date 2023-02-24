import argparse
import time

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


def on_connect(client, userdata, flags, rc):
    print("connect with result code(rc): " + str(rc))
    print("Flags: " + str(flags) + "\n")
    client.subscribe(userdata)


def on_disconnect(client, userdata, rc):
    print("disconnected with result code(rc): " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print("Userdata: " + str(userdata) + "\n")


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def main():
    args, unkown = arg_parse()
    host = "mqtt.eclipseprojects.io"
    port = 1883
    keepalive = 60
    client_id = "1000" if args.disable_clean_session else None

    topic = ("Sensor/Temp", 1)

    client = mqtt.Client(client_id,
                         clean_session=not args.disable_clean_session)

    client.user_data_set(topic)

    client.on_message = on_message
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect

    print("Connecting to " + host + " port: " + str(port))
    client.connect(host, port, keepalive)

    client.loop_start()  # Free up main thread

    time.sleep(3)  # Give client time to connect and subscribe

    client.disconnect()

    publish_20_msgs(host, port, topic=topic)

    print("Connecting to " + host + " port: " + str(port))
    client.connect(host, port, keepalive)

    client.loop_start()

    time.sleep(3)


def publish_20_msgs(host, port, keepalive=60, topic=("Sensor/Temp", 1)):
    msgs = iter([(topic[0], f"Message: {i}", topic[1]) for i in range(0, 20)])
    publish.multiple(msgs, host, port, "", keepalive)  # Error can be ignored


def arg_parse() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--disable-clean-session', action='store_true', help="disable 'clean session' (sub + msgs not cleared when client disconnects)")

    return parser.parse_known_args()


if __name__ == "__main__":
    main()
