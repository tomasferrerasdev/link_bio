""" This is a simple example of a reflex component. """

import reflex as rx
from link_bio.components.audio_player import audio_player
from link_bio.views.body.body import body
from link_bio.views.header.header import header
from link_bio.views.links.links import links


class State(rx.State):
    """This is a simple example of a reflex state."""

    pass


def index() -> rx.Component:
    """This is a simple example of a reflex component."""
    return rx.box(
        rx.box(
            class_name="w-full min-h-screen hidden md:block",
            style={
                "background": "url('video/donut.gif')",
                "background-size": "contain",
            },
        ),
        rx.vstack(
            rx.vstack(
                audio_player(),
                header(),
                body(),
                links(),
                class_name="w-full flex flex-col gap-14",
            ),
            class_name="max-w-[580px] w-full mx-auto bg-black px-4 py-14 relative z-10",
        ),
        rx.box(
            class_name="w-full min-h-screen hidden md:block",
            style={
                "background": "url('video/donut.gif')",
                "background-size": "contain",
            },
        ),
        class_name="min-h-screen w-full bg-black flex text-white font-sans overflow-x-hidden",
        font_family="IBM Plex Mono",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)
app.add_page(index)
app._compile()
