from zeroconf import IPVersion, ServiceInfo, Zeroconf
from flask import Flask
import RPi.GPIO as GPIO
import socket
import os

# NSD init
server = socket.gethostname()
port = int(os.environ.get('PORT', 8555))
name = os.getenv('NAME', server.title())
desc = {'deviceName': name}
type = '_nanny._tcp.local.'

info = ServiceInfo(
    type,
    name + "." + type,
    port=port,
    properties=desc,
    server=server + ".local.",
)

zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
print("Registration of a service {} on {}:{}".format(name, server, port))
zeroconf.register_service(info)

# IR GPIO init
PWMLed = 13
state = 100

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMLed, GPIO.OUT)

breath = GPIO.PWM(PWMLed, 1000)
breath.start(0)
breath.ChangeDutyCycle(state)


def get_cpu_temp():
    temp = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = temp.read()
    temp.close()
    return float(cpu_temp) / 1000


def get_wifi_signal():
    wifi = open("/proc/net/wireless")
    signal = wifi.read()
    # m = re.findall('(wlan[0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
    wifi.close()
    return signal


# REST init
app = Flask(__name__)


@app.route("/")
def status():
    global state
    return {
        'ir': state,
        'cpu': get_cpu_temp()
    }


@app.route("/ir")
def get_ir():
    global state
    return {
        'message': 'Current PWM setting of IR LEDs',
        'state': state
    }


@app.route("/ir/<int:level>")
def set_ir(level):
    global state
    state = level
    breath.ChangeDutyCycle(state)
    return {
        'message': 'Updated PWM setting of IR LEDs',
        'state': state
    }


try:
    if __name__ == "__main__":
        port = int(os.environ.get('SERVER', 8080))
        app.run(host='0.0.0.0', port=port)
finally:
    # cleanup
    print("Unregistering...")
    zeroconf.unregister_service(info)
    zeroconf.close()
