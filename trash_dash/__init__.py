from blessed import Terminal
from rich import print
from rich.align import Align
from rich.columns import Columns
from rich.live import Live

from trash_dash.screen import Screen

screen = Screen(
    "main",
    header_renderable=Columns(
        [
            Align("[bold u]TrashDash[/]", align="left", vertical="middle"),
            Align("[bold]Settings[/]", align="right", vertical="middle"),
        ],
        expand=True,
    ),
)

term = Terminal()


def run():
    """Run the app"""
    try:
        with term.fullscreen(), term.cbreak():
            with Live(screen.layout, screen=True):
                pressed_key = ""
                while pressed_key != "q":
                    pressed_key = term.inkey()
        print("[b]Exiting!")
    except KeyboardInterrupt:
        pass
