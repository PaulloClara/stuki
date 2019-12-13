from src.utils import Utils


class Apresentacao:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller

        self.tabela = 'apresentacao'
        self.colunas = ['id_apresentacao', 'id_atividade', 'id_grupo',
                        'duracao', 'data_apresentacao', 'data_cadastro']

        self.apresentacoes = []

        self.obter_apresentacoes()

    def obter_apresentacao(self, id_apresentacao):
        tab, cols = self.tabela, self.colunas
        con = f'id_apresentacao == "{id_apresentacao}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_apresentacoes(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.apresentacoes = self.store.executar(codigo_sql=sql, colunas=cols)

        for apresentacao in self.apresentacoes:
            id_grupo = apresentacao['id_grupo']
            grupo = self.model.grupo.obter_grupo(id_grupo=id_grupo)

            id_atividade = apresentacao['id_atividade']
            atividade =\
                self.model.atividade.obter_atividade(id_atividade=id_atividade)

            if grupo == []:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            apresentacao['grupo'] = grupo[0]
            apresentacao['atividade'] = atividade[0]

            nome_do_grupo = apresentacao['grupo']['nome']
            titulo_da_atividade = apresentacao['atividade']['titulo']
            apresentacao['titulo'] = f'{nome_do_grupo} - {titulo_da_atividade}'

    def cadastrar_apresentacao(self, apresentacao):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        vals.append(apresentacao['id_atividade'])
        vals.append(apresentacao['id_grupo'])
        vals.append(apresentacao['duracao'])
        vals.append(apresentacao['data_apresentacao'])
        vals.append(Utils.obter_data_e_hora_atual())

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_apresentacoes()

    def remover_apresentacao(self, id_apr):
        tab, cols = self.tabela, self.colunas
        con = f'id_apresentacao = {id_apr}'

        apresentacao = self.obter_apresentacao(id_apresentacao=id_apr)[0]

        id_atividade = apresentacao['id_atividade']
        self.model.atividade.atualizar_uso(id_atividade=id_atividade, valor=0)

        id_grupo = apresentacao['id_grupo']
        self.model.grupo.atualizar_uso(id_grupo=id_grupo, valor=0)

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_apresentacoes()

    def validar_campos(self, formulario):
        return None
