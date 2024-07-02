import reflex as rx


def header() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="/photos/ascii.png",
                    height="164px",
                    width="164px",
                    class_name="rounded-full",
                ),
                rx.box(
                    rx.text("Tomas Ferreras", class_name="leading-[110%]"),
                    rx.text("@tomasferrerasdev", class_name="leading-[110%]"),
                    class_name="flex flex-col gap-1",
                ),
                class_name="flex flex-col gap-4 flex-1",
            ),
            rx.image(
                src="/photos/camel.png",
                height="168px",
                width="233px",
                class_name="flex-1",
            ),
            class_name="flex items-end justify-between gap-4 w-full",
        ),
        class_name="w-full",
    )
