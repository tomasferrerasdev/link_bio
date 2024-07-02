import reflex as rx


def body() -> rx.Component:
    return rx.vstack(
        rx.hstack(rx.text("?"), rx.text("Fullstack engineer"), class_name="text-green"),
        rx.box(
            rx.hstack(
                rx.text("1", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("React.JS"),
            ),
            rx.hstack(
                rx.text("2", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("Next.JS"),
            ),
            rx.hstack(
                rx.text("3", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("Node.JS"),
            ),
            rx.hstack(
                rx.text("4", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("Python"),
            ),
            rx.hstack(
                rx.text("5", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("PostgreSQL"),
            ),
            rx.hstack(
                rx.text("6", class_name="text-yellow"),
                rx.text("->", class_name="text-lightblue"),
                rx.text("MongoDB"),
            ),
            class_name="flex flex-col gap-1",
        ),
        rx.text(
            "I'm Tomas Ferreras a fullstack developer specialized on React.JS, Next.JS and Node.js.",
            class_name="max-w-[398px]",
        ),
        class_name="w-full flex flex-col gap-8",
    )
