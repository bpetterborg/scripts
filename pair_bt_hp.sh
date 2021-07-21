#!/bin/bash

bluetoothctl power on
sleep 1 
bluetoothctl scan on
sleep 0.5
bluetoothctl connect 1C:52:16:1C:10:EF