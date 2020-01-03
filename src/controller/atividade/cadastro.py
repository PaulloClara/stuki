class Cadastro(object):

    def __init__(self):
        pass

    def confirmar(self, evt=None) -> None:
        """Evento click do botao confirmar cadastro."""
        formulario = self.view.atividade.cadastro.obter_campos()

        erro = self.model.atividade.validar(formulario)
        if erro:
            return self.view.janela_erro.iniciar(erro)

        atividade = self.model.atividade.cadastrar(atividade=formulario)
        self.view.atividade.cadastro.fechar()

        elemento = self.view.atividade.listagem.adicionar(atividade)
        self.configurar_(elemento)

    def cancelar(self, evt=None) -> None:
        """Evento click do botao cancelar do formulario."""
        self.view.atividade.cadastro.fechar()

    def configurar(self):
        cadastro = self.view.atividade.cadastro.subelemento

        cadastro.titulo.input.evento['<Return>'] = self.confirmar
        cadastro.descricao.input.evento['<Return>'] = self.confirmar

        cadastro.cancelar.defs.mcnf['command'] = self.cancelar
        cadastro.confirmar.defs.mcnf['command'] = self.confirmar

        self.view.atividade.cadastro.carregar_eventos()