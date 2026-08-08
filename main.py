from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SecretRoomApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text='Secret Room Support', font_size='24sp'))
        layout.add_widget(Label(text='Bot runs in background'))
        layout.add_widget(Button(text='Background service active', disabled=True))
        return layout

SecretRoomApp().run()
