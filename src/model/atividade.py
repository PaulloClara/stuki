from src.utils import Utils
from src.model.modelo import Modelo


class Atividade(Modelo):

    def __init__(self):
        super().__init__()

        self.tabela = 'atividade'

        self.atividade = None
        self.atividades = []

    def iniciar(self, model):
        super().iniciar(model)
        self.carregar()

    def sortear(self) -> dict or None:
        if self.atividade:
            atividade, self.atividade = self.atividade, None

            return atividade

        if not self.atividades:
            return None

        return super().sortear(lista=self.atividades)

    def obter(self, id_atividade):
        return super().obter(_id=id_atividade)

    def carregar(self):
        self.atividades = super().carregar()

    def cadastrar(self, atividade):
        vals = []
        vals.append(atividade['titulo'].capitalize())
        vals.append(atividade['descricao'].capitalize())
        vals.append(0)
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)

        self.carregar()

        return self.atividades[-1]

    def atualizar(self, id_atividade, campos: dict):
        super().atualizar(_id=id_atividade, campos=campos)

        self.carregar()

    def remover(self, id_atividade):
        super().remover(_id=id_atividade)

        for i, atividade in enumerate(self.atividades):
            if atividade['id_atividade'] == id_atividade:
                del self.atividades[i]
                break

    def validar(self, formulario):
        if formulario['titulo'] == '':
            return 'O campo "Titulo" não pode estar vazio'

        if formulario['descricao'] == '':
            return 'O campo "Descrição" não pode estar vazio'

        return None

    def limpar(self, formulario):
        formulario['titulo'] = ''
        formulario['descricao'] = ''
