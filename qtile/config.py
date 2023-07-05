import os
import subprocess

from libqtile import bar, hook, layout, lazy, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from keys import *
from settings import *
from widgets import w_battery, w_light, w_systray, w_volume

home = os.path.expanduser("~")
script_folder = f"{home}/.config/qtile/scripts"

layouts = [
    layout.Columns(
        border_focus=colors["border_focus"],
        border_normal=colors["border_normal"],
        margin=gaps,
        border_width=border_width,
        border_on_single=False,
        grow_amount=2,
    ),
    layout.Spiral(
        border_focus=colors["border_focus"],
        border_normal=colors["border_normal"],
        margin=gaps,
        border_width=border_width,
        grow_amount=2,
    ),
    layout.Floating(
        border_focus=colors["border_focus"],
        border_normal=colors["border_normal"],
        margin=gaps,
        border_width=border_width,
        grow_amount=2,
    ),
]

widget_defaults = dict(
    font="Hack Nerd Font", fontsize=14, padding=2, background=colors["background"]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper=".config/qtile/assets/wallpaper.png",
        wallpaper_mode="fill",
        bottom=bar.Gap(10),
        left=bar.Gap(10),
        right=bar.Gap(10),
        top=bar.Bar(
            [
                widget.Spacer(
                    length=10,
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/qtile.png",
                    margin=7,
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.GroupBox(
                    fontsize=25,
                    hide_unused=False,
                    highlight_method="line",
                    # highlight_color=colors["border_normal"],
                    highlight_color=colors["base"],
                    active=colors["white"],
                    inactive=colors["gray"],
                    padding_y = 20,
                    padding_x = 20,
                    disable_drag=True,
                    this_current_screen_border=colors["blue"],
                    this_screen_border=colors["blue"],
                    other_current_screen_border='#353446',
                    other_screen_border=None,
                ),
                widget.Prompt(),
                # ----------------------------------------
                widget.Spacer(length=bar.STRETCH, background=colors["background"]),
                widget.Clock(
                    format="%b %d, %H:%M",
                    font="Roboto, Regular",
                ),
                widget.Spacer(length=bar.STRETCH, background=colors["background"]),
                # ---------------------------------------
                # w_systray,
                *w_light,
                widget.Spacer(
                    length=10,
                ),
                *w_volume,
                widget.Spacer(
                    length=10,
                ),
                *w_battery,
                widget.Spacer(
                    length=10,
                ),
                widget.CurrentLayoutIcon(
                    padding=0,
                    scale=0.6,
                    custom_icon_paths=[
                        os.path.expanduser("~/.config/qtile/assets/layout/"),
                    ],
                ),
                widget.Image(
                    filename="~/.config/qtile/assets/bar/power.png",
                    margin=8,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            f"{script_folder}/power-menu.sh"
                        )
                    },
                ),
                widget.Spacer(
                    length=10,
                ),
            ],
            35,
            margin=[6, 12, 6, 12],
            background=colors["background"],
        ),
    ),
    Screen(
        wallpaper=".config/qtile/assets/wallpaper.png",
        wallpaper_mode="fill",
        bottom=bar.Gap(10),
        left=bar.Gap(10),
        right=bar.Gap(10),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])
