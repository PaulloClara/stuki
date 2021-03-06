from src.utils.tk import TKUtils


class Actions(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['bd'] = 10
        self.defs.pack['expand'] = True
        self.defs.pack['side'] = 'bottom'

        self.subelemento.cadastrar = TKUtils.obter_botao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_cadastro()

    def inicializar_botao_cadastro(self):
        self.subelemento.cadastrar.defs.cnf['text'] = 'Gerar Grupos'
        self.subelemento.cadastrar.defs.cnf['bg'] = 'green'
        self.subelemento.cadastrar.defs.cnf['width'] = 20

        self.subelemento.cadastrar.defs.pack['side'] = 'right'

        self.subelemento.cadastrar.iniciar(master=self)
