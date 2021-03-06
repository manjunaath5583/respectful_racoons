"""Main screen"""
from rich.align import Align
from rich.columns import Columns
from rich.console import RenderGroup
from rich.padding import Padding

from trash_dash.body import body
from trash_dash.events import emit, on, once
from trash_dash.screen import Screen
from trash_dash.settings import get_settings


def create_screen() -> Screen:
    """Creates and returns a screen"""
    app_settings = get_settings()
    body_renderable, body_destroy, body_update = body()
    screen = Screen(
        "main",
        header_renderable=Padding(
            RenderGroup(
                Columns(
                    [
                        Align(
                            f"[bold u]{app_settings.get('app_name', 'TrashDash')}[/]",
                            align="left",
                            vertical="middle",
                        ),
                        Align(
                            "[bold]Settings(s)    Exit(q)[/]",
                            align="right",
                            vertical="middle",
                        ),
                    ],
                    expand=True,
                ),
                Align("Use the [yellow]keyboard[/] to navigate!", align="center"),
            ),
            (1, 3, 0, 3),
        ),
        body_renderable=body_renderable,
    )

    def el():
        screen.render_body(body_update())
        emit("main.update", screen.layout)

    once("main.destroy", body_destroy)
    on("main.event_loop", el)

    return screen
