#
# Created by Rui Santos
# Complete project details: https://randomnerdtutorials.com
#

import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

mqttc=mqtt.Client()
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {

   # STAND
   # FORWARD
   # BACK
   # LEFT
   # RIGHT
   # HAND_WAVE
   # BODY_DANCE
   # SIT
   1 : {'name' : 'STAND', 'board' : 'esp8266', 'topic' : 'esp8266/1', 'state' : 'False'},
   2 : {'name' : 'FORWARD', 'board' : 'esp8266', 'topic' : 'esp8266/2', 'state' : 'False'},
   3 : {'name' : 'BACK', 'board' : 'esp8266', 'topic' : 'esp8266/3', 'state' : 'False'},
   4 : {'name' : 'LEFT', 'board' : 'esp8266', 'topic' : 'esp8266/4', 'state' : 'False'},
   5 : {'name' : 'RIGHT', 'board' : 'esp8266', 'topic' : 'esp8266/5', 'state' : 'False'},
   6 : {'name' : 'HAND_WAVE', 'board' : 'esp8266', 'topic' : 'esp8266/6', 'state' : 'False'},
   7 : {'name' : 'BODY_DANCE', 'board' : 'esp8266', 'topic' : 'esp8266/7', 'state' : 'False'},
   8 : {'name' : 'SIT', 'board' : 'esp8266', 'topic' : 'esp8266/8', 'state' : 'False'},
   #9 : {'name' : 'BACK', 'board' : 'esp8266', 'topic' : 'esp8266/9', 'state' : 'False'},
}

# Put the pin dictionary into the template data dictionary:
templateData = {
   'pins' : pins
   }

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<board>/<changePin>/<action>")

def action(board, changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   devicePin = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "1" and board == 'esp8266':
      mqttc.publish(pins[changePin]['topic'],"1")
      pins[changePin]['state'] = 'True'

   if action == "0" and board == 'esp8266':
      mqttc.publish(pins[changePin]['topic'],"0")
      pins[changePin]['state'] = 'False'

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8181, debug=True)