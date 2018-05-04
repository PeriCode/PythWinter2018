from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class GridMaker(GridLayout):
	buttons = {}
	for i in range(6):
		buttons[str(i + 1)] = str(i + 1)

	def do_press(self, numb):
		filename = "sound/audio" + self.buttons[numb] + ".mp3"
		sound = SoundLoader.load(filename)
		sound.play()

class MusicBoxApp(App):
	def build(self):
		return GridMaker()

if __name__ == "__main__":
	MusicBoxApp().run()