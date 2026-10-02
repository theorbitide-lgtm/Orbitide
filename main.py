from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class OrbitideApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="ORBITIDE",
            font_size=32,
            size_hint_y=None,
            height=60
        )

        message = Label(
            text="ORBITIDE AI is ready.",
            font_size=18
        )

        user_input = TextInput(
            hint_text="Type something...",
            multiline=False,
            size_hint_y=None,
            height=55
        )

        send_button = Button(
            text="SEND",
            size_hint_y=None,
            height=55
        )

        def send_message(instance):
            text = user_input.text.strip()

            if text:
                message.text = "ORBITIDE: " + text
                user_input.text = ""

        send_button.bind(on_press=send_message)

        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(user_input)
        layout.add_widget(send_button)

        return layout


if __name__ == "__main__":
    OrbitideApp().run()
