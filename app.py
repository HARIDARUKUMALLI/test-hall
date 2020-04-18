import signal
import threading
#from gi.repository import GLib
#from pydbus import SessionBus
#from pydbus.generic import signal
from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

# Creating the context for Flask operations.
app = Flask(__name__)


#def my_callback(*args):
"""
        FUNCTION NAME : my_callback
        VERSION : 1.0
        AUTHOR(S) : 
            1) Version 1.0 : Srijan Sivakumar
        FUNCTIONALITY : 
            1) Version 1.0 : This function is the signal callback for the DBUS 
            signals.
"""
#    print ("Recieved signal from remote process")

def on_connect(client, userdata, flags, rc):
    global app
    print("Connected with result code "+str(rc))
    client.subscribe("srijan/sample/value")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


@app.route('/config_modbus', methods=['GET', 'POST', 'PUT', 'DELETE'])
def config_modbus_handler():
    """
        FUNCTION NAME : config_modbus_handler
        VERSION : 1.0
        AUTHOR(S) : 
            1) Version 1.0 : Srijan Sivakumar
        FUNCTIONALITY : 
            1) Version 1.0 : This function is binded with the route '/config_modbus'.
            for operations, GET, POST, PUT and DELETE.
    """
    global domain_object
    if request.method == 'POST':
        #reply = domain_object.configure("csv_string")
        method_value = 'POST'
    elif request.method == 'GET':
        reply = domain_object.configure("csv_string")
        #method_value = 'GET'
    elif request.method == 'PUT':
        reply = domain_object.configure("csv_string")
        #method_value = 'PUT'
    elif request.method == 'DELETE':
        reply = domain_object.configure("csv_string")
        #method_value = 'DELETE'
    reply = "SUCCESS"
    return jsonify({'function' : 'config', 'method' : method_value, 'response' : reply})

@app.route('/init_modbus', methods=['GET', 'POST', 'PUT', 'DELETE'])
def init_modbus_handler():
    """
        FUNCTION NAME : init_modbus_handler
        VERSION : 1.0
        AUTHOR(S) : 
            1) Version 1.0 : Srijan Sivakumar
        FUNCTIONALITY : 
            1) Version 1.0 : This function is binded with the route '/init_modbus'.
            for operations, GET, POST, PUT and DELETE.
    """
    global domain_object
    if request.method == 'POST':
        #reply = domain_object.configure("csv_string")
        method_value = 'POST'
    elif request.method == 'GET':
        #reply = domain_object.configure("csv_string")
        method_value = 'GET'
    elif request.method == 'PUT':
        #reply = domain_object.configure("csv_string")
        method_value = 'PUT'
    elif request.method == 'DELETE':
        #reply = domain_object.configure("csv_string")
        method_value = 'DELETE'
    reply = "SUCCESS"
    return jsonify({'function' : 'init', 'method' : method_value, 'response' : reply})

@app.route('/mapping_modbus', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mapping_modbus_handler():
    """
        FUNCTION NAME : mapping_modbus_handler
        VERSION : 1.0
        AUTHOR(S) : 
            1) Version 1.0 : Srijan Sivakumar
        FUNCTIONALITY : 
            1) Version 1.0 : This function is binded with the route '/mapping_modbus'.
            for operations, GET, POST, PUT and DELETE.
    """
    global domain_object
    if request.method == 'POST':
        #reply = domain_object.configure("csv_string")
        method_value = 'POST'
    elif request.method == 'GET':
        #reply = domain_object.configure("csv_string")
        method_value = 'GET'
    elif request.method == 'PUT':
        #reply = domain_object.configure("csv_string")
        method_value = 'PUT'
    elif request.method == 'DELETE':
        #reply = domain_object.configure("csv_string")
        method_value = 'DELETE'
    reply = "SUCCESS"
    return jsonify({'function' : 'mapping', 'method' : method_value, 'response' : reply})



#def init_event_loop(loop):
"""
        FUNCTION NAME : init_event_loop
        VERSION : 1.0
        AUTHOR(S) : 
            1) Version 1.0 : Srijan Sivakumar
        FUNCTIONALITY : 
            1) Version 1.0 : This function is invoked as a thread to start the G main loop.
    """
 #   loop.run()

"""
def signal_received(signalNumber, frame):
    global client
    client.loop_stop()
    return

# Adding singla handler.
#signal.signal(signal.SIGINT, signal_received)
"""

# Creating MQTT Client handle.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()

# Adding DBUS components
"""loop = GLib.MainLoop()
bus = SessionBus()
bus.subscribe(iface='Lnt.domain_services.Interface',signal='wifiSignal',object='/Lnt/domain_services/Object', signal_fired = my_callback)
domain_object = bus.get('Lnt.Ubiqsense.domain_services','/Lnt/domain_services/Object')

try:
    x = threading.Thread(target=init_event_loop, args=(loop,))
    x.start()
except:
    print("Thread creation failed.")
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
