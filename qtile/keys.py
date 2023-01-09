from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Group, Key, Match, Screen
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
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
]


groups = [Group(f" {i} ") for i in ["", "", "﬏", "", "阮"]]

for i, group in enumerate(groups, start=1):
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
