from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from menu_screen import MenuScreen
from analises_screen import AnalisesScreen
from biblioteca_screen import BibliotecaScreen
from sobre_screen import SobreScreen
from results_screen import ResultScreen

class EspectroAnalysis(App):
    def build(self):
        # Criar o ScreenManager para controlar as telas
        sm = ScreenManager()

        # Adicionar as telas ao ScreenManager
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AnalisesScreen(name='analises'))
        sm.add_widget(BibliotecaScreen(name='biblioteca'))
        sm.add_widget(SobreScreen(name='sobre'))
        sm.add_widget(ResultScreen(name="resultado"))

        # Definir a tela inicial como 'menu'
        sm.current = 'menu'

        return sm

# Rodar o aplicativo
EspectroAnalysis().run()
