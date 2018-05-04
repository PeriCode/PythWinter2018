from kivy.app import App
from kivy.uix.button import Button

class My_app(App):

	def build(self):
		return Button(
			text = 'Нажми на меня!',
			font_size = 70,
			on_press = action_1)

def action_1(instance):
	instance.text = 'Наконец-то на меня нажали!'
	# print('Наконец-то на меня нажали!')

if __name__ == '__main__':
	My_app().run()

