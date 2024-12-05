from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        box = BoxLayout(orientation="vertical")
        
        # Criar os botões do menu
        button_analises = Button(text="Análises")
        button_biblioteca = Button(text="Biblioteca")
        button_sobre = Button(text="Sobre")
        
        # Adicionar os botões ao layout
        box.add_widget(button_analises)
        box.add_widget(button_biblioteca)
        box.add_widget(button_sobre)
        
        # Adicionar a ação de troca de telas
        button_analises.bind(on_press=self.show_analises)
        button_biblioteca.bind(on_press=self.show_biblioteca)
        button_sobre.bind(on_press=self.show_sobre)
        
        self.add_widget(box)

    def show_analises(self, instance):
        self.manager.current = 'analises'

    def show_biblioteca(self, instance):
        self.manager.current = 'biblioteca'

    def show_sobre(self, instance):
        self.manager.current = 'sobre'
    

