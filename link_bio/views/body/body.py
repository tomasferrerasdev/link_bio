import reflex as rx


def body(role: str, technologies: list[str], description: str) -> rx.Component:
    technology_components = [
        rx.hstack(
            rx.text(f"{index + 1}", class_name="text-yellow"),
            rx.text("->", class_name="text-lightblue"),
            rx.text(tech),
        )
        for index, tech in enumerate(technologies)
    ]
    return rx.vstack(
        rx.hstack(rx.text("?"), rx.text(f"{role}"), class_name="text-green"),
        rx.box(
            *technology_components,
            class_name="flex flex-col gap-1",
        ),
        rx.text(
            f"{description}",
            class_name="max-w-[398px]",
        ),
        class_name="w-full flex flex-col gap-8",
    )
