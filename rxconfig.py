import reflex as rx

config = rx.Config(
    app_name="link_bio",
    tailwind={
        "theme": {
            "extend": {
                "colors": {
                    "green": "#61FF00",
                    "pink": "#DC0AFE",
                    "lightblue": "#0AEFFE",
                    "yellow": "#FFE604",
                    "red": "#FF0404",
                    "black": "#000",
                    "white": "#FFF",
                }
            },
            "font-family": {
                "sans": ["IBM Plex Mono", "sans-serif"],
            },
        },
    },
)
