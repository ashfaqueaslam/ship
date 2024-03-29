import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(
            f'''Name : {self.name.text} {self.lastname.text}\nEmail : {self.email.text}''')
        self.name.text = ''
        self.lastname.text = ''
        self.email.text = ''

# def __init__(self, **kwargs):
#     super(MyGrid, self).__init__(**kwargs)
#     self.cols = 1

#     self.inside = GridLayout()
#     self.inside.cols = 2
#     self.inside.add_widget(Label(text='Name: '))
#     self.name = TextInput(multiline=False)
#     self.inside.add_widget(self.name)

#     self.inside.add_widget(Label(text='Lastname: '))
#     self.last_name = TextInput(multiline=False)
#     self.inside.add_widget(self.last_name)

#     self.inside.add_widget(Label(text='Email: '))
#     self.email = TextInput(multiline=False)
#     self.inside.add_widget(self.email)

#     self.add_widget(self.inside)

#     self.submit = Button(text='Submit', font_size=40)
#     self.submit.bind(on_press=self.pressed)
#     self.add_widget(self.submit)

# def pressed(self, instance):
#     name = self.name.text
#     last = self.last_name.text
#     email = self.email.text
#     print(f'''Name : {name} {last}\nEmail : {email}''')
#     self.name.text = ''
#     self.last_name.text = ''
#     self.email.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
