from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from plyer import vibrator
import random

class LovePrank(App):
    def build(self):
        self.no_count = 0
        self.sound = SoundLoader.load("funny.wav")

        layout = FloatLayout()

        label = Label(
            text="Do you love me? ❤️",
            font_size=30,
            pos_hint={"center_x": 0.5, "top": 0.9}
        )

        self.counter = Label(
            text="NO clicked: 0 times",
            font_size=18,
            pos_hint={"center_x": 0.5, "y": 0.55}
        )

        yes_btn = Button(
            text="YES 😊",
            size_hint=(0.3, 0.15),
            pos_hint={"x": 0.1, "y": 0.2}
        )
        yes_btn.bind(on_press=self.yes_clicked)

        no_btn = Button(
            text="NO 😈",
            size_hint=(0.3, 0.15),
            pos_hint={"x": 0.6, "y": 0.2}
        )
        no_btn.bind(on_press=self.no_clicked)

        layout.add_widget(label)
        layout.add_widget(self.counter)
        layout.add_widget(yes_btn)
        layout.add_widget(no_btn)

        self.label = label
        self.no_btn = no_btn

        return layout

    def no_clicked(self, instance):
        self.no_count += 1
        self.counter.text = f"NO clicked: {self.no_count} times"

        instance.pos_hint = {
            "x": random.uniform(0, 0.7),
            "y": random.uniform(0, 0.7)
        }
        instance.parent.do_layout()

        try:
            vibrator.vibrate(0.15)
        except:
            pass

        if self.sound:
            self.sound.play()

    def yes_clicked(self, instance):
        self.label.text = "I knew it 😍❤️"
        self.counter.text = f"You tried NO {self.no_count} times 😂"

LovePrank().run()
