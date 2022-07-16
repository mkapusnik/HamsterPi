from flask import Flask
import RPi.GPIO as GPIO

PWMLed = 13
state = 0

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
  return {
    'message': 'Current PWM setting of IR LEDs',
    'state': state
  }

@app.route("/state/<int:level>")
def setState(level):
  state = level
  breath.ChangeDutyCycle(state)
  return {
    'message': 'Updated PWM setting of IR LEDs',
    'state': state
  }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)