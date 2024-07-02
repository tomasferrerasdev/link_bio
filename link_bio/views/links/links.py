import reflex as rx


def links(links: list[dict]) -> rx.Component:
    technology_components = [
        rx.link(
            tech["label"],
            href=tech["url"],
            class_name="text-red underline decoration-red hover:text-red",
        )
        for tech in links
    ]
    return rx.box(
        *technology_components,
        class_name="flex flex-col gap-1",
    )
