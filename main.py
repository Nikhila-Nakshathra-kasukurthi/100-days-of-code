import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.text import LabelBase

# Register the custom font
LabelBase.register(name='NeonFont', fn_regular='fonts/f24q203-neonlux-neonlux-regular-400.ttf')

class RockPaperScissorsGame(BoxLayout):
    user_choice = StringProperty("fist_left.jpg")
    computer_choice = StringProperty("fist_right.jpg")
    result_text = StringProperty("")
    win_count = NumericProperty(0)
    draw_count = NumericProperty(0)
    loss_count = NumericProperty(0)
    options = ['rock', 'paper', 'scissor']

    def user_select(self, choice):
        self.user_choice = f"{choice}.jpg"
        self.computer_choice = f"{random.choice(self.options)}_right.jpg"
        self.determine_winner(choice)

    def determine_winner(self, user_choice):
        comp_choice = self.computer_choice.split('_')[0]
        if user_choice == comp_choice:
            self.result_text = "It's a draw!"
            self.draw_count += 1
        elif (user_choice == 'rock' and comp_choice == 'scissor') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissor' and comp_choice == 'paper'):
            self.result_text = "You won!"
            self.win_count += 1
        else:
            self.result_text = "You lost!"
            self.loss_count += 1

    def reset_game(self):
        self.user_choice = "fist_left.jpg"
        self.computer_choice = "fist_right.jpg"
        self.result_text = ""

class RockPaperScissorsApp(App):
    def build(self):
        return RockPaperScissorsGame()

if __name__ == "__main__":
    RockPaperScissorsApp().run()
