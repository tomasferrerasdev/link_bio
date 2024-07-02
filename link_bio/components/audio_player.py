import reflex as rx


class PlayAudio(rx.State):
    is_playing: bool = False

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False


def audio_player() -> rx.Component:
    return rx.flex(
        rx.audio(
            url="audio/nightcall.mp3",
            height="0",
            volume=0.1,
            class_name="w-full max-w-[580px]",
            playing=PlayAudio.is_playing,
        ),
        rx.box(
            rx.cond(
                PlayAudio.is_playing,
                rx.button(
                    rx.image(
                        src="/photos/stop.png",
                        height="12px",
                        width="12px",
                    ),
                    class_name="bg-transparent text-white w-fit",
                    on_click=PlayAudio.stop,
                ),
                rx.button(
                    rx.image(
                        src="/photos/play.png",
                        height="12px",
                        width="12px",
                    ),
                    class_name="bg-transparent text-white w-fit",
                    on_click=PlayAudio.play,
                ),
            ),
            rx.text("Kavinsky - Nightcall", class_name="text-white text-xs"),
            class_name="flex items-center",
        ),
        direction="column",
    )
