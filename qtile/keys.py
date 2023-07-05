from libqtile.config import Group, Key, KeyChord, Match
from libqtile.lazy import lazy

from settings import *

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, sft], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, sft], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, sft], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, sft], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, ctr], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, ctr], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, ctr], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, ctr], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, sft], rtn, lazy.layout.toggle_split(), desc="Split / unsplit of Stack"),
    Key([mod], rtn, lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, ctr], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, ctr], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "x", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod, sft], "s", lazy.spawn("scrot -s")),
    Key([mod], "r", lazy.spawn(
            "rofi -show drun -no-default-config -config ~/.config/rofi/center.rasi"
        ), desc="Launch rofi"
    ),
    KeyChord(
        [mod], "l", [
            Key([], "d", lazy.spawn("discord --enable-gpu-rasterization")),
        ],
    ),

    # Special keys
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5")),
    Key([], "XF86MonBrightnessUP", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]


workspaces = [
    {"key": "1", "matches": [Match(wm_class="firefox")], },
    {"key": "2", "matches": [], },
    {"key": "3", "matches": [Match(wm_class="Code")], },
    {"key": "4", "matches": [Match(wm_class="")], },
    {"key": "5", "matches": [Match(wm_class="Spotify")], },
    {"key": "6", "matches": [Match(wm_class="discord")], },
]


groups = [Group(f"{i}") for i in ["󰈹", "", "󰨞", "󰉋", "󰓇", "󰙯"]]

for i, (group, workspace) in enumerate(zip(groups, workspaces), start=1):
    matches = workspace["matches"] if workspace["matches"] else [] 
    groups.append(Group(group.name, matches=matches))

    keys.extend(
        [
            Key(
                [mod],
                str(i),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )
