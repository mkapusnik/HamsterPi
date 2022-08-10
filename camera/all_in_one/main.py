from zeroconf import IPVersion, ServiceInfo, Zeroconf
from flask import Flask
from timeloop import Timeloop
from datetime import timedelta
import RPi.GPIO as GPIO
import socket
import os
import re

# NSD init
server = socket.gethostname()
port = int(os.environ.get('PORT', 8555))
name = os.getenv('NAME', server.title())
desc = {'deviceName': name}
serviceType = '_nanny._tcp.local.'

info = ServiceInfo(
    serviceType,
    name + "." + serviceType,
    port=port,
    properties=desc,
    server=server + ".local.",
)

zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
print("Registration of a service {} on {}:{}".format(name, server, port))
zeroconf.register_service(info)


def get_cpu_temp():
    try:
        temp = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = temp.read()
        temp.close()
        return float(cpu_temp) / 1000
    except:
        return 0


def get_wifi_signal():
    try:
        wifi = open("/proc/net/wireless")
        signal = wifi.readlines()
        m = re.search('(?<=-)([0-9]+)', signal[2])
        wifi.close()
        return m.group(0)
    except:
        return 0


# IR GPIO init
PWMLed = 13
state = {
    "ir": 100,
    "cpu": 0,
    "wifi": 0
}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMLed, GPIO.OUT)

breath = GPIO.PWM(PWMLed, 1000)
breath.start(0)
breath.ChangeDutyCycle(state["ir"])


# REST init
app = Flask(__name__)
tl = Timeloop()


@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    global state
    state["cpu"] = get_cpu_temp()
    state["wifi"] = get_wifi_signal()


@app.route("/")
def status():
    global state
    return state


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
    state["ir"] = level
    breath.ChangeDutyCycle(state["ir"])
    return {
        'message': 'Updated PWM setting of IR LEDs',
        'state': state
    }


try:
    if __name__ == "__main__":
        port = int(os.environ.get('SERVER', 8080))
        tl.start()
        app.run(host='0.0.0.0', port=port)
finally:
    # cleanup
    print("Unregistering...")
    tl.stop()
    zeroconf.unregister_service(info)
    zeroconf.close()
