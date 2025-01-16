import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class CampoMinadoApp(App):
    def __init__(self):
        super().__init__()
        self.modo_mark = False
        self.revelados_dic = {}
        self.bandeiras = set()

    def prepara_lista_minas(self):
        lista_minas = []
        qtd_minas = self.config['minas']
        while qtd_minas:
            x = random.randint(0, self.config['linhas'] - 1)
            y = random.randint(0, self.config['colunas'] - 1)
            if (x, y) not in lista_minas:
                lista_minas.append((x, y))
                qtd_minas -= 1
        return lista_minas

    def configuracoes(self):
        return {
            'minas': 10,
            'colunas': 10,
            'linhas': 10,
        }

    def pega_vizinhos(self, x, y, lista_minas):
        bombas_proximas = 0
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in direcoes:
            viz_x, viz_y = x + dx, y + dy
            if (viz_x, viz_y) in lista_minas:
                bombas_proximas += 1
        return f"{bombas_proximas:2}"

    def abrir_celula(self, x, y, button, lista_minas):
        print(self.revelados_dic)
        if self.modo_mark:
            return self.marcar_bandeira(x, y, button)
        if (x, y) in lista_minas:
            button.text = ':('
            button.background_color = (255, 0, 0, 1)
            self.exibir_popup_fim_de_jogo("Abriu uma mina!")

        else:
            minas_vizinhas = self.pega_vizinhos(x, y, lista_minas)
            self.revelados_dic[(x, y)] = minas_vizinhas
            button.text = minas_vizinhas

            if len(self.revelados_dic) == self.total_celulas:
                self.exibir_popup_fim_de_jogo("Você venceu!")

    def exibir_popup_fim_de_jogo(self, mensagem):
        """Exibe o popup perguntando se o usuário deseja reiniciar ou sair após o fim de jogo"""
        content = BoxLayout(orientation='vertical')
        label = Label(text=mensagem)
        button_reiniciar = Button(
            text="Reiniciar", size_hint_y=None, height=50)
        button_sair = Button(text="Sair", size_hint_y=None, height=50)

        button_reiniciar.bind(
            on_press=lambda _: self.reiniciar_jogo(popup))
        button_sair.bind(on_press=self.stop)

        content.add_widget(label)
        content.add_widget(button_reiniciar)
        content.add_widget(button_sair)

        popup = Popup(title="Fim de Jogo", content=content,
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def prepara_jogo(self):
        self.config = self.configuracoes()
        self.lista_minas = self.prepara_lista_minas()
        self.total_celulas = (
            self.config['colunas'] * self.config['linhas'] - self.config['minas'])

    def reiniciar_jogo(self, popup):
        popup.dismiss()
        self.__init__()
        self.prepara_jogo()
        self.grid_layout.clear_widgets()
        self.criar_grid()

    def sair_jogo(self, instance):
        """Fecha o aplicativo"""
        self.stop()

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

    def criar_grid(self):
        """Cria o grid de botões do jogo"""

        for x in range(self.config['linhas']):
            for y in range(self.config['colunas']):
                button = Button(text='', size_hint_y=None, height=40)
                button.bind(on_press=lambda instance, x=x, y=y: self.abrir_celula(
                    x, y, instance, self.lista_minas))
                self.grid_layout.add_widget(button)

    def build(self):
        """O método build() é essencialmente responsável por criar a interface gráfica do jogo,
        configurando o layout, botões e interações do usuário. Ele não executa a lógica do jogo
        diretamente (isso é feito em outros métodos), mas sim organiza os elementos visuais que
        o usuário interage."""

        """size_hint_y=None indica que o Kivy não deve redimensionar o widget verticalmente com base
          no layout. A altura do widget será determinada pela propriedade height (se definida) ou por 
          seu tamanho padrão."""

        self.prepara_jogo()
        Window.size = (Window.width, Window.height)
        self.layout = BoxLayout(orientation='vertical', padding=[0, 0, 0, 0])

        botao_alternar = Button(text="8)", size_hint_y=None, height=50)
        botao_alternar.bind(on_press=self.alternar_modo)

        self.grid_layout = GridLayout(
            cols=self.config['colunas'], spacing=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter(
            'height'))  # pegar a altura dos "filhos"

        self.criar_grid()

        self.layout.add_widget(botao_alternar)
        self.layout.add_widget(self.grid_layout)
        return self.layout


if __name__ == '__main__':
    CampoMinadoApp().run()
