from tkinter import Message
from src.utils.tk.elemento import Elemento


class MMensagem(Message, Elemento):

    def __init__(self) -> None:
        Elemento.__init__(self)

        self.defs.cnf['text'] = 'MENSAGEM'
        self.defs.cnf['font'] = ('times new roman', 14, 'italic')

    def iniciar(self, master: object) -> None:
        if 'fz' in self.defs.mcnf:
            fonte = self.defs.cnf['font']
            self.defs.cnf['font'] = (fonte[0], self.defs.mcnf['fz'], fonte[2])

        Message.__init__(self, master=master, cnf=self.defs.cnf)
        self.mostrar()
