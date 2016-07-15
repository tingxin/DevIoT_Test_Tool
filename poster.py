__author__ = 'tingxxu'

import paho.mqtt.client as mqtt
import sys
import json


class MQClient:

    def __init__(self, action_topic):
        self.__sender = mqtt.Client()

        self.__sender.on_connect = self.__on_connect
        self.__sender.on_message = self.__on_message

        self.__action_topic = action_topic

    def __on_connect(self, client, userdata, flags, rc):
        self.__sender.subscribe(self.__action_topic)

    # The callback for when a PUBLISH message is received from the server.
    def __on_message(self, client, userdata, msg):
        pass

    def run(self, server_host, server_port):
        self.__sender.connect(server_host, server_port, 60)
        self.__sender.loop_start()
        while True:
            data = None

            while data is None:
                try:
                    str_action = raw_input("--Please input your action:\n")
                    data = json.loads(str_action)
                except:
                    print("input is error %s" % sys.exc_info()[0])
                    data = None
            self.__sender.publish(self.__action_topic, str_action)

if __name__ == '__main__':
    host = "10.140.92.25:1883"
    try:
        if len(sys.argv) > 1:
            host = str(sys.argv[1])
    except:
        print("mqtt host are needed!")

    account = raw_input("--Please input DevIot email account(someone@domain.com):\n")
    gateway_name = raw_input("--Please input gateway service account:\n")
    topic = "{0:s}-{1:s}-action".format(gateway_name, account)
    host_server = ""
    host_port = 0

    try:
        host_info = host.split(":")
        host_server = host_info[0]
        host_port = int(host_info[1])
    except:
        print("mqtt host should be with the format: ip:port")

    print("listen the host %s and communication with topic: %s" % (host, topic))

    if len(host_server) > 0 and host_port > 0 and len(topic) > 0:
        sender = MQClient(topic)
        sender.run(host_server, host_port)

