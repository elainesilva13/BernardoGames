import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class CampoMinadoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modo_mark = False  
        self.revelados_dic = {}  
        self.bandeiras = set()  
        self.jogo_ativo = True  

    def prepara_lista_minas(self, config):
        lista_minas = []
        qtd_minas = config['minas']
        while qtd_minas:
            x = random.randint(0, config['linhas'] - 1)
            y = random.randint(0, config['colunas'] - 1)
            if (x, y) not in lista_minas:
                lista_minas.append((x, y))
                qtd_minas -= 1
        return lista_minas

    def configuracoes(self):
        return {
            'minas': 10,
            'colunas': 10,
            'linhas': 10
        }

    def pega_vizinhos(self, x, y, lista_minas):
        bombas_proximas = 0
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in direcoes:
            viz_x, viz_y = x + dx, y + dy
            if (viz_x, viz_y) in lista_minas:
                bombas_proximas += 1
        return f"{bombas_proximas:2}"

    def abrir_celula(self, x, y, button, config, lista_minas):
        if self.modo_mark:
            return self.marcar_bandeira(x, y, button)
        if (x, y) in lista_minas:
            button.text = 'X'
            button.background_color = (1, 0, 0, 1)
            popup = Popup(title="Fim de Jogo", content=Label(text="Você perdeu!"), size_hint=(None, None), size=(400, 400))
            popup.open()
            self.jogo_ativo = False
            return True
        else:
            minas_vizinhas = self.pega_vizinhos(x, y, lista_minas)
            self.revelados_dic[(x, y)] = minas_vizinhas
            button.text = minas_vizinhas
            if len(self.revelados_dic) == (config['colunas'] * config['linhas'] - config['minas']):
                popup = Popup(title="Vitória", content=Label(text="Você venceu!"), size_hint=(None, None), size=(400, 400))
                popup.open()
                self.jogo_ativo = False
                return True
        return False

    def marcar_bandeira(self, x, y, button):
        if (x, y) not in self.revelados_dic:
            if button.text == '':
                button.text = 'bomba'
                button.background_color = (0, 1, 0, 1)
                self.bandeiras.add((x, y))
            elif button.text == 'bomba':
                button.text = ''
                button.background_color = (1, 1, 1, 1)
                self.bandeiras.remove((x, y))

    def alternar_modo(self, button):
        self.modo_mark = not self.modo_mark
        modo = "<|" if self.modo_mark else "8)"
        print(f"Modo alterado para {modo}.")
        button.text = modo

    def build(self):
        config = self.configuracoes()
        lista_minas = self.prepara_lista_minas(config)

        self.layout = BoxLayout(orientation='vertical')

        botao_alternar = Button(text="8)", size_hint_y=None, height=50)
        botao_alternar.bind(on_press=self.alternar_modo)

        self.grid_layout = GridLayout(cols=config['colunas'], spacing=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))

        for x in range(config['linhas']):
            for y in range(config['colunas']):
                button = Button(text='', size_hint_y=None, height=40)
                button.bind(on_press=lambda instance, x=x, y=y: self.abrir_celula(x, y, instance, config, lista_minas))
                self.grid_layout.add_widget(button)

        self.layout.add_widget(botao_alternar)
        self.layout.add_widget(self.grid_layout)
        return self.layout

if __name__ == '__main__':
    CampoMinadoApp().run()
