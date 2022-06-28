from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Calculator(App):
    
    def build(self):
        
        rootWidget = BoxLayout(orientation='vertical')
        outputLabel = Label(size_hint_y=1)
        buttonSymbols = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '.', '0', '*', '/', '=')
        buttonGrid = GridLayout(cols=4, size_hint_y=2)
        
        for symbol in buttonSymbols:
            buttonGrid.add_widget(Button(text=symbol, font_size=30, bold=True))
            
        clearButton = Button(text='Clear', size_hint_y=None, font_size=25, bold=True, height=100)
        
        exitButton = Button(text='Exit', size_hint_y=None, font_size=25, bold=True, height=100)

        def printButtonText(instance):
            outputLabel.text += instance.text

        for button in buttonGrid.children[1:]:
            button.bind(on_press=printButtonText)

        def resizeLabelText(label, new_height):
            label.font_size = 0.5 * label.height

        outputLabel.bind(height=resizeLabelText)

        def evaluateResult(instance):
            try:
                eval(outputLabel.text)
            except ZeroDivisionError as err:
                outputLabel.text = str(err)
            except SyntaxError:
                outputLabel.text = "Syntax Error"
            else:
                if type(eval(outputLabel.text)) is int:
                    outputLabel.text = str(eval(outputLabel.text))
                else:
                    outputLabel.text = "%.7f" % eval(outputLabel.text)

        buttonGrid.children[0].bind(on_press=evaluateResult)

        def clearLabel(instance):
            outputLabel.text = ''

        clearButton.bind(on_press=clearLabel)
        exitButton.bind(on_press=quit)
        rootWidget.add_widget(outputLabel)
        rootWidget.add_widget(buttonGrid)
        rootWidget.add_widget(clearButton)
        rootWidget.add_widget(exitButton)
        return rootWidget


if __name__ == '__main__':
    Calculator().run()
