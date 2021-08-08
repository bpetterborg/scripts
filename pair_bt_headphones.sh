#!/bin/bash

# This script is a needlessly overkill and complex
# way to reliably pair my bluetooth headphones
# Make sure to set the correct device_id

# variables

power_on_wait=1 # set time to wait after bt power on
scan_time=2 # time to scan for
device_id="1C:52:16:7B:B9:3F" # self explanatory, find w/ bluetoothctl scan on

# actual stuff

# power on
bluetoothctl power on
sleep $power_on_wait # wait until power on is complete

# scan
bluetoothctl scan on &
sleep $scan_time

# kill previous command
pkill --signal SIGINT --full "bluetoothctl scan on"

# connect
bluetoothctl connect $device_id


# exit script
exit 0
