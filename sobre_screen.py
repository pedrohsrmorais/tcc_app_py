from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class SobreScreen(Screen):
    def __init__(self, **kwargs):
        super(SobreScreen, self).__init__(**kwargs)
        # Criação de componentes
        box = BoxLayout(orientation="vertical")        
        label = Label(text="Tela de Sobre")
        button_voltar = Button(text="Voltar ao Menu", on_press=self.voltar_ao_menu)


        # Adicionando widget ao box
        box.add_widget(button_voltar)
        box.add_widget(label)
        
        # Adicionando o layout à tela
        self.add_widget(box)

    # Funções ----------------------------------------

    def voltar_ao_menu(self, instance):
        self.manager.current = 'menu'