# All in one
Run all services natively, without docker

## Installation
Prepare and boot Raspberry Pi OS (32bit, bullseye) on your RPi

    touch .hushlogin && sudo rm /etc/profile.d/sshpwd.sh && sudo rm /etc/profile.d/wifi-check.sh
    echo "awb_auto_is_greyworld=1" | sudo tee -a /boot/config.txt > /dev/null
    sudo apt-get update && sudo apt-get install -y software-properties-common avahi-daemon libffi-dev libssl-dev python3-dev python3 python3-pip ladspa-sdk

### Enable camera
    sudo raspi-config

### Sound setup
    sudo pip3 install --upgrade adafruit-python-shell
    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2smic.py && sudo python3 i2smic.py

As per [this advice](https://github.com/mpromonet/v4l2rtspserver/issues/94#issuecomment-378788356), download ![asound.conf](doc/asound.conf "asound configuration") 

### RTSP server
    sudo apt-get install -y liblivemedia-dev liblog4cpp5-dev libasound2-dev cmake git
    git clone https://github.com/mpromonet/v4l2rtspserver.git
    cd v4l2rtspserver && cmake . -Wno-dev && make

### Install dependencies
    sudo -H pip install --no-cache-dir -r requirements.txt

### Startup script
Open and copy ![camera.service](camera/camera.service "Camera service")

    sudo nano /lib/systemd/system/camera.service

Open and copy ![rest.service](camera/rest.service "REST service")

    sudo nano /lib/systemd/system/rest.service

    sudo systemctl daemon-reload
    sudo systemctl enable camera.service
    sudo systemctl enable rest.service