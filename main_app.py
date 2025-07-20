# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
#from runner import*
#from sits import*

class UserData():
    name = age = ruf_ind = ruf_uns = error = previus = result_1 = result_2 = result_3 = None
user_data = UserData()

def check_int(str_int):
    try:
        return int(str_int)
    except:
        return False

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
        result_1 = check_int(self.in_result_1.text)
        if result_1 == False or result_1 < 0:
            self.in_result_1.text = ""
            user_data.error.text = "Введите целое число которое не будет меньше нуля"
            user_data.previus = "second"
            self.manager.transition.direction = 'down'
            self.manager.current = 'error'
        else:
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
        result_2 = check_int(self.in_result_2.text)
        result_3 = check_int(self.in_result_3.text)
        correct = True
        if result_2 == False or result_2 < 0:
            self.in_result_2.text = ""
            correct = False
            user_data.error.text = "Введите целое число которое не будет меньше нуля"
            user_data.previus = "fourth"
            self.manager.transition.direction = 'down'
            self.manager.current = 'error'

        if result_3 == False or result_3 < 0:
            self.in_result_3.text = ""
            correct = False
            user_data.error.text = "Введите целое число которое не будет меньше нуля"
            user_data.previus = "fourth"
            self.manager.transition.direction = 'down'
            self.manager.current = 'error'

        if correct == True:
            user_data.result_2 = self.in_result_2
            user_data.result_3 = self.in_result_3
            r_index = ruffier_index(int(user_data.result_1.text),int(user_data.result_2.text),int(user_data.result_3.text))
            user_data.ruf_ind.text += str(r_index)
            level = neud_level(user_data.age)
            index_result = ruffier_result(r_index, level)
            user_data.ruf_uns.text = txt_res[index_result]

            self.manager.transition.direction = 'left'
            self.manager.current = 'fifth'

class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        btn_end = Button(text="Завершить",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        btn_again = Button(text="Начать сначала",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        user_data.ruf_ind = txt_ruf_index = Label(text = "Ваш индекс Руфье:")
        txt = Label(text = "Работоспособность сердца:")
        user_data.ruf_uns = txt_ruf_unswer = Label(text = "...")

        main_line = BoxLayout(orientation = "vertical", padding = 25, spacing = 10)
        txt_line = BoxLayout(orientation = "vertical", padding = 2, spacing = 10, size_hint = (None, 0.1),pos_hint = {"center_x":0.5})
        second_line = BoxLayout(padding = 10, spacing = 10)
        btn_again.on_press = self.again
        btn_end.on_press = self.exit

        txt_line.add_widget(txt_ruf_index)
        txt_line.add_widget(txt)
        txt_line.add_widget(txt_ruf_unswer)
        #main_line.add_widget(btn_end)
        second_line.add_widget(btn_again)
        second_line.add_widget(btn_end)
        main_line.add_widget(txt_line)
        main_line.add_widget(second_line)
        self.add_widget(main_line)

    def again(self):
        u = user_data
        u.name = u.age =  u.ruf_ind.text = u.ruf_uns.text = u.result_1.text = u.result_2.text = u.result_3.text = ""
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

    def exit(self):
        print("Хорошего давления")
        app.stop()

class ErrorScr(Screen):
    def __init__(self, name='error'):
        super().__init__(name=name)
        btn = Button(text="Вернуться",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.2),background_color = (0,0.5,0,1))
        self.txt = Label(text = "ошибка")
        user_data.error = self.txt

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        btn.on_press = self.next

        main_line.add_widget(self.txt)
        main_line.add_widget(btn)
        self.add_widget(main_line)

    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = user_data.previus

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FifthScr())
        sm.add_widget(ErrorScr())
        return sm

app = MyApp()
app.run()