#to use kivy you have to import all the kivy modules you need,
#like for example i need to import ap to make an app
#box layout to make it look like a box
#button to make buttons, text input to make input for the numbers 
#grid layout to make a grid layout and window to make the window of the app


from kivy.app import App #this runs the app and stores everything
from kivy.uix.boxlayout import BoxLayout #this is the layout of the app
from kivy.uix.button import Button #this is the button widget
from kivy.uix.textinput import TextInput #this is the text input widget
from kivy.uix.gridlayout import GridLayout #this is the grid layout widget
from kivy.core.window import Window  #this is the window of the app


Window.size = (400, 600) # Set the window size to 400x600 pixels

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        #building out the app
        
        self.result = TextInput(
            font_size=32,
            size_hint=(1, 0.2),
            readonly=True,
            halign='right',
            multiline=False,
            background_color=(0.2,0.2, 0.2, 1),  
            foreground_color=(1, 1, 1, 1)  # White text color

        )
        self.add_widget(self.result)    

        #for the buttons
        buttons = [
            [ 'C', '+/-', '%', '/' ],
            [ '7', '8', '9', '*' ],
            [ '4', '5', '6', '-' ],
            [ '1', '2', '3', '+' ],
            [ '0', '00', '.', '=']
        ]
        #creating the grid layout for the buttons
        grid = GridLayout(cols=4, spacing=6,padding=10)
        for row in buttons:
            for item in row:
                button = Button(
                    text=item,
                    font_size=24,
                    background_color=self.button_color(item),  # Set button color based on label
                    on_press=self.on_button_press,
                )
                grid.add_widget(button)
        self.add_widget(grid)

    def button_color(self, label):
        # Set the color of the button based on its label
        if label in {'C', '+/-', '%', '='}:
            return [0.6, 0.6, 0.6, 1]
        elif label in {'/', '*', '-', '+'}:
            return [0, 1, 0, 1]
        return [0.3, 0.3, 0.3, 1]  # Default color for numbers










    
    def on_button_press(self, instance):
        # Handle button press events
        text = instance.text
        if text == 'C':
            self.result.text = ''  # Clear the result
        elif text == '=':
            self.calculate()
        elif text == '+/-':
            self.toggle_sign()
        elif text == '%':
            self.convert_to_float()
        else:
           #take the text from the button and add it to the result
            self.result.text += text


    #calculating method
    def calculate(self):
        # This method will evaluate the expression in the result TextInput
        try:
            self.result.text = str(eval(self.result.text))
        except Exception as e:
            self.result.text = 'Error'

    def toggle_sign(self):
        # Toggle the sign of the current result
        if self.result.text:
            self.result.text = self.result.text[1:] if self.result.text.startswith('-') else '-' + self.result.text
    def convert_to_float(self):
        # Convert the result to float
        try:
            self.result.text = str(float(self.result.text)/100)
        except ValueError:
            self.result.text = 'Error'


class CalculatorApp(App):
    def build(self):
          # Set the window size
        return Calculator()
    

if __name__ == '__main__':
    CalculatorApp().run()  #this runs the app
