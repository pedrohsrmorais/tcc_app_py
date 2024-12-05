from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
import pandas as pd
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error, r2_score
from results_screen import ResultScreen



class AnalisesScreen(Screen):
    def __init__(self, **kwargs):
        super(AnalisesScreen, self).__init__(**kwargs)

        # Criação de componentes
        self.box = BoxLayout(orientation="vertical")        
        self.label = Label(text="Tela de Análises")
        self.button_voltar = Button(text="Voltar ao Menu", on_press=self.voltar_ao_menu)
        self.input_num_espectros = TextInput(hint_text="Digite um número", input_filter='int')
        self.input_num_corantes = TextInput(hint_text="Digite um número", input_filter='int')
        self.button_verif_corantes_espectros = Button(text="Continuar", on_press=self.verif_corantes_espectros)
        self.lista_espectros = BoxLayout(orientation="vertical")
        self.button_pls = Button(text="Realizar a PLS", on_press=self.realizar_PLS)
        

        

        # Adicionando widgets ao box
        self.box.add_widget(self.button_voltar)
        self.box.add_widget(self.label)
        self.box.add_widget(self.input_num_corantes)
        self.box.add_widget(self.input_num_espectros)
        self.box.add_widget(self.button_verif_corantes_espectros)
        self.box.add_widget(self.lista_espectros)
        self.box.add_widget(self.button_pls)
        
        
        # Adicionando o layout à tela
        self.add_widget(self.box)

    # Funções ----------------------------------------

    def voltar_ao_menu(self, instance):
        self.lista_espectros.clear_widgets() 
        self.manager.current = 'menu'

    def verif_corantes_espectros(self, instance):
        try:
            num_espectros = int(self.input_num_espectros.text)
            num_corantes = int(self.input_num_corantes.text)
            
            if num_espectros > 0 and num_corantes > 0:
                
                self.lista_espectros.clear_widgets() 

                for i in range(num_espectros):
                    button = Button(text=f"Escolher arquivo Excel {i+1}", on_press=self.abrir_filechooser)
                    self.lista_espectros.add_widget(button)

            else:
                print("Os valores devem ser maiores que 0")
        except ValueError:
            print("Por favor, insira números válidos para espectros e corantes")


    def abrir_filechooser(self, instance):
        # Criação do FileChooser e restringindo a seleção a arquivos Excel
        filechooser = FileChooserIconView()
        filechooser.filters = ['*.xls', '*.xlsx']  # Apenas arquivos Excel

        # Vincula a função que será chamada quando um arquivo for selecionado
        filechooser.bind(on_selection=lambda *args: self.selecionar_arquivo(filechooser.selection))

        # Criando uma Popup para exibir o FileChooser
        popup = Popup(title="Escolha um arquivo Excel",
                      content=filechooser,
                      size_hint=(0.8, 0.8),
                      auto_dismiss=True)

        # Exibindo a Popup
        popup.open()

    def selecionar_arquivo(self, selection):
        if selection:
            # Atualiza a label com o caminho do arquivo escolhido
            arquivo_selecionado = selection[0]
            self.label.text = f"Arquivo escolhido: {arquivo_selecionado}"

            # Carregar o arquivo Excel usando o pandas
            try:
                df = pd.read_excel(arquivo_selecionado)  # Lê o arquivo Excel
                print("Conteúdo do arquivo Excel:")
                print(df.head())  # Exibe as primeiras linhas do arquivo para verificação
            except Exception as e:
                print(f"Erro ao ler o arquivo Excel: {e}")
                self.label.text = "Erro ao ler o arquivo Excel"
        else:
            self.label.text = "Nenhum arquivo escolhido"

    def realizar_PLS(self, instance):

        X = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)  
        Y = np.array([1, 2, 3, 4, 5])

        # Realizando a regressão PLS
        n_components = 1  
        pls = PLSRegression(n_components=n_components)
        pls.fit(X, Y)

        # Previsões
        Y_pred = pls.predict(X)

        # Métricas
        r2 = r2_score(Y, Y_pred)
        mse = mean_squared_error(Y, Y_pred)
        msr = mse / np.var(Y)
        coef = pls.coef_[0]  
        intercept = pls.intercept_  


        print(f"R²: {r2:.2f}")
        print(f"MSE: {mse:.2f}")
        print(f"MSR: {msr:.2f}")
        
        # Armazenando os parâmetros na tela de resultados
        result_screen = self.manager.get_screen('resultado')
        result_screen.exibir_resultados(intercept, coef, r2, mse, msr)

        # Redirecionando para a tela de resultados
        self.manager.current = 'resultado'

