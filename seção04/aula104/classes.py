# Herança múltipla
from seção04.aula104.log import LogMixin


class Eletronicos:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado.')
            return
        print(f'{self._nome} está ligado.')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado.')
            return
        print(f'{self._nome} está desligado.')
        self._ligado = False
        
        
class Smartphone(Eletronicos, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado.'
            self.log_info(info)
            return
        if self._conectado:
            error = f'{self._nome} já está conectado.'
            self.log_error(error)
            return

        info = f'{self._nome} está conectado.'
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            self.log_error(error)
            return
        info = f'{self._nome} está desconectado.'
        self.log_info(info)
        self._conectado = False
