#!/bin/sh

#resolution
xrandr --output DP-0 --mode 1920x1080 --rate 144 --primary --output HDMI-0 --mode 1920x1080 --rate 60 --left-of DP-0
picom -b &
nm-applet &
