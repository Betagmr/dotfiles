#!/bin/bash

chosen=$(printf "  Power Off\n  Restart\n  Lock\nX  Exit" | rofi -dmenu -i)

case "$chosen" in
	"  Power Off") poweroff ;;
	"  Restart") reboot ;;
	"  Lock") slock ;;
	*) exit 1 ;;
esac

