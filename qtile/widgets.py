from libqtile import widget
from settings import colors


w_battery = (
    (
        widget.Image(
            filename="~/.config/qtile/assets/bar/bat.png", 
            margin=7
        ),
        widget.Battery(
            format=" {percent:2.0%}",
            font="Roboto, Regular",
            foreground=colors["red"],
            padding=0,
        )
    )
    if False
    else (
        widget.Image(
            filename="~/.config/qtile/assets/bar/bat.png", 
            margin=7
        ),
        widget.GenPollText(
            fmt="100%",
            foreground=colors["red"],
            padding=0,
        )
    )
)


w_volume = (
    (
        widget.Image(
            filename="~/.config/qtile/assets/bar/vol.png",
            margin=8,
        ),
        widget.PulseVolume(
            font="Roboto, Regular",
            foreground=colors["blue"],
            padding=0,
        ),
    )
)


w_light = (
    (
        widget.Image(
            filename="~/.config/qtile/assets/bar/sun.png",
            margin=8,
        ),
        widget.Backlight(
            font="Roboto, Regular",
            foreground=colors["yellow"],
            brightness_file="/sys/class/backlight/intel_backlight/actual_brightness",
            max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            fontsize=12,
            padding=0,
        )
    )
    if False
    else (
        widget.Image(
            filename="~/.config/qtile/assets/bar/sun.png", 
            margin=7
        ),
        widget.GenPollText(
            fmt="100%",
            foreground=colors["yellow"],
            padding=0,
        )
    )
)