"""  """

import reflex as rx


def navbar() -> rx.Component:
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
