""" This is a simple example of a reflex component. """

import reflex as rx


class State(rx.State):
    """This is a simple example of a reflex state."""

    pass


def index() -> rx.Component:
    """This is a simple example of a reflex component."""
    return rx.text("Hola reflex!", style={"color": "red"})


app = rx.App()
app.add_page(index)
app._compile()
