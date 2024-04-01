from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import kivy
from kivy.config import Config





class MyApp(App):
    
    def build(self):
        # Create a root widget, in this case a BoxLayout
        layout = BoxLayout(orientation='vertical')
        
        self.title = 'correct'

        # Create a button and set its text
        button = Button(text="correct my sentence")

        # Bind a function to the button's on_press event
        button.bind(on_press=self.on_button_press)

        # Add the button to the layout
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # This function is called when the button is pressed
        print("Button clicked!")

def main():
    Config.set('graphics', 'width', '200')
    Config.set('graphics', 'height', '200')
    MyApp().run()
    
    

if __name__ == "__main__":
    main()