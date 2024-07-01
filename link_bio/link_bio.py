""" This is a simple example of a reflex component. """

import reflex as rx


class State(rx.State):
    """This is a simple example of a reflex state."""

    pass


def index() -> rx.Component:
    """This is a simple example of a reflex component."""
    return rx.hstack(
        rx.text(
            "Tomas Ferreras Fullstack developer",
            height="40px",
            color="white",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        position="sticky",
        bg="black",
        padding="16px",
        z_index=10,
    )


app = rx.App()
app.add_page(index)
app._compile()
