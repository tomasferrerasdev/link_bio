""" This is a simple example of a reflex component. """

import reflex as rx
from link_bio.components.audio_player import audio_player
from link_bio.views.body.body import body
from link_bio.views.header.header import header
from link_bio.views.links.links import links


data = {
    "name": "Tomas Ferreras",
    "profile_pic": "/photos/ascii.png",
    "twitter": "tomasferrerasdev",
    "role": "Software engineer",
    "technologies": [
        "React.JS",
        "Next.JS",
        "Node.JS",
        "Python",
        "PostgreSQL",
        "MongoDB",
    ],
    "description": "I'm Tomas Ferreras a fullstack developer specialized on React.JS, Next.JS and Node.js.",
    "links": [{"label": "GitHub", "url": "https://github.com/tomasferrerasdev"}],
}


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
                header(
                    name=data["name"],
                    profile_pic=data["profile_pic"],
                    twitter=data["twitter"],
                ),
                body(
                    role=data["role"],
                    technologies=data["technologies"],
                    description=data["description"],
                ),
                links(links=data["links"]),
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
