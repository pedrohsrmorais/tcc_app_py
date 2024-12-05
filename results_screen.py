from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore



class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

        # Criando Widget
        self.box = BoxLayout(orientation="vertical")
        self.box_sair_salvar = BoxLayout(orientation="horizontal")
        self.label_resultados = Label(text="Resultados da PLS")
        self.button_salvar = Button(text="Salvar Resultado", on_press=self.salvar_resultados)
        self.button_sair = Button(text="Sair", on_press=self.voltar_ao_menu)
        self.blankbox = BoxLayout()

        # Adicionando Widgets ao box secundários
        self.box_sair_salvar.add_widget(self.button_sair)
        self.box_sair_salvar.add_widget(self.button_salvar)

        # Adicionando Widgets ao box principal
        self.box.add_widget(self.label_resultados)
        self.box.add_widget(self.blankbox)
        self.box.add_widget(self.box_sair_salvar)

        self.add_widget(self.box)

    def exibir_resultados(self, intercept, coef, r2, mse, msr):
        equacao = f"Equação da Reta: Y = {intercept[0]:.2f} + {coef[0]:.2f} * X"
        resultados = f"R²: {r2:.2f}\nMSE: {mse:.2f}\nMSR: {msr:.2f}"

        self.label_resultados.text = f"{equacao}\n\n{resultados}"

        # Armazenando resultados em atributos da tela para usar em outros métodos
        self.intercept = intercept
        self.coef = coef
        self.r2 = r2
        self.mse = mse
        self.msr = msr

    def salvar_resultados(self, instance):
        try:
            # Usando JsonStore para salvar os resultados de forma simples
            store = JsonStore('resultados_pls.json')
            store.put('resultados', intercept=self.intercept[0], coef=self.coef[0], r2=self.r2, mse=self.mse, msr=self.msr)

            # Exibindo uma mensagem de sucesso
            popup = Popup(title="Sucesso",
                        content=Label(text="Resultados salvos com sucesso!"),
                        size_hint=(None, None), size=(400, 200))
            popup.open()
        except Exception as e:
            # Exibindo uma mensagem de erro
            popup = Popup(title="Erro",
                        content=Label(text=f"Erro ao salvar os resultados: {str(e)}"),
                        size_hint=(None, None), size=(400, 200))
            popup.open()

    def voltar_ao_menu(self, instance):
        # Voltando para a tela de menu
        self.manager.current = 'menu'
