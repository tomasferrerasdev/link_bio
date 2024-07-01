""" This is a simple example of a reflex component. """

import reflex as rx
from link_bio.components.navbar import navbar


class State(rx.State):
    """This is a simple example of a reflex state."""

    pass


def index() -> rx.Component:
    """This is a simple example of a reflex component."""
    return navbar()


app = rx.App()
app.add_page(index)
app._compile()
