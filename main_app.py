# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from seconds import *
#from runner import*
from kivy.core.window import Window
#from sits import*
Window.size = (450,800)
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
        user_data.name.text = self.in_name.text
        user_data.age = self.in_age.text
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        self.lbl_sec = Seconds(15)#15
        self.lbl_sec.bind(done=self.sec_finished)
        self.stage = False

        self.btn = Button(text="Начать",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.5),background_color = (0,0.5,0,1))
        self.btn_fast_end = Button(text="Пропустить таймер",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.5),background_color = (0,0.5,0,1))
        self.btn_fast_end.set_disabled(True)
        txt = Label(text = txt_test1)
        txt_result = Label(text = "Введите результат:")

        self.in_result_1 = TextInput(multiline = False)
        self.in_result_1.set_disabled(True)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        second_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        third_line = BoxLayout(padding = 10, spacing = 10)
        self.btn.on_press = self.next
        self.btn_fast_end.on_press = self.lbl_sec.fast_end

        second_line.add_widget(txt_result)
        second_line.add_widget(self.in_result_1)
        third_line.add_widget(self.btn)
        third_line.add_widget(self.btn_fast_end)

        main_line.add_widget(txt)
        main_line.add_widget(self.lbl_sec)
        main_line.add_widget(second_line)
        main_line.add_widget(third_line)
        self.add_widget(main_line)

    def sec_finished(self, *args):
        self.stage = True
        self.in_result_1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn_fast_end.set_disabled(True)
        self.btn.text = "Продолжить"
        return False

    def next(self):
        self.manager.transition.direction = 'left'
        result_1 = check_int(self.in_result_1.text)
        if self.stage == False:
            self.in_result_1.set_disabled(True)
            self.btn.set_disabled(True)
            self.btn_fast_end.set_disabled(False)
            self.lbl_sec.start()
        else:
            if result_1 == False or result_1 < 0:
                self.in_result_1.text = ""
                user_data.error.text = "Введите целое число которое не будет меньше нуля"
                user_data.previus = "second"
                self.manager.transition.direction = 'down'
                self.manager.current = 'error'
            else:
                self.lbl_sec.reset(15)#15
                user_data.result_1 = self.in_result_1
                self.manager.current = 'third'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        self.lbl_sec = Seconds(45)#45
        self.lbl_sec.bind(done=self.sec_finished)
        self.stage = False
        self.btn = Button(text="Начать",pos_hint = {"center_x": 0.5}, size_hint = (0.35, 0.5),background_color = (0,0.5,0,1))
        self.btn_fast_end = Button(text="Пропустить таймер",pos_hint = {"center_x": 0.5}, size_hint = (0.35, 0.5),background_color = (0,0.5,0,1))
        self.btn_fast_end.set_disabled(True)
        txt = Label(text = txt_sits)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        second_line = BoxLayout(padding = 10, spacing = 10)
        self.btn.on_press = self.next
        self.btn_fast_end.on_press = self.lbl_sec.fast_end

        second_line.add_widget(self.btn)
        second_line.add_widget(self.btn_fast_end)

        main_line.add_widget(txt)
        main_line.add_widget(self.lbl_sec)
        main_line.add_widget(second_line)
        self.add_widget(main_line)

    def sec_finished(self, *args):
        self.stage = True
        self.btn.text = "Продолжить"
        self.btn.set_disabled(False)
        self.btn_fast_end.set_disabled(True)
        return False

    def next(self):
        if self.stage == False:
            self.btn.set_disabled(True)
            self.btn_fast_end.set_disabled(False)
            self.lbl_sec.start()
        else:
            self.lbl_sec.reset(45)#45
            self.manager.transition.direction = 'left'
            self.manager.current = 'fourth'

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        self.lbl_sec = Seconds(15)#15
        self.lbl_sec.bind(done=self.sec_finished)
        self.stage = 0

        self.btn = Button(text="Начать",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.8),background_color = (0,0.5,0,1))
        self.btn_fast_end = Button(text="Пропустить таймер",pos_hint = {"center_x": 0.5}, size_hint = (0.35, 0.8),background_color = (0,0.5,0,1))
        self.btn_fast_end.set_disabled(True)
        txt = Label(text = txt_instruction)
        self.txt_need_to_do = Label(text = "Считайте пульс")
        txt_result_2 = Label(text = "Результат:")
        txt_result_3 = Label(text = "Результат после отдыха:")
        txt = Label(text = txt_test3)

        self.in_result_2 = TextInput(multiline = False)
        self.in_result_2.set_disabled(True)
        self.in_result_3 = TextInput(multiline = False)
        self.in_result_3.set_disabled(True)

        main_line = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        result_2_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        result_3_line = BoxLayout(height = "30sp", size_hint = (0.8, None))
        second_line = BoxLayout(padding = 10, spacing = 10)
        self.btn.on_press = self.next
        self.btn_fast_end.on_press = self.lbl_sec.fast_end

        result_2_line.add_widget(txt_result_2)
        result_2_line.add_widget(self.in_result_2)
        result_3_line.add_widget(txt_result_3)
        result_3_line.add_widget(self.in_result_3)
        second_line.add_widget(self.btn)
        second_line.add_widget(self.btn_fast_end)

        main_line.add_widget(txt)
        main_line.add_widget(self.txt_need_to_do)
        main_line.add_widget(self.lbl_sec)
        main_line.add_widget(result_2_line)
        main_line.add_widget(result_3_line)
        main_line.add_widget(second_line)
        self.add_widget(main_line)

    def sec_finished(self, *args):
        if self.lbl_sec.done == True:
            if self.stage == 0:
                self.stage = 1
                self.txt_need_to_do.text = "Отдыхайте"
                self.lbl_sec.restart(30)#30
                self.in_result_2.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.txt_need_to_do.text = "Считайте пульс"
                self.lbl_sec.restart(15)#15
            elif self.stage == 2:
                self.in_result_3.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn_fast_end.set_disabled(True)
                self.btn.text = "Узнать результат"
                return False

    def next(self):
        if self.stage == 0:
            self.btn.set_disabled(True)
            self.in_result_2.set_disabled(True)
            self.in_result_3.set_disabled(True)
            self.btn_fast_end.set_disabled(False)
            self.lbl_sec.start()

        else:
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
                user_data.result_1.text = ""
                user_data.result_2.text = ""
                user_data.result_3.text = ""
                user_data.ruf_ind.text += str(r_index)
                level = neud_level(user_data.age)
                index_result = ruffier_result(r_index, level)
                user_data.ruf_uns.text = txt_res[index_result]
                #if txt_name.text is None:

                self.manager.transition.direction = 'left'
                self.manager.current = 'fifth'

