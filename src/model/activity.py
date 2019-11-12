class Activity:

    def __init__(self, controller, store):
        self.__store = store
        self.__controller = controller

        self.table = 'activity'
        self.columns = ['activity_id', 'title', 'desc', 'deadline']

        self.activities = []

        self.get_activities()

    def get_activities(self):
        sql_code = self.__store.select(table=self.table, columns=self.columns)
        self.activities =\
            self.__store.run(sql_code=sql_code, columns=self.columns)

    def register_activity(self, activity):
        values = [activity['title'], activity['desc'], activity['deadline']]

        sql_code = self.__store.insert(
            table=self.table, columns=self.columns[1:], values=values)

        self.__store.run(sql_code=sql_code)
        self.get_activities()

    def remove_activity(self, activity_id):
        condition = f'activity_id = {activity_id}'
        sql_code = self.__store.delete(table=self.table, condition=condition)

        self.__store.run(sql_code=sql_code)
        self.get_activities()

    def check_form(self, form):
        if form['title'] == '':
            return 'O campo "Titulo" não pode estar vazio'
        if form['desc'] == '':
            return 'O campo "Descrição" não pode estar vazio'
        if form['deadline'] == '':
            return 'O campo "Data de Entrega" não pode estar vazio'

        deadline = form['deadline'].replace('/', '')
        if len(deadline) != 8:
            return 'Campo "Data de Entrega" invalido'

        return 'ok'

    def reset_form(self, form):
        form['title'] = ''
        form['desc'] = ''
        form['deadline'] = ''
