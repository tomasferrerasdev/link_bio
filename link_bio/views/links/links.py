import reflex as rx


def links() -> rx.Component:
    return (
        rx.box(
            rx.link(
                "GitHub",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "LinkedIn",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "Discord",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "Youtube channel",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "Youtube channel [secondary channel]",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "Twitch [Regular broadcast]",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            rx.link(
                "Udemy Courses",
                href="https://reflex.dev",
                class_name="text-red underline decoration-red hover:text-red",
            ),
            class_name="flex flex-col gap-1",
        ),
    )
