# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
#from runner import*
#from sits import*

class UserData():
    name = age = ruf_ind = ruf_uns = None
user_data = UserData()

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text="Начать",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        txt = Label(text = txt_instruction)
        txt_name = Label(text = "Введите имя:")
        txt_age = Label(text = "Введите возраст:")
        txt = Label(text = txt_instruction)

        self.in_name = TextInput(multiline = False)
        self.in_age = TextInput(text = "7", multiline = False)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        name_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        age_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        btn.on_press = self.next

        name_line.add_widget(txt_name)
        name_line.add_widget(self.in_name)
        age_line.add_widget(txt_age)
        age_line.add_widget(self.in_age)

        main_line.add_widget(txt)
        main_line.add_widget(name_line)
        main_line.add_widget(age_line)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'left'
        user_data.name = self.in_name.text
        user_data.age = self.in_age.text
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="Продолжить",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        txt = Label(text = txt_test1)
        txt_result = Label(text = "Введите результат:")

        self.in_result_1 = TextInput(multiline = False)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        second_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        btn.on_press = self.next

        second_line.add_widget(txt_result)
        second_line.add_widget(self.in_result_1)

        main_line.add_widget(txt)
        main_line.add_widget(second_line)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'left'
        user_data.result_1 = self.in_result_1
        self.manager.current = 'third'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        btn = Button(text="Продолжить",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        txt = Label(text = txt_sits)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        btn.on_press = self.next

        main_line.add_widget(txt)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        btn = Button(text="Узнать результат",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        txt = Label(text = txt_instruction)
        txt_result_2 = Label(text = "Результат:")
        txt_result_3 = Label(text = "Результат после отдыха:")
        txt = Label(text = txt_test3)

        self.in_result_2 = TextInput(multiline = False)
        self.in_result_3 = TextInput(multiline = False)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        result_2_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        result_3_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        btn.on_press = self.next

        result_2_line.add_widget(txt_result_2)
        result_2_line.add_widget(self.in_result_2)
        result_3_line.add_widget(txt_result_3)
        result_3_line.add_widget(self.in_result_3)

        main_line.add_widget(txt)
        main_line.add_widget(result_2_line)
        main_line.add_widget(result_3_line)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'left'
        user_data.result_2 = self.in_result_2.text
        user_data.result_3 = self.in_result_3.text
        user_data.ruf_uns.text = "хорошее"
        self.manager.current = 'fifth'

class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        btn = Button(text="удалить кнопку")
        user_data.ruf_ind = txt_ruf_index = Label(text = "Ваш индекс Руфье:")
        txt = Label(text = "Работоспособность вашего сердца:")
        user_data.ruf_uns = txt_ruf_unswer = Label(text = "...")

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        btn.on_press = self.next

        main_line.add_widget(txt_ruf_index)
        main_line.add_widget(txt)
        main_line.add_widget(txt_ruf_unswer)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FifthScr())
        return sm

app = MyApp()
app.run()