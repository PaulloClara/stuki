from src.utils.tk import TKUtils


class JanelaDeCadastro(TKUtils.Janela()):

    def __init__(self, titulo):
        super().__init__()

        self.eventos = None
        self.titulo = titulo

        self.corpo = None
        self.botao_cancelar = None
        self.botao_confirmar = None

    def iniciar(self, texto):
        self.title(self.titulo)
        self.geometry('340x240')
        self.resizable(0, 0)

        self.criar_corpo()

        self.criar_botao_cancelar()
        self.criar_botao_confirmar(texto=texto)

    def criar_corpo(self):
        self.corpo = TKUtils.obter_container(master=self, cnf={'bd': 10})

    def criar_botao_cancelar(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Cancelar'
        cnf['bg'] = 'red'
        cnf['command'] = self.eventos['cancelar']

        grid['row'] = 3
        grid['column'] = 0
        grid['sticky'] = 'W'
        grid['pady'] = 320 - self.winfo_screenmmheight()

        self.botao_cancelar =\
            TKUtils.obter_botao(master=self.corpo, cnf=cnf, grid=grid)

    def criar_botao_confirmar(self, texto):
        cnf, grid = {}, {}

        cnf['text'] = texto
        cnf['bg'] = 'green'
        cnf['command'] = self.eventos['confirmar']

        grid['row'] = 3
        grid['column'] = 1
        grid['sticky'] = 'E'
        grid['pady'] = 320 - self.winfo_screenmmheight()

        self.botao_confirmar =\
            TKUtils.obter_botao(master=self.corpo, cnf=cnf, grid=grid)