class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        btn_end = Button(text="Завершить",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.35),background_color = (0,0.5,0,1))
        btn_again = Button(text="Начать сначала",pos_hint = {"center_x": 0.5}, size_hint = (0.3, 0.35),background_color = (0,0.5,0,1))
        user_data.name = txt_name = Label(text = "")
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
        second_line.add_widget(btn_again)
        second_line.add_widget(btn_end)
        main_line.add_widget(txt_name)
        main_line.add_widget(txt_line)
        main_line.add_widget(second_line)
        self.add_widget(main_line)

    def again(self):
        user_data.ruf_ind.text = ""
        user_data.ruf_uns.text = ""

        app.sm.get_screen("second").stage = False
        app.sm.get_screen("second").lbl_sec.reset(15)#15
        app.sm.get_screen("second").btn.text = "Начать"
        app.sm.get_screen("second").in_result_1.set_disabled(True)

        app.sm.get_screen("third").stage = False
        app.sm.get_screen("third").lbl_sec.reset(45)#45
        app.sm.get_screen("third").btn.text = "Начать"

        app.sm.get_screen("fourth").stage = False
        app.sm.get_screen("fourth").lbl_sec.reset(15)#15
        app.sm.get_screen("fourth").btn.text = "Начать"
        app.sm.get_screen("fourth").in_result_2.set_disabled(True)
        app.sm.get_screen("fourth").in_result_3.set_disabled(True)

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
        self.sm = sm
        return sm

app = MyApp()
app.run()