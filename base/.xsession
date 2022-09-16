#!/usr/bin/env bash
exec openbox-session &
while true; do
  python3 /home/pi/Documents/script.py
done