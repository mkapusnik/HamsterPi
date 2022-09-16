# Baby camera

## Bill of Materials
- [Raspberry Pi 3B (or compatible)](https://rpishop.cz/raspberry-pi-3b/896-raspberry-pi-3-model-b-plus-64-bit-1gb-ram-713179640259.html)
- [Waveshare 3.5" LCD (B)](https://rpishop.cz/lcd-oled-displeje/1203-waveshare-35-lcd-b-displej-320480-dotykovy-rezistivni.html)
- [Adafruit Powerboost 1000C](https://learn.adafruit.com/adafruit-powerboost-1000c-load-share-usb-charge-boost)
- Li-Pol battery 3,7V / 4500mAh 
- [Rocker Switch](https://www.gme.cz/p-sm101-1r3)

## Installation
    touch .hushlogin && sudo rm /etc/profile.d/sshpwd.sh && sudo rm /etc/profile.d/wifi-check.sh
    sudo apt-get update && sudo apt-get install -y mc aptitude git cmake sysvbanner nodm

### LCD Screen
    git clone https://github.com/waveshare/LCD-show.git
    cd LCD-show && chmod +x LCD35B-show-V2 && ./LCD35B-show-V2

### Install dependencies
    sudo -H pip install --no-cache-dir -r requirements.txt


### Wifi AutoAP
    bash <(curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh)

### Startup script
_sudo nano /etc/rc.local_

    clear && banner "" && banner "" && banner "  Boot" && banner ""
    /usr/local/sbin/autostart &
