# Test tool for Gateway Service of DevIot platform
There are test tool for test gateway service.

* poster is used to post action to DevIoT Gateway Service with MQTT protocol, it can send action command to your gateway service to check if you gateway service is work
* receiver is used to receive data from DevIoT Gateway Service with MQTT protocol, it can help you check all the data sent by your gateway service

##Prerequisite
1.[Python2.7](https://www.python.org/downloads/):This sdk base on the Python 2.7.10

2.paho-mqtt:It is a MQTT client implementation for Python, typing follow command to install it on you pc:
    
        sudo pip install paho-mqtt

##How to use
Use terminate window and navigate to the folder of this file, typing follow command:
poster tool:
        
        python poster                #it will use the default mqtt server : mqtt.cisco.com:7777
or
        
        python poster [mqtt server]
        
receiver tool:

        python receiver                #it will use the default mqtt server : mqtt.cisco.com:7777
or
        
        python receiver [mqtt server]
     
when the poster run, it wil ask you for action command, the command should follow blow json format:

    {"name":"sensorid", "action":"action name", "other action parameter":"parameter value" ...}
    
this action parameter should follow you sensor action property, here is a sample for buzzer sensor:
    
    {"name":"buzzer_a", "action":"on", "duration": 5,"interval": 1}
    
    
## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker
