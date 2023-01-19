#!/bin/bash

chosen=$(printf "  Power Off\n  Restart\n  Lock\n  Wifi\nX  Exit" | rofi -dmenu -i)

case "$chosen" in
	"  Power Off") poweroff ;;
	"  Restart") reboot ;;
	"  Lock") dm-tool lock ;;
	"  Wifi") sh ~/.config/qtile/scripts/rofi-wifi-menu.sh;;
	*) exit 1 ;;
esac

