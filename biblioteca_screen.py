from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class BibliotecaScreen(Screen):
    def __init__(self, **kwargs):
        super(BibliotecaScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation="vertical")
        label = Label(text="Tela de Biblioteca")

        button_voltar = Button(text="Voltar ao Menu" , on_press=self.voltar_ao_menu)
        
        # Adicionando widgets ao box
        box.add_widget(button_voltar)
        box.add_widget(label)
        self.add_widget(box)

    def voltar_ao_menu(self, instance):
        # Mudando a tela atual para o menu
        self.manager.current = 'menu'