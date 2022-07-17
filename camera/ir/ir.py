from flask import Flask
import RPi.GPIO as GPIO
import os

PWMLed = 13
state = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMLed,GPIO.OUT)

breath = GPIO.PWM(PWMLed, 1000)
breath.start(0)
breath.ChangeDutyCycle(state)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/state")
def getState():
  global state
  return {
    'message': 'Current PWM setting of IR LEDs',
    'state': state
  }

@app.route("/state/<int:level>")
def setState(level):
  global state
  state = level
  breath.ChangeDutyCycle(state)
  return {
    'message': 'Updated PWM setting of IR LEDs',
    'state': state
  }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)