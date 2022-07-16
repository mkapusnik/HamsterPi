#!/bin/bash
clear && banner "" && banner "" && banner " Krecek"
if ! nmcli d | grep wifi | grep -v wifi-p2p | grep -q -v disconnected; then
  banner "No-WiFi"
else
  banner ""
fi

sleep 2
su - pi -c "cvlc --no-video-title --network-caching=100 rtsp://nanny.local:8555/unicast  &> /dev/null"

if ! nmcli d | grep wifi | grep -v wifi-p2p | grep -q -v disconnected; then
    clear && banner "" && banner "" && banner "AP mode" && banner ""
    sleep 1
    wifi-connect --portal-ssid "Kreckova Zakladna" &
fi

while true
do
  su - pi -c "cvlc --no-video-title --network-caching=100 rtsp://nanny.local:8555/unicast  &> /dev/null"
  clear && banner "" && banner "" && banner " Reload" && banner ""
  sleep 1
done
