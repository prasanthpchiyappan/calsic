import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.animation import Animation

kivy.require('2.0.0')

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Input field for the calculator
        self.input_field = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.add_widget(self.input_field)
        
        # Calculator buttons
        buttons_layout = BoxLayout(orientation='vertical')
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_release=self.on_button_press)
                row_layout.add_widget(button)
            buttons_layout.add_widget(row_layout)
        
        self.add_widget(buttons_layout)

    def on_button_press(self, instance):
        current_text = self.input_field.text
        button_text = instance.text

        if button_text == 'C':
            self.input_field.text = ''
        elif button_text == '=':
            try:
                # Evaluate the expression and animate the result
                result = str(eval(self.input_field.text))
                self.animate_text_change(result)
            except Exception as e:
                self.input_field.text = 'Error'
        else:
            self.input_field.text += button_text

    def animate_text_change(self, new_text):
        animation = Animation(opacity=0, duration=0.5) + Animation(opacity=1, duration=0.5)
        animation.bind(on_complete=lambda *x: setattr(self.input_field, 'text', new_text))
        animation.start(self.input_field)

if __name__ == '__main__':
    CalculatorApp().run()
